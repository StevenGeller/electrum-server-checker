# BitKey Electrum Server Checker

[![PyPI version](https://badge.fury.io/py/electrum-server-checker.svg)](https://badge.fury.io/py/electrum-server-checker)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python 3.7+](https://img.shields.io/badge/python-3.7+-blue.svg)](https://www.python.org/downloads/)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)

An unofficial command-line tool to check if an Electrum server is compatible with BitKey and show all available connectivity options. This tool helps BitKey users verify their Electrum server configuration before setup.

## Features

- 🔒 **BitKey Compatibility Check**:
  - Verifies SSL/TLS (port 50002) availability required for BitKey
  - Clear indication if server is compatible
  - Provides exact connection string for BitKey configuration
- 🔍 **Connection Methods Detection**:
  - TCP (port 50001)
  - SSL/TLS (port 50002)
  - HTTP
  - HTTPS
  - Onion (Tor) address detection
- 🚀 **Easy to Use**:
  - Simple command-line interface
  - Clear, color-coded output
  - Support for both domain names and IP addresses
- 🛡️ **Security First**:
  - Helps ensure secure SSL/TLS connections
  - Identifies Tor onion addresses
  - Warns about insecure connection methods

## Quick Start

```bash
# Install from PyPI
pip install electrum-server-checker

# Check a server
electrum-server-check electrum.blockstream.info
```

## Installation

### From PyPI
```bash
pip install electrum-server-checker
```

### From Source
```bash
# Clone the repository
git clone <repository-url>
cd electrum-server-checker

# Create and activate virtual environment (recommended)
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install the package
pip install -e .
```

## Usage

### Basic Usage
```bash
electrum-server-check your-server-address
```

### Examples
```bash
# Check a domain
electrum-server-check electrum.blockstream.info

# Check an IP address
electrum-server-check 192.168.1.100

# Check a Tor onion address
electrum-server-check abcdef123456.onion
```

### Example Output
```
Checking connectivity for electrum.blockstream.info...
[*] Checking TCP port 50001...
[*] Checking SSL port 50002...
[*] Checking HTTP...
[*] Checking HTTPS...

Results:
--------------------------------------------------
Server: electrum.blockstream.info

BitKey Compatibility:
✅ This server is COMPATIBLE with BitKey (SSL port 50002 is available)
   Connection string for BitKey: ssl://electrum.blockstream.info:50002

All Available Connection Methods:
• TCP     - tcp://electrum.blockstream.info:50001
• SSL/TLS - ssl://electrum.blockstream.info:50002
```

## BitKey Integration

BitKey requires SSL/TLS connection on port 50002 for secure communication with Electrum servers. This tool helps users:

1. ✅ Verify server compatibility before setup
2. 🔒 Ensure secure SSL/TLS availability
3. 📝 Get the exact connection string for configuration
4. 🔍 View all available connection methods

## API Usage

You can also use the tool programmatically:

```python
from electrum_server_checker import check_server

# Check a server
results = check_server('electrum.blockstream.info')

# Check BitKey compatibility
if results['ssl']:
    print("Server is compatible with BitKey")
    print(f"Connection string: ssl://{results['address']}:50002")
```

## Development

### Setting up Development Environment

```bash
# Clone the repository
git clone <repository-url>
cd electrum-server-checker

# Create virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install development dependencies
pip install -e ".[dev]"
```

### Running Tests

```bash
pytest
```

### Code Style

We use:
* Black for code formatting
* isort for import sorting
* flake8 for style guide enforcement

```bash
# Format and check code
black .
isort .
flake8
```

## Contributing

We welcome contributions! Please see our [Contributing Guidelines](CONTRIBUTING.md) for details on how to submit pull requests, report issues, and contribute to the project.

## Security

Security is important to us. If you discover a security vulnerability, please follow the guidelines in our [Security Policy](SECURITY.md).

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- BitKey team for their work on Bitcoin security
- Electrum developers for their excellent wallet software
- The Bitcoin community for their continued support

---
Made with ❤️ by the Bitcoin community