#A program for user authentification after logging in
import time


for i in range(1000):
    users = {

}
    checking_account = input("\nType enter to continue or sign up to create an account.\n")
    if checking_account.lower() == "enter":
        user_name = input("Enter below your user name\n")
        if user_name == userName:
            print("\nYou are damn in.")
        else:
            print("\nOh sorry! You entered a wrong user name.")

    elif checking_account.lower() == "sign up":
        email = input("Enter a valid email below:\n")

        userName = input("\nEnter your user name below:\n")

        password = input("\nEnter a password of atleast 8 characters.\n")
        if len(password) < 8:
            cor_pass = input("\nPlease enter a password of atleast 8 characters:\n")
            if len(cor_pass) >= 8:
                print("Congs, you have set up a new password.")
                users[userName] = cor_pass
        
        users[userName] = password

    else:
        print("You entered a wrong entry, pliz try again: \n")
    time.sleep(2)