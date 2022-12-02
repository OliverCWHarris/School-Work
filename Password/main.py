import time
import os

#os.chdir("C:\Users\olive\OneDrive - UTC Reading\Y12+13\Comp Sci\Password")



def admin_tools():
    admin_pass=input("Enter password>")
    if admin_pass=="cheese":
        print("1:print usernames\n2:print passwords\n3:ERASE ALL USERNAMES AND PASSWORDS")
        admin_choice=int(input(">"))

        if admin_choice==1:
            os.system("cls")
            f=open("usernames.txt","r")
            print(f.readlines())
            f.close()
            admin_tools()
        elif admin_choice==2:
            os.system("cls")
            f=open("passwords.txt","r")
            print(f.readlines())
            f.close()
            admin_tools()
        elif admin_choice==3:
            confirm=input("ARE YOU SURE? y/n\n>")
            if confirm=="y":
                f=open("usernames.txt","w")
                g=open("passwords.txt","w")
                f.write("")
                g.write("")
                f.close()
                g.close()
                quit()
        else:
            print("input not recognised")
            quit()


def del_acc():

    username=input("Enter username: ")
    password=input("Enter password: ")

    done1=False
    done2=False

    while done1==False:
        f=open("usernames.txt","rt")
        if username not in f:
            print("Error: user does not exist")
            f.close()
            username=input("Enter username: ")
            password=input("Enter password: ")

        else:
            with open("usernames.txt", "r") as file :
                filedata = file.read()

            filedata = filedata.replace(username,"")

            with open("usernames.txt", "w") as file:
                file.write(filedata)
            done1=True

    while done2==False:
        f=open("passwords.txt","rt")
        if password not in f:
            print("Error: user does not exist")
            f.close()
            username=input("Enter username: ")
            password=input("Enter password: ")

        else:
            with open("passwords.txt", "r") as file :
                filedata = file.read()

            filedata = filedata.replace(password,"")

            with open("passwords.txt", "w") as file:
                file.write(filedata)
            done2=True

    while done1==True and done2==True:
        out_menu()


def register():
    print("Welcome! Lets get you started with the system!")
    time.sleep(0.5)
    new_username=input("Enter your username: ")
    new_password=input("Enter your password: ")

    done1=False
    done2=False

    while done1==False:
        f=open("usernames.txt","rt")
        if new_username in f:
            print("Error: username already exists")
            f.close()

        else:
            f=open("usernames.txt","a")
            f.write("\n"+new_username)
            f.close()
            done1=True

    while done2==False:    
        f=open("passwords.txt","rt")
        if new_password in f:
            print("Error: please choose another password")
            f.close()

        else:
            f=open("passwords.txt","a")
            f.write("\n"+new_password)
            f.close()
            done2=True
    
    while done1==True and done2==True:
        out_menu()


def in_menu():
    print("""Welcome to the system!
    1:Logout
    2:Delete account""")
    time.sleep(0.5)
    in_menu_option=int(input("Enter option: "))

    if in_menu_option==1:
        out_menu()
    else:
        del_acc()


def login():
    logged_in=False
    while logged_in==False:
        username=input("Enter username: ")
        password=input("Enter password: ")

        f=open("usernames.txt","rt")
        if username in f:
            username_check=True
            f.close()
        else:
            print("Username not recognised")
            username_check=False
            f.close()
        
        f=open("passwords.txt", "rt")
        if password in f:
            password_check=True
            f.close()
        else:
            print("Password not recognised")
            password_check=False
            f.close()
        
        if (username_check==True) and (password_check==True):
            logged_in=True
            print("loggin successful!")
            in_menu()


def out_menu():
    print("1:Login\n2:Register\n3:Shutdown\n4:Admin tools")
    time.sleep(0.5)
    out_menu_option=int(input("Enter option: "))

    if out_menu_option==1:
        login()
    elif out_menu_option==2:
        register()
    elif out_menu_option==3:
        quit()
    elif out_menu_option==4:
        admin_tools()
    else:
        print("Input not recognised")


out_menu()