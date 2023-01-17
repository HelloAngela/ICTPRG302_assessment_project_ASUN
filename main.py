# Written by Angela Sun, 17/01/2023 for ICTPRG302 project assessment
# The purpose of this program is to provide a sign-in and registration service for the user,
# and keeping the record for the administrator.


# Importing relevant libraries
import pandas as pd
import time
import sys
import string
import random

# Welcome message
print('Welcome to Gelos Enterprise! What would you like to do today?')

# Loading account information, converted accounts.txt to a dictionary
with open("accounts.txt") as f:
    login_db = pd.read_csv(f, delimiter=" ", header=None)
    login_db.set_index(0, inplace=True)
    db2 = login_db.to_dict()[1]


# Converting dictionary object back to txt and save after a registration process is completed
def update_db():
    df = pd.DataFrame([db2]).T
    df.to_csv("accounts.txt", header=False, sep=" ")


# Random password generator with a password length of 10 characters
def pwd_gen():
    pw_len = 10
    char_list = string.ascii_letters + string.digits + string.punctuation
    global gen_pw
    gen_pw = "".join(random.choice(char_list) for i in range(pw_len))
    return gen_pw


# Main menu, asking user to select a task
def task_selection():
    task = str.upper(input("Enter letters A-D to access the corresponding function:\n "
                     "A. Login \n B. Register for a new account\n"
                     " C. View accounts (Administrator only) \n D. Exit \n"))
    if task == 'A':
        login()
    elif task == 'B':
        new_acc()
    elif task == 'C':
        view_acct()
    elif task == 'D':
        exit_program()
    else:
        print ("No function associated with this input, please enter letters A~D only")


# Existing user login
def login():
    print("Login")
    uid = str(input("Please enter your user name:\n"))
    pw = str(input("Please provide your password:\n"))
    if db2.get(uid) == pw:
        print("Thank you. You have successfully logged into the system.")
    else:
        print("Sorry,login details did not match, please double check your input")
        t = int(input("Enter 1 to try again, 2 to go back to the main menu, or 3 to exit the program\n"))
        if t == 1:
            login()
        elif t == 2:
            task_selection()
        elif t == 3:
            exit_program()
        else:
            print("No function associated with this input, please enter numbers 1~3 only")


# Registering for a new account, new login information saved to accounts.txt
def new_acc():
    print("Registering for a new account")
    new_id = str(input("Please enter a new user name: \n"))
    dupl_id = new_id in db2

    if dupl_id == True:
        print("This user name has already been used, please select a new one")
        new_acc()
    else:
        set_pw = int(input("How would you like to set your password? "
                           "Press 1 to set it yourself, or 2 for the program to generate one for you:\n"))
        if set_pw == 1:
            new_pw = str(input("Please enter a password,\n"
                           "it may contain alphabets, numbers and special symbols such as _, ~ and !\n"))
            db2[new_id] = new_pw
            update_db()
            print("Password saved.")
        elif set_pw == 2:
            pwd_gen()
            print("Your new password is:")
            print(gen_pw)
            db2[new_id] = gen_pw
            update_db()
            print("Password saved.")
        else:
            print("No function associated with this input, please enter numbers 1~2 only")
            new_acc()


# View account information from the accounts.txt file
def view_acct():
    print("Displaying user account information....\n")
    with open("accounts.txt") as f:
        for line in f:
            print(line.strip())
    print("\n Returning to the main menu...\n")
    task_selection()


# Exiting program after 2 seconds
def exit_program():
    print("Exiting program in 2 seconds...")
    time.sleep(2)
    sys.exit()


task_selection()