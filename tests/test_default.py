from testinfra.utils.ansible_runner import AnsibleRunner

testinfra_hosts = AnsibleRunner('.molecule/ansible_inventory').get_hosts('all')


def test_directories(File):
    present = [
        "/opt/prometheus/alertmanager",
        "/etc/prometheus/alertmanager",
        "/etc/prometheus/alertmanager/templates",
        "/var/lib/alertmanager",
        "/var/log/alertmanager"
    ]
    if present:
        for directory in present:
            d = File(directory)
            assert d.is_directory
            assert d.exists


def test_files(File):
    present = [
        "/etc/prometheus/alertmanager/alertmanager.yml",
        "/etc/systemd/system/alertmanager.service"
    ]
    if present:
        for file in present:
            f = File(file)
            assert f.exists
            assert f.is_file


def test_service(Service):
    present = [
        "alertmanager"
    ]
    if present:
        for service in present:
            s = Service(service)
            assert s.is_enabled
            assert s.is_running


def test_socket(Socket):
    present = [
        "tcp://127.0.0.1:9093"
    ]
    for socket in present:
        s = Socket(socket)
        assert s.is_listening
