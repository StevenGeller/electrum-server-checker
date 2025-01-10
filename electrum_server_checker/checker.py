"""Check Electrum server compatibility with BitKey.

This module provides functions to verify if an Electrum server is compatible with
BitKey and shows all available connection methods.
"""
from typing import Dict, Optional
import socket
import requests
from urllib.parse import urlparse


def check_tcp_port(host: str, port: int) -> bool:
    """Check if a TCP port is open on a host.

    Args:
        host: The hostname or IP address to check
        port: The port number to check

    Returns:
        bool: True if the port is open, False otherwise
    """
    try:
        sock = socket.create_connection((host, port), timeout=5)
        sock.close()
        return True
    except (socket.timeout, socket.error):
        return False


def check_http_endpoint(url: str) -> bool:
    """Check if an HTTP endpoint is available.

    Args:
        url: The URL to check

    Returns:
        bool: True if the endpoint returns 200, False otherwise
    """
    try:
        response = requests.get(url, timeout=5, verify=False)
        return response.status_code == 200
    except requests.exceptions.RequestException:
        return False


def is_onion_address(address: str) -> bool:
    """Check if an address is a Tor onion address.

    Args:
        address: The address to check

    Returns:
        bool: True if the address is an onion address, False otherwise
    """
    return address.endswith('.onion')


def check_server(address: str) -> Dict[str, bool]:
    """Check an Electrum server for available connection methods.

    Args:
        address: The server address to check (domain, IP, or onion)

    Returns:
        dict: A dictionary containing the availability of each connection method:
            {
                'address': str,  # The normalized server address
                'tcp': bool,     # TCP port 50001 availability
                'ssl': bool,     # SSL port 50002 availability (required for BitKey)
                'http': bool,    # HTTP endpoint availability
                'https': bool,   # HTTPS endpoint availability
                'onion': bool    # Whether this is an onion address
            }

    Raises:
        ValueError: If address is empty or None
    """
    if not address:
        raise ValueError("Server address cannot be empty")

    results = {
        'address': address,
        'tcp': False,
        'ssl': False,
        'http': False,
        'https': False,
        'onion': False
    }
    
    # Parse the address
    if not (address.startswith('http://') or address.startswith('https://')):
        parsed = urlparse(f'http://{address}')
    else:
        parsed = urlparse(address)
    
    host = parsed.hostname or address
    results['address'] = host
    
    # Check if it's an onion address
    if is_onion_address(host):
        print(f"[*] Detected .onion address: {host}")
        results['onion'] = True
        print("[!] To connect to .onion addresses, make sure you have Tor configured")
        return results

    # Check standard Electrum ports
    print(f"\nChecking connectivity for {host}...")
    
    print("[*] Checking TCP port 50001...")
    results['tcp'] = check_tcp_port(host, 50001)
    
    print("[*] Checking SSL port 50002...")
    results['ssl'] = check_tcp_port(host, 50002)
    
    print("[*] Checking HTTP...")
    results['http'] = check_http_endpoint(f'http://{host}:50001')
    
    print("[*] Checking HTTPS...")
    results['https'] = check_http_endpoint(f'https://{host}:50002')
    
    return results