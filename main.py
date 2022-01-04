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

    def find_credential(account):
        """
        Function that finds a Credentials by an account name and returns the Credentials that belong to that account
        """
        return Credentials.find_credential(account)

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
    elif short_code=="LG":
        print("*"*50)
        print("Enter your User name and your Password to log in:")
        print('*' * 50)
        username = input("User name: ")
        password = input("password: ")
        login_user:(create_new_user(username,password))
        if login_user == "login":
            print(f"Hello {username}.Welcome To PassWord Locker Manager")  
            print('\n')
    while True:
        print("Use these short codes:\n CC - Create a new credential \n DC - Display Credentials \n FC - Find a credential \n GP - Generate A randomn password \n D - Delete credential \n EX - Exit the application \n")
        short_code = input().lower().strip()
        if short_code == "cc":
            print("Create New Credential")
            print("."*20)
            print("Account name ....")
            account = input().lower()
            print("Your Account username")
            userName = input()
            while True:
                print(" TP - To type your own pasword if you already have an account")
                password_Choice = input().lower().strip()
                if password_Choice == 'TP':
                    password = input("Enter Your Own Password\n")
                    break
                else:
                    print("Invalid password please try again")
            save_credentials:(create_new_credentials(account,userName,password))
            print('\n')
            print(f"Account Credential for: {account} - UserName: {userName} - Password:{password} created succesfully")
            print('\n')  
        else:
                print("You don't have any credentials saved yet..........")
        elif short_code=="FC":
        print("Enter the Account Name you want to search for")
        search_name = input().lower()
        if find_credential(search_name):
                search_credential = find_credential(search_name)
                print(f"Account Name : {search_credential.account}")
                print('-' * 50)
                print(f"User Name: {search_credential.userName} Password :{search_credential.password}")
                print('-' * 50)
        else:
                print("That Credentials does not exist")
                print('\n')  
        elif short_code=="d":
        print("Enter the account name of the Credentials you want to delete")
        search_name = input().lower()
        if find_credential(search_name):
                search_credential = find_credential(search_name)
                print("_"*50)
                search_credential.delete_credentials()
                print('\n')
                print(f"Your stored credentials for : {search_credential.account} successfully deleted!!!")
                print('\n')
        else:
                print("That Credential you want to delete does not exist in your store yet")

        elif short_code == 'ex':
        print("Thanks for using passwords store manager.. See you next time!")
        break
    else:
        print("Wrong entry... Check your entry again and let it match those in the menu")
    else:
    print("Please enter a valid input to continue")


if __name__ == '__main__':
    passwordlocker()    
    