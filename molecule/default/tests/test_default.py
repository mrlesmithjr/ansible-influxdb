#!/usr/bin/env python3
# 2018-10-21 (cc) <paul4hough@gmail.com>

import os
import yaml

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


with open("../../defaults/main.yml", 'r') as stream:
    defaults = yaml.load(stream)


def test_package(host):
    assert host.package('influxdb').is_installed


def test_user(host):
    assert host.user('influxdb').name
    assert host.user('influxdbnot').name


def test_group(host):
    assert host.group('influxdb')

def test_service(host):
    svc = host.service('influxd')
    assert svc.is_running
    assert svc.is_enabled


def test_http_tcp_port(host):
    port = host.socket("tcp://0.0.0.0:%d" %
                       defaults['influxdb_http']['bind_port'])
    assert port.is_listening


def test_admin_tcp_port(host):
    port = host.socket("tcp://127.0.0.1:%d" %
                       defaults['influxdb_admin']['bind_port'])
    assert port.is_listening
