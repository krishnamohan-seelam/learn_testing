import unittest
import os
import tempfile
from remove_file  import rm

class TestRemoveFile(unittest.TestCase):

    tmpfilepath = os.path.join(tempfile.gettempdir(), "tmp-testfile")
    
    def setUp(self) -> None:
        with open(self.tmpfilepath,"w") as tempfile:
            tempfile.write("Delete this file")

        

    def test_ok(self):
        self.assertTrue(True)
    
    def test_rm(self):
        rm(self.tmpfilepath)
        self.assertFalse(os.path.isfile(self.tmpfilepath), "Failed to remove the file.")


if __name__ =='__main__':
    unittest.main()
