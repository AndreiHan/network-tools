import pytest
import os

import tools.fileManager


class TestClass:
    @classmethod
    def setup_class(cls):
        try:
            os.rmdir("output")
            os.rmdir("input")
        except OSError:
            pass
        else:
            raise

    @classmethod
    def teardown_class(cls):
        try:
            os.rmdir("output")
            os.rmdir("input")
        except OSError:
            pass
        else:
            raise

    @pytest.fixture(autouse=True)
    def cleanup_files(self):
        try:
            os.rmdir("output")
            os.rmdir("input")
        except OSError:
            pass
        else:
            raise

    files = ["input/ssh-credentials.txt", "input", "output", "output/status.json"]

    @pytest.mark.parametrize("path", files)
    def test_files(self, path):

        tools.fileManager.init_files()  # function to test

        try:
            assert os.path.exists(path)  # assert the presence of the path
        except OSError:
            assert False  # fail is the path does not exist
