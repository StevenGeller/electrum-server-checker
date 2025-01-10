"""
BitKey Electrum Server Checker
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

A command-line tool to check if an Electrum server is compatible with BitKey
and show all available connection methods.

Basic usage:

    >>> from electrum_server_checker import check_server
    >>> results = check_server('electrum.blockstream.info')
    >>> results['ssl']  # Check if compatible with BitKey
    True

See https://github.com/StevenGeller/electrum-server-checker for more information.
"""

from .checker import check_server, check_tcp_port, check_http_endpoint, is_onion_address

__version__ = '0.1.0'
__author__ = 'Steven Geller'
__license__ = 'MIT'

__all__ = ['check_server', 'check_tcp_port', 'check_http_endpoint', 'is_onion_address']