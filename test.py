import unittest # Importing the unittest module
from User import User  # Importing the contact class

class TestUser(unittest.TestCase):

    '''
    Test class that defines test cases for the user class behaviours.

    Args:
        unittest.TestCase: TestCase class that helps in creating test cases
    '''
def setUp(self):
        '''
        Set up method to run before each test cases.
        '''

        self.new_user = User("Edwike","Edu@123") # create user object

def tearDown(self):
        '''
        tearDown method that does clean up after each test case has run.
        '''   
        User.User_list=[]    

def test_init(self):
        """
        test case to chek if the object has been initialized correctly
        """
        self.assertEqual(self.new_user.username,'Edwike')
        self.assertEqual(self.new_user.password,'Edu@123')

if __name__ == '__main__':
    unittest.main()        
