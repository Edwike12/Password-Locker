import random
import string
class User:
    """
    Class that generates new intances of users
    """
    User_list=[] # Empty User list

    def __init__(self, username, password):
        '''
        __init__ method that helps us define properties for our objects.

        Args:
            username: new_user username.
            password: new_user password.
            
            '''
        self.username=username
        self.password=password

    def save_user(self):


        '''
        save_uer method saves user objects into user_list
        '''

        User.User_list.append(self)


    def delete_user(self):
        '''
        delete_account method deletes a  saved account from the list
        '''
        User.User_list.remove(self)

class Credentials():
    """
    Create credentials class to help create new objects of credentials
    """
    credentials_list = []

    def __init__(self, account, username, password):
        '''
        __init__ method that helps us define properties for our objects.

        Args:
            account: new_user  account.
            username: new_user username.
            password: new_user password.
            
            '''
        self.account=account    
        self.username=username
        self.password=password


        def save_credentials(self):
            '''
            method to store new credentials
            '''
        Credentials.credentials_list.append(self)

        def delete_credentials_(self):
            '''
            method that deletes an account credentials from the credentials list
            '''
        Credentials.credentials_list.append(self)

        def search_credentials_(cls,account):
            '''
            method that searches an account and returns the credentials that matches that is the password and username
            '''
            for credential in cls.credentials_list:
                if credential.account == account:
                    return credential

        def check_credentials_exist(cls,account):
            '''
            method that searches an account and its credentials if they exist and returns true or false
            '''
            for credential in cls.credentials_list:
                if credential.account == account:
                    return True
                    return False      

        def display_credentials(cls):
            """
            Method that returns all items in the credentials list
            """
            return cls.credentials_list                  


        

        

        