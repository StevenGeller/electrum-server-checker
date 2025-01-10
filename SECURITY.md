# Security Policy

## Supported Versions

| Version | Supported          |
| ------- | ------------------ |
| 0.1.x   | :white_check_mark: |

## Reporting a Vulnerability

We take the security of BitKey Electrum Server Checker seriously. If you discover a security vulnerability, please follow these steps:

1. Report the vulnerability through GitHub Issue.
2. Include:
   - A description of the vulnerability
   - Steps to reproduce
   - Potential impact
   - Any suggested fixes (if available)

You should receive a response within 48 hours. If the issue is confirmed, we will:

1. Acknowledge your contribution
2. Work on a fix
3. Release a security update
4. Credit you in the release notes (unless you prefer to remain anonymous)

## Security Considerations

### SSL/TLS Verification

The tool currently disables SSL certificate verification when checking HTTPS endpoints. This is done to support self-signed certificates commonly used in private Electrum servers. However, you should:

1. Be aware that this reduces security when checking HTTPS endpoints
2. Consider enabling certificate verification for your specific use case
3. Always verify server certificates when actually connecting your wallet

### Tor Support

When checking .onion addresses:

1. The tool will detect Tor addresses but won't attempt to connect
2. You need a properly configured Tor setup to actually use .onion addresses
3. Consider using Tor Browser or similar for additional privacy

### Best Practices

When using this tool:

1. Don't share server check results publicly if they're for private servers
2. Be cautious with error messages that might reveal internal infrastructure
3. Keep the tool updated to get the latest security fixes

## Security Updates

Security updates will be released as patch versions and announced:

1. Through GitHub security advisories
2. In the release notes
3. Via the changelog

## Dependency Security

We regularly monitor and update dependencies for security issues using:

1. GitHub's Dependabot
2. Regular manual reviews
3. Automated security scanning in CI/CD
