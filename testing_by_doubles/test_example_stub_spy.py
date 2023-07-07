import unittest
from unittest import mock


def read_file(file):
    print("started reading the file")
    return file.read()


class TestReadFile(unittest.TestCase):
    def test_using_dummy(self):
        file = mock.Mock()
        read_file(file)

    def test_using_stub(self):
        file = mock.Mock()
        file.read.return_value = "Hello World"
        test_result = read_file(file)
        self.assertEqual(test_result, "Hello World")

    def test_using_spy(self):
        file = mock.Mock()
        file.return_value = "Hello World"
        test_result = read_file(file)
        self.assertEqual(1, file.read.call_count)


if __name__ == "__main__":
    unittest.main()
