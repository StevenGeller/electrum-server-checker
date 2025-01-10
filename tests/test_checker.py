import pytest
from unittest.mock import patch, MagicMock
from electrum_server_checker import check_server, is_onion_address, check_tcp_port, check_http_endpoint

def test_is_onion_address():
    assert is_onion_address("abc123.onion") == True
    assert is_onion_address("example.com") == False
    assert is_onion_address("test.onion.com") == False
    assert is_onion_address("") == False
    assert is_onion_address("onion") == False
    assert is_onion_address(".onion") == True

@patch('socket.create_connection')
def test_check_tcp_port_success(mock_connection):
    mock_socket = MagicMock()
    mock_connection.return_value = mock_socket
    
    assert check_tcp_port("example.com", 50002) == True
    mock_connection.assert_called_once_with(("example.com", 50002), timeout=5)
    mock_socket.close.assert_called_once()

@patch('socket.create_connection')
def test_check_tcp_port_failure(mock_connection):
    mock_connection.side_effect = socket.timeout()
    assert check_tcp_port("invalid.example", 50002) == False

    mock_connection.side_effect = socket.error()
    assert check_tcp_port("invalid.example", 50002) == False

@patch('requests.get')
def test_check_http_endpoint_success(mock_get):
    mock_response = MagicMock()
    mock_response.status_code = 200
    mock_get.return_value = mock_response
    
    assert check_http_endpoint("http://example.com") == True
    mock_get.assert_called_once_with("http://example.com", timeout=5, verify=False)

@patch('requests.get')
def test_check_http_endpoint_failure(mock_get):
    # Test non-200 response
    mock_response = MagicMock()
    mock_response.status_code = 404
    mock_get.return_value = mock_response
    assert check_http_endpoint("http://example.com") == False
    
    # Test connection error
    mock_get.side_effect = requests.exceptions.RequestException()
    assert check_http_endpoint("http://invalid.example") == False

def test_check_server_blockstream():
    results = check_server("electrum.blockstream.info")
    assert isinstance(results, dict)
    assert all(key in results for key in ['tcp', 'ssl', 'http', 'https', 'onion'])
    assert results["ssl"] == True  # Should support SSL for BitKey
    assert results["onion"] == False

def test_check_server_onion():
    results = check_server("abc123.onion")
    assert results["onion"] == True
    assert results["ssl"] == False
    assert results["tcp"] == False
    assert results["http"] == False
    assert results["https"] == False

def test_check_server_invalid():
    results = check_server("invalid.example.notreal")
    assert results["ssl"] == False
    assert results["tcp"] == False
    assert results["http"] == False
    assert results["https"] == False
    assert results["onion"] == False

def test_check_server_empty():
    with pytest.raises(Exception):
        check_server("")

def test_check_server_none():
    with pytest.raises(Exception):
        check_server(None)

@pytest.mark.parametrize("address,expected", [
    ("example.com", "example.com"),
    ("http://example.com", "example.com"),
    ("https://example.com", "example.com"),
    ("abc123.onion", "abc123.onion"),
])
def test_check_server_address_parsing(address, expected):
    results = check_server(address)
    assert results["address"] == expected