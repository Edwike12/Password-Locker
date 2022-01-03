from User import User, Credentials

def  create_new_user(username,password):
    '''
    function to create new user with username and password
    '''
    new_user=User(username,password)
    return new_user

    def save_user(User):
        '''
        its a function to save user
        '''
        User.save_user()

    def login_user(username,password):
        """
        function that checks whether a user exist and then login the user in.
        """
        check_user = Credentials.verify_user(username,password)
        return check_user

def create_new_credentials(account,username,password):
    '''
    a function that creates a new credentials with account,username and password
    '''
    new_credentials=Credentials(account,username,password)
    return new_credentials

    def save_credentials(Credentials):
        '''
        its a function to save credentials
        '''
        Credentials.save_credentials() 

    def display_accounts_credentials():
        """
        Function that shows all the saved credentials.
        """
        return Credentials.display_credentials()

    def delete_credentials(Credentials):
        '''
        its a function to delete credentials
        '''
        Credentials.delete_credentials() 

        def check_credentials(Credentials):
            '''
            its a function that check if a credentials exists with that account name and return true or false
            '''
            return Credentials.check_credentials_exist(account)

'''
creating an opening display page
'''

def passwordlocker():
    print("Hello, welcome to passwordlocker", "To proceed enter:","create new account 'CA'","log in account 'lG'","Exit",sep="\n\n")
    short_code=input("").lower().strip()
    if short_code=="CA":
        print("Sign Up")
        print('*' *20)
        username=input("User_name: ")
        while True:
            print(" TP - To type your own pasword: ")
            password_Choice = input().lower().strip()
            if password_Choice == 'TP':
                password = input("Enter Password\n")
                break
            else:
                print("Invalid password please try again")
        save_user:(create_new_user(username,password))
        print("*"*85)
        print(f"Hello {username}, Your account has been created succesfully! Your password is: {password}")
        print("*"*85)