class User:
    """
    Class that generates new intances of users
    """
    User_list=[] # Empty User list

    def __init__(self, username, password):
        # docstring removed for simplicityn
        self.username=username
        self.password=password

        