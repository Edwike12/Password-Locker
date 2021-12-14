import unittest # Importing the unittest module
from User import User  # Importing the user class
from User import Credentials

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

        def test_init(self):
                """
                test_init test case to test if the object is initialized properly
                """
                self.assertEqual(self.new_user.username,"Edwike")
                self.assertEqual(self.new_user.password,"Edu@123")

        def test_save_user(self):
                """
                test case to test if a new user instance has been saved into the User list
                """
                self.new_user.save_user()
                self.assertEqual(len(User.User_list),1)

                    
class TestCredentials(unittest.TestCase):

        '''
        Test class that defines test cases for the user class behaviours.

        Args:
                unittest.TestCase: TestCase class that helps in creating test cases
        '''
        def setUp(self):
                '''
                Set up method to run before each test cases.
                '''
                self.new_credential = Credentials("Facebook", "Invioleta", "Invi@456") # create user object  

        def test_init(self):
                """
                test_init test case to test if the object is initialized properly
                """
                self.assertEqual(self.new_credential.account,"Facebook")
                self.assertEqual(self.new_credential.username,"Invioleta")
                self.assertEqual(self.new_credential.password,"Invi@456")

        def test_save_credentials_(self):
                '''
                test_save_credentials test case to test if the accounts object is saved into
                the credentials list
                '''
                self.new_credentials.save_credentials() # saving the new account
                self.assertEqual(len(Credentials.credentials_list),1)


        def test_delete_credentials_(self):
                '''
                test_delete_credentials to test if we can remove a credentials from our credentials list
                '''
                self.new_credential.save_credentials()
                test_credential = Credentials("Facebook","Invioleta","Invi@456")
                test_credential.save_credentialsls()

                self.new_credential.delete_credentials()
                self.assertEqual(len(Credentials.credentials_list),1)

        def tearDown(self):
                '''
                tearDown method that does clean up after each test case has run.
                '''
                Credentials.credential_list = []

        def test_save_multiple_accounts(self):
                
                '''
                test_save_multiple_accounts to check if we can save multiple account
                objects to our credential list
                '''
                self.new_credentials.save_credentials()
                test_credentials = Credentials("Facebook", "Invioleta", "Invi@456") # new contact
                test_credentials.save_credentials()
                self.assertEqual(len(Credentials.credentials_list),2)

        def test_credentials_exist(self):
                '''
                test_credentials_exist is a test to check if the credentials exist to return a true or false
                '''
                self.new_credential.save_credentials()
                test_credential = Credentials("Facebook","Invioleta","Invi@456")
                test_credential.save_credentialsls()

                credentials_is_found = Credentials.check_credentials_exist("Facebook")
                self.assertTrue(credentials_is_found)




               

       

if __name__ == '__main__':

    unittest.main()   