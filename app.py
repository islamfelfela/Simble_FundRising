#! /usr/bin/python3

# import libin_place
import validate


print("Welcome To FundRais....")
print("choose Option")


# Vars
# current_user
# status
# flag


# current_user
# status

# Register User
def regiter_user(fname, lname, email, passwd, mobil):
    with open('users.txt','a') as f:
        f.write(fname+':'+lname+':'+email+':'+passwd+':'+mobil+"\n")
        print("*******  User Registered Successfully  *********")
        

# User Authentication
def user_auth(email, passwd):
    with open('users.txt', 'r') as searchfile:
        for line in searchfile:
            if email in line:
                l = line.split(":")
                return l[:-1]


# create new Project
def create_new_project():
    title = input("Enter Project Title:")
    while not validate.name_validate(title):
        title = input("Enter Valid Title :")
    details = input("Enter Project details:")
    target = input("Enter your target:")
    while not validate.num_validate(target):
        target = input("Enter Valid Target (Only Nums):")
    date = input("Enter project date:")
    while not validate.date_validate(date):
        date = input("Enter Valid Date (dd/mm/yyyy):")
    owner = current_user
    with open('projects.txt','a') as f:
        f.write(owner+":"+title+':'+details+':'+target+':'+date+"\n")
        print("*******  Project Created Successfully  *********")


# View Project

def view_project(title):
    with open('projects.txt', 'r') as searchfile:
        for line in searchfile:
            if title in line:
                l = line.rstrip().split(":")
                return l[1:]


# Edit Project 
# def edite_project(title):
    # with in_place.InPlace('data.txt') as file:
    #     for line in file:
    #         line = line.replace('test', 'testZ')
    #         file.write(line)



# Remove Project
def remove_project(title):
   with open("projects.txt", "r") as f:
        lines = f.readlines()
   with open("projects.txt", "w") as f:
        for line in lines:
            if line.split(":")[1] != title:
                f.write(line)


# Project Crud operations  -> create, view, edit, delete, search
def crud():
    while True: 
        opt = int(input("1- Create Project\n2- View Project\n3- Edit Project\n4- Delete Project\n5- Logout\n"))
        if opt == 1:
            print("*****  Creating new Project ***")
            create_new_project()
            crud()
        elif opt == 2:
            print("*****  View Project ***")
            title = input("Enter Project title ")
            if title:
                print("*********************************")
                print(view_project(title))
                print("*********************************")
            else:
                print("***** Project Name Invalid ***")
        elif opt == 3:
            print("*****  Edit  Project ***")
            title = input("Enter Project title: ")
            if title:
                print(edite_project(title))
            else:
                print("***** Project Name Invalid ***")
        elif opt == 4:
            print("*****  Delete Project ***")
            title = input("Enter Project title")
            remove_project(title)
        elif opt == 5:
            current_user = ""
            break
        else:
            print("Wrong Input.. ")
            crud()
    

# Entry
def main():
    while True:
        ch = int(input("1- Register\n2- Login\n3- Exite\n"))
        if ch == 1:
            print("Register Mode: ")
            #code...
            fname = input("Enter First Name:")
            while not validate.name_validate(fname):
                fname = input("Enter Valid First Name:")
            lname = input("Enter Last Name:")
            while not validate.name_validate(lname):
                lname = input("Enter Valid Last Name:")
            email = input("Enter Email:")
            while not validate.email_validate(email):
                email = input("Enter Valid Email:")
            passwd = input("Enter Password:")
            while not validate.password_validate(passwd):
                passwd = input("Enter Valid Password:")
            passwd_confirm = input("Confirm Password:")
            while passwd != passwd_confirm:
                passwd = input("Not Matching, Enter Password:")
                passwd_confirm = input("Confirm Password:")
            mobil = input("Enter Mobile num:")
            while not validate.mobil_validate(mobil):
                mobil = input("Enter Valid Mobile num:")
            regiter_user(fname, lname, email, passwd, mobil)
            main()
        elif ch == 2:
            print("Loging Mode: ")
            #code...
            email = input("Enter Email:")
            passwd = input("Enter passwd:")
            user_creds = user_auth(email, passwd)
            # Shoeing Crud Menue
            if user_creds:
                global current_user
                current_user = user_creds[0]
                print("\tLogged In User : "+ current_user+"\n")
                crud()
            else:
                print("Auth Faild , Plaease Enter valid Data..\n")
            
        elif ch == 3:
            break
        else:
            print("Wrong Input.. ")
            main()


main()






