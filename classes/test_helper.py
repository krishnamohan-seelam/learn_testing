import unittest
from unittest import mock
from helper import Helper, Worker


class TestHelper(unittest.TestCase):

    @mock.patch('helper.os.getcwd')
    def test_get_path(self, _mock):
        _mock.return_value = '/unittest'
        test_value = Helper('helper').get_path()
        expected_value = '/unittest/helper'
        self.assertEqual(test_value, expected_value)

    @mock.patch('helper.Helper', autospec=True)
    def test_work(self, mock_helper):
        mock_helper.return_value.get_path.return_value = "/unittest/db"
        expected_value = '/unittest/db'
        worker = Worker()
        self.assertEqual(worker.work(), expected_value)
        mock_helper.assert_called_once_with('db')


if __name__ == '__main__':
    unittest.main()
