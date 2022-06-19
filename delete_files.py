# python program to delete contents of given directory
import os
import shutil
import unittest


DIR_TO_DELETE = "test"


# function to delete directory content
def delete_content(path:  str)->bool:
    
    status = True    
    print()

    # move to the target directory
    print(f"Switch to target directory {path}")
    current_path = os.getcwd()
    os.chdir(path)

    # get the directory content
    directory_items = os.listdir()

    # delete the directory content
    for item in directory_items:
        
        
        try:
            if os.path.isfile(item):
                print(f"Deleting the file : {item}")
                os.remove(item)
            elif os.path.isdir(item):
                print(f"Deleting the directory : {item}")
                shutil.rmtree(item)
            else:
                raise
        except:
            print(f"Could not delete {item}")
            status = False

    # revert to the current directory
    print(f"Revert control back to {current_path}")
    os.chdir(current_path)
    
    return status   


class TestDelete(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        
        cls.path = DIR_TO_DELETE

    def is_a_dir(self):
        if os.path.isdir(self.path):    
            return True
        return False
    
    def is_empty(self):
        if not os.listdir(self.path):
            return True
        return False

    def test_1_is_not_a_directory(self):
        self.assertTrue(self.is_a_dir(), msg=f"{self.path} is not a directory")
    
    def test_2_is_empty_directory(self):
        self.assertFalse(self.is_empty(), msg=f"{self.path} is an empty directory")

    def test_3_delete_content(self):
        self.assertTrue(delete_content(self.path), msg=f"{self.path} content deletion failed")

    def test_4_is_dir_empty(self):
        self.assertTrue(self.is_empty, msg=f"{self.path} directory is not cleared")
    
    @classmethod
    def tearDownClass(cls):
        del cls.path



if __name__ == '__main__':
    os.system("touch test/text.txt")    
    unittest.main(verbosity=2, failfast=True)

