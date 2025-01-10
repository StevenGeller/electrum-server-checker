"""Command-line interface for BitKey Electrum Server Checker.

This module provides the command-line interface for checking Electrum server
compatibility with BitKey and showing available connection methods.
"""
from typing import Dict, Optional
import sys
import warnings
import requests
from .checker import check_server


def print_results(results: Dict[str, bool]) -> None:
    """Print the server check results in a user-friendly format.

    Args:
        results: Dictionary containing server check results
    """
    print("\nResults:")
    print("-" * 50)
    print(f"Server: {results['address']}")
    
    # First check BitKey compatibility
    print("\nBitKey Compatibility:")
    if results['ssl']:
        print("✅ This server is COMPATIBLE with BitKey (SSL port 50002 is available)")
        print(f"   Connection string for BitKey: ssl://{results['address']}:50002")
    else:
        print("❌ This server is NOT COMPATIBLE with BitKey (requires SSL port 50002)")
    
    print("\nAll Available Connection Methods:")
    if results['tcp']:
        print(f"• TCP     - tcp://{results['address']}:50001")
    if results['ssl']:
        print(f"• SSL/TLS - ssl://{results['address']}:50002")
    if results['http']:
        print(f"• HTTP    - http://{results['address']}:50001")
    if results['https']:
        print(f"• HTTPS   - https://{results['address']}:50002")
    if results['onion']:
        print("• Onion   - .onion address detected (requires Tor)")
    
    if not any([results['tcp'], results['ssl'], results['http'], results['https'], results['onion']]):
        print("❌ No connection methods available or server is not responding")


def main() -> None:
    """Main entry point for the command-line interface."""
    # Suppress SSL warnings
    warnings.filterwarnings('ignore', category=Warning)
    requests.packages.urllib3.disable_warnings()

    if len(sys.argv) != 2:
        print("BitKey Electrum Server Checker")
        print("Check if an Electrum server is compatible with BitKey and show all available connection methods.")
        print("\nUsage: electrum-server-check <server_address>")
        print("Examples:")
        print("  electrum-server-check example.com")
        print("  electrum-server-check electrum.blockstream.info")
        print("  electrum-server-check abc123.onion")
        sys.exit(1)
    
    server_address = sys.argv[1]
    results = check_server(server_address)
    print_results(results)


if __name__ == "__main__":
    main()