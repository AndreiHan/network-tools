import pytest

from tools.ping import ping
from tools.ping import ping_multiple_dictionary

server_list_true_local = ["localhost", "0:0:0:0:0:0:0:1", "127.0.0.1"]
server_list_true_dns = ["1.1.1.1", "8.8.8.8", "1.0.0.1", "8.8.4.4"]
server_list_true_all = [server_list_true_local, server_list_true_dns]
server_list_false = ["0:0:0:0:0:0:0:2", "192.168.2.2", "test", "12345", "123.123.123.123.123", "0", "1"]


@pytest.fixture()
def list_true():
    'list_true_local.txt'
    open(server_list_true_local.txt, 'r+')


# Test ping()

@pytest.mark.parametrize("server", server_list_true_local)
def test_ping_true(server):
    assert ping(server) == 1


@pytest.mark.parametrize("server", server_list_true_dns)
def test_ping_true(server):
    assert ping(server) == 1


@pytest.mark.parametrize("server", server_list_false)
def test_ping_false(server):
    assert ping(server) == 0


def test_ping_wrong_format_low():
    host = "1"
    assert ping(host) == 0


def test_ping_wrong_format_high():
    host = "123.123.123.123.123.123.123.123.123"
    assert ping(host) == 0


def test_ping_port():
    host = "http://192.168.1.120:8989/"
    assert ping(host) == 0


#### Test ping_multiple_dictionary()

@pytest.mark.parametrize("server_list", server_list_true_all)
def test_ping_multiple_dictionary_true(server_list):
    servers_status = dict.fromkeys(server_list, 1)
    assert ping_multiple_dictionary(server_list) == servers_status


@pytest.mark.parametrize("server_list", server_list_true_all)
def test_ping_multiple_dictionary_true_format(server_list):
    servers_status = dict.fromkeys(server_list, 0)
    assert ping_multiple_dictionary(server_list) != servers_status


@pytest.mark.parametrize("server", server_list_true_local)
def test_ping_multiple_dictionary_true_low(server):
    server_list = [server]
    servers_status = dict.fromkeys(server_list, 1)
    assert ping_multiple_dictionary(server_list) == servers_status


@pytest.mark.parametrize("server_list", server_list_true_all)
def test_ping_multiple_dictionary_true_high(server_list):
    server_list_local = server_list + server_list + server_list
    servers_status = dict.fromkeys(server_list_local, 1)
    assert ping_multiple_dictionary(server_list_local) == servers_status


def test_ping_multiple_dictionary_false():
    servers_status = dict.fromkeys(server_list_false, 0)
    assert ping_multiple_dictionary(server_list_false) == servers_status


def test_ping_multiple_dictionary_false_format():
    servers_status = dict.fromkeys(server_list_false, 1)
    assert ping_multiple_dictionary(server_list_false) != servers_status


@pytest.mark.parametrize("server", server_list_false)
def test_ping_multiple_dictionary_false_low(server):
    server_list = [server]
    servers_status = dict.fromkeys(server_list, 0)
    assert ping_multiple_dictionary(server_list) == servers_status


def test_ping_multiple_dictionary_false_high():
    server_list = server_list_false + server_list_false + server_list_false
    servers_status = dict.fromkeys(server_list, 0)
    assert ping_multiple_dictionary(server_list) == servers_status
