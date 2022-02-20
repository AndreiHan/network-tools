import subprocess


def speedtest():
    return subprocess.check_output(['speedtest-cli', '--simple'])


def speedtest_verbose():
    subprocess.call("speedtest-cli")
