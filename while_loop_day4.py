import re
def prog1():
    while True:
        enter_username=input("enter the username: ")
        match=re.search(r"^[p|P]\d{6}",enter_username)
        if match:
            print("You can login.")
            break
        else:
            print("entered username is invalid, please enter valid name.")
prog1()

