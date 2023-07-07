import unittest
from unittest import mock
from work import work_on


class DummyPath(object):
    @staticmethod
    def cwd(*args, **kwargs):
        return 'temp'


class TestWork(unittest.TestCase):

    @mock.patch('work.Path')
    def test_work_on_called(self, mock_path):
        mock_path.return_value = DummyPath()
        val = work_on()
        self.assertEqual(val, 'temp')

    @mock.patch('work.Path')
    def test_work_on_called_cwd(self, mock_path):
        mock_path.return_value.cwd.return_value = DummyPath.cwd()
        val = work_on()
        self.assertEqual(val, 'temp')


if __name__ == "__main__":
    unittest.main()
