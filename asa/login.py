#Another version pf a user authentification page for login and sign ups
import time
users = {}
status = ''

def register():
    print("\nHi there, Please enter below your details for a sign up.\n")
    name = input("Enter your user name:\n")
    for i in range(1000):
        password = input("Enter your new password:\n")
        passwrd = input("Confirm your password by entering it again:\n")
        if passwrd != password:
            print("\nSorry! Your passwords didn't match, please try again.\n\n")
            time.sleep(2)
        if passwrd == password:
            break
    time.sleep(1)
    users[name] = password
    print("\nCongrats! user has been created.")
    logins = open("login.txt", "a")
    logins.write("\n" + name + " " + password)
    logins.close()
    


    
def login():
    print("Enter your details below:\n")
    name = input("User name: ")
    passwrd = input("Password: ")
    if name and passwrd in users:
        print("\nYou have successfully logged in. Enjoy!\n")
    else:
        print("\nSorry, your username or password was incorrect, please try again.\n")
    print(users)

    
def mainMenue():
    global status
    status = input("\nEnter y to login, n to sign up and q to quit:\n")
    if status.lower() == 'y':
        login()
    elif status.lower() == 'n':
        register()
    else:
        exit()


while status != 'q':
    status = mainMenue()
