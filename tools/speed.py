import subprocess


def speedtest_silent():
    return subprocess.call("speedtest-cli --simple")


def speedtest_verbose():
    subprocess.call("speedtest-cli --simple")
