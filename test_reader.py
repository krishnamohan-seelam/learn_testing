import unittest
from unittest.mock import Mock
from reader import read_file_contents

VALS = ["Hello \n"]


class TestReader(unittest.TestCase):

    @unittest.mock.patch('reader.open')
    def test_reader(self, mock_ctx):
        mock_ctx.return_value.__enter__.return_value = (val for val in VALS)
        test_vals = read_file_contents("hello.txt")
        self.assertEqual(VALS, test_vals)


if __name__ == '__main__':
    unittest.main()
