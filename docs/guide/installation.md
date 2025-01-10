# Installation Guide

This guide will help you install the BitKey Electrum Server Checker on your system.

## Prerequisites

- Python 3.7 or later
- pip (Python package installer)
- Optional: virtualenv or venv for isolated environments

## Installation Methods

### 1. From PyPI (Recommended)

The simplest way to install is using pip:

```bash
pip install electrum-server-checker
```

This will install the latest stable version from PyPI.

### 2. From Source

For the latest development version or if you want to contribute:

```bash
# Clone the repository
git clone https://github.com/StevenGeller/electrum-server-checker.git
cd electrum-server-checker

# Create and activate virtual environment (recommended)
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install the package
pip install -e .
```

## Verifying Installation

After installation, verify that the tool is working:

```bash
electrum-server-check --version
```

Or try checking a known Electrum server:

```bash
electrum-server-check electrum.blockstream.info
```

## Virtual Environment (Optional but Recommended)

It's recommended to use a virtual environment to avoid conflicts with other Python packages:

```bash
# Create virtual environment
python -m venv venv

# Activate virtual environment
# On Linux/macOS:
source venv/bin/activate

# On Windows:
venv\Scripts\activate

# Install the package
pip install electrum-server-checker
```

## Development Installation

If you plan to contribute to the project:

```bash
# Clone and install with development dependencies
git clone https://github.com/StevenGeller/electrum-server-checker.git
cd electrum-server-checker
python -m venv venv
source venv/bin/activate
pip install -e ".[dev]"
```

## Troubleshooting

### Common Issues

1. **SSL Warnings**
   ```
   Solution: These warnings are expected and can be safely ignored for testing purposes.
   ```

2. **Permission Errors**
   ```
   Solution: Use sudo or --user flag with pip:
   pip install --user electrum-server-checker
   ```

3. **Python Version Errors**
   ```
   Solution: Ensure you're using Python 3.7 or later:
   python --version
   ```

### Getting Help

If you encounter any issues:

1. Check the [GitHub Issues](https://github.com/StevenGeller/electrum-server-checker/issues)
2. Create a new issue if your problem isn't already reported
3. Join our community discussions