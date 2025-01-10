# Usage Guide

Learn how to use the BitKey Electrum Server Checker effectively.

## Basic Usage

The basic command syntax is:

```bash
electrum-server-check <server-address>
```

Where `<server-address>` can be:
- Domain name (e.g., `electrum.blockstream.info`)
- IP address (e.g., `192.168.1.100`)
- Onion address (e.g., `abc123.onion`)

## Examples

### 1. Check a Public Server

```bash
electrum-server-check electrum.blockstream.info
```

Example output:
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

### 2. Check a Private Server

```bash
electrum-server-check 192.168.1.100
```

### 3. Check a Tor Hidden Service

```bash
electrum-server-check abc123.onion
```

## Understanding the Output

The tool provides several sections in its output:

1. **Progress Information**
   ```
   Checking connectivity for example.com...
   [*] Checking TCP port 50001...
   [*] Checking SSL port 50002...
   [*] Checking HTTP...
   [*] Checking HTTPS...
   ```

2. **BitKey Compatibility**
   ```
   BitKey Compatibility:
   ✅ This server is COMPATIBLE with BitKey (SSL port 50002 is available)
   Connection string for BitKey: ssl://example.com:50002
   ```
   Or for incompatible servers:
   ```
   ❌ This server is NOT COMPATIBLE with BitKey (requires SSL port 50002)
   ```

3. **Available Connection Methods**
   ```
   All Available Connection Methods:
   • TCP     - tcp://example.com:50001
   • SSL/TLS - ssl://example.com:50002
   • HTTP    - http://example.com:50001
   • HTTPS   - https://example.com:50002
   ```

## Connection Types

The tool checks for several connection methods:

1. **TCP (Port 50001)**
   - Basic unencrypted connection
   - Not recommended for BitKey

2. **SSL/TLS (Port 50002)**
   - Encrypted connection
   - Required for BitKey
   - Most secure option

3. **HTTP (Port 50001)**
   - Web-based unencrypted connection
   - Not recommended for BitKey

4. **HTTPS (Port 50002)**
   - Web-based encrypted connection
   - Alternative secure option

5. **Onion (Tor)**
   - Special handling for .onion addresses
   - Requires Tor configuration

## Error Messages

Common error messages and their meanings:

1. **No Connection Methods Available**
   ```
   ❌ No connection methods available or server is not responding
   ```
   - Server might be offline
   - Incorrect address
   - Firewall blocking access

2. **Onion Address Detection**
   ```
   [*] Detected .onion address: abc123.onion
   [!] To connect to .onion addresses, make sure you have Tor configured
   ```
   - Server is a Tor hidden service
   - Requires Tor configuration to connect

## Tips

1. Always use SSL/TLS (port 50002) for BitKey connections
2. Verify server certificates when possible
3. Use Tor for additional privacy when needed
4. Keep the tool updated for security fixes

## Getting Help

If you encounter issues:

1. Check the [GitHub Issues](https://github.com/StevenGeller/electrum-server-checker/issues)
2. Join the community discussions
3. Read the [Security Guidelines](../bitkey/security.md)