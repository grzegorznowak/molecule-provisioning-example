import os
import pytest

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')

@pytest.mark.parametrize('port', [
    '80'
])
def test_ports(host, port):
    assert host.socket("tcp://0.0.0.0:{}".format(port)).is_listening


@pytest.mark.parametrize('port', [
    '80'
])
def test_up(host, port):

    cmd = host.run(
        'curl --write-out %{http_code} --silent ' +
        '--output /dev/null http://{}:{}/pinfo.php'.format('0.0.0.0', port))

    assert cmd.stdout == '200'


def test_composer_installed(host):
    cmd = host.run("COMPOSER_ALLOW_SUPERUSER=1 composer --version")
    assert cmd.stderr == ''
    assert 'Composer' in cmd.stdout


