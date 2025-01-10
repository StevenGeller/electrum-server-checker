# BitKey Electrum Server Checker Documentation

Welcome to the BitKey Electrum Server Checker documentation. This tool helps you verify if an Electrum server is compatible with BitKey and shows all available connection methods.

## Why Use This Tool?

BitKey requires secure SSL/TLS connections to Electrum servers. This tool helps you:

1. ✅ Verify server compatibility before setup
2. 🔒 Ensure secure SSL/TLS availability
3. 📝 Get the exact connection string for configuration
4. 🔍 View all available connection methods

## Quick Start

```bash
# Install from PyPI
pip install electrum-server-checker

# Check a server
electrum-server-check electrum.blockstream.info
```

## Features

### BitKey Compatibility Check

The tool verifies if a server supports SSL/TLS connections on port 50002, which is required for BitKey:

```bash
BitKey Compatibility:
✅ This server is COMPATIBLE with BitKey (SSL port 50002 is available)
   Connection string for BitKey: ssl://electrum.blockstream.info:50002
```

### Connection Methods Detection

Checks multiple connection methods:

- TCP (port 50001)
- SSL/TLS (port 50002)
- HTTP
- HTTPS
- Onion (Tor) addresses

### Security Features

- SSL/TLS verification
- Tor address detection
- Clear security warnings
- Connection string validation

## Next Steps

- [Installation Guide](guide/installation.md)
- [Usage Examples](guide/examples.md)
- [BitKey Integration](bitkey/overview.md)
- [API Reference](development/api.md)