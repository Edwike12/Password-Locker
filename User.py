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
        User.user_list.remove(self)

class Credentials():
    """
    Create credentials class to help create new objects of credentials
    """
    credentials_list = []

        