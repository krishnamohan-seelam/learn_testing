import unittest
from unittest import mock 
from remove_file  import rm, rm2

class TestRemoveFile(unittest.TestCase):

    def setUp(self) -> None:
        self.tmpfile='tempfile'

    @mock.patch('remove_file.os')
    def test_rm(self, mock_os):
       rm(self.tmpfile)
       mock_os.remove.assert_called_with(self.tmpfile)

    @mock.patch('remove_file.os.path')
    @mock.patch('remove_file.os')
    def test_rm2(self, mock_os, mock_os_path):
       mock_os_path.isfile.return_value =True
       rm2(self.tmpfile)
       mock_os.remove.assert_called_with(self.tmpfile)

    @mock.patch('remove_file.os.path')
    @mock.patch('remove_file.os')
    def test_rm2fail(self, mock_os, mock_os_path):
       mock_os_path.isfile.return_value =False
       rm2(self.tmpfile)
       self.assertFalse(mock_os.remove.called)

if __name__ =='__main__':
    unittest.main()
