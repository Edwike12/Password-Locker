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

    def save_User(self):
        """
        A method that saves a new user instace into the user list
        """
        User.User_list.append(self)

        