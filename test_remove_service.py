from service import RemovalService,UploadService
from unittest import mock
import unittest


class TestRemovalService(unittest.TestCase):

    def setUp(self) -> None:
        self.filename ="tempfile"
    
    @mock.patch('service.os.path')
    @mock.patch('service.os')
    def test_remove(self, mock_os, mock_os_path):
        rmservice =RemovalService()
        mock_os_path.isfile.return_value = True
        rmservice.rm(self.filename)
        mock_os.remove.assert_called_with(self.filename)

# Patch particular method
class TestUploadService(unittest.TestCase):

    def setUp(self) -> None:
        self.filename ='tempfile'
       
    @mock.patch.object(RemovalService,'rm')
    def test_upload(self,mock_rm):
        removal_srv = RemovalService()
        upload_srv = UploadService(removal_srv)
        upload_srv.upload(self.filename)
        mock_rm.assert_called_with(self.filename)
        removal_srv.rm.assert_called_with(self.filename)

# OPTION 2: CREATING MOCK INSTANCES    

class TestUploadService2(unittest.TestCase):

    def setUp(self) -> None:
        self.filename ='tempfile'
       
    def test_upload2(self):
        removal_srv = mock.create_autospec(RemovalService)
        upload_srv = UploadService(removal_srv)
        upload_srv.upload(self.filename)
        removal_srv.rm.assert_called_with(self.filename)    


if __name__ == '__main__':
    unittest.main()

