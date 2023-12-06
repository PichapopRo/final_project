# import database module
import database
import random
import time
import csv

# define a function called initializing
my_DB = database.DB()


def initializing():
    persons_list = database.read_csv('persons.csv')
    login_list = database.read_csv('login.csv')
    project_list = database.read_csv('project.csv')
    adviser_request_list = database.read_csv('adviser_request.csv')
    member_request_list = database.read_csv('member_request.csv')
    persons_table = database.Table('persons', persons_list)
    login_table = database.Table('login', login_list)
    project_table = database.Table('project', project_list)
    adviser_request_table = database.Table('adviser_request',
                                           adviser_request_list)
    member_request_table = database.Table('member_request',
                                          member_request_list)

    my_DB.insert(persons_table)
    my_DB.insert(login_table)
    my_DB.insert(project_table)
    my_DB.insert(adviser_request_table)
    my_DB.insert(member_request_table)


# here are things to do in this function:

# create an object to read all csv files that will serve as a persistent state for this program

# create all the corresponding tables for those csv files

# see the guide how many tables are needed

# add all these tables to the database


# define a function called login

def login():
    print('Please, enter your username or password.')
    username = input('Enter Username: ')
    password = input('Enter your password: ')
    for i in my_DB.search('login').table:
        if i['username'] == username and i['password'] == password:
            print(
                f"Hello, {my_DB.search('persons').table[my_DB.search('login').table.index(i)]['fist']}"
                f" {my_DB.search('persons').table[my_DB.search('login').table.index(i)]['last']}")
            return i['ID'], i['role']
    return None


def admin_commands():
    print('/help to view every commands')
    while True:
        user_input = int(input('Input Number: '))
        if user_input == 'exit':
            break
        if user_input == '/help':
            print('1. View every student')
            print('2. View every project')
            print('3. View project member')
            print('4. Changes role')
            print('5. Add student or remove student')
            print('6. Add or remove project')
            print('Type exit to exit')
            if user_input == 1:
                view_student()
            elif user_input == 2:
                view_project()
            elif user_input == 3:
                view_member()
            elif user_input == 4:
                change_role_or_add_admin()
            elif user_input == 5:
                add_remove_student()
            elif user_input == 6:
                add_remove_project()


def student():
    have_project = False
    if user_id in my_DB.search('project'):
        have_project = True
    if have_project:
        edit_project()
        pass
        # Edit Project
    else:
        create_project()
        # create project


def create_project():
    # ProjectID, Title, Lead, Member1, Member2, Advisor, Status
    new_project = {}
    new_project['ProjectID'] = str(random.randint(1111111, 9999999))
    new_project['Title'] = input("Enter Project's name: ")
    new_project['Lead'] = user_id
    print('Select Member 1:')
    invite_user(new_project['ProjectID'], 'student')
    new_project['Member1'] = ''
    print('Select Member 2:')
    invite_user(new_project['ProjectID'], 'student')
    new_project['Member2'] = ''
    print('Select Advisor:')
    invite_user(new_project['ProjectID'], 'faculty')
    new_project['Advisor'] = ''
    new_project['Status'] = 'Pending'
    my_DB.search('project').table.append(new_project)
    print(new_project)
    print("Adding...")
    time.sleep(1)
    print("Project Created.")
    my_DB.search('member_request').print()


def invite_user(Project_ID, type):
    # ProjectID, to_be_member, Response, Response_date
    my_DB.search('persons').filter(lambda x: x['type'] == type).print()
    student_id = input(f'Enter {type} ID: ')
    new_member_request = {}
    new_member_request['ProjectID'] = Project_ID
    new_member_request['to_be_member'] = student_id
    new_member_request['Response'] = 'Pending'
    new_member_request['Response_date'] = ''
    my_DB.search('member_request').table.append(new_member_request)


def edit_project():



def view_student():
    for i in my_DB.search('persons').table:
        print(
            f"ID: {i['ID']} Full name: {i['fist']} {i['last']} Type: {i['type']}")


def view_project():
    num_project = 1
    for i in my_DB.search('project').table:
        print(f'{num_project}. Title: {i["Title"]} Project: {i["ProjectID"]}')
        num_project += 1


def view_member():
    project_id_input = input('Enter Project ID: ')
    for i in my_DB.search('project').table:
        member_checker1 = i['Member1']
        member_checker2 = i['Member2']
        if member_checker1 == '':
            member_checker1 = 'No one'
        if member_checker2 == '':
            member_checker2 = 'No one'
        if i['ProjectID'] == project_id_input:
            print(
                f"Lead: {i['Lead']} Member1: {member_checker1} Member2: {member_checker2} ")
            print(f"Advisor: {i['Adviser']} Status: {i['Status']}")


def add_remove_student():
    user_add_remove = input('add or remove: ')
    if user_add_remove == 'remove':
        student_id = str(input("Enter Student ID: "))
        for i in my_DB.search('persons').table:
            if i['ID'] == student_id:
                my_DB.search('persons').table.pop(
                    my_DB.search('persons').table.index(i))
                print('Removing...')
                time.sleep(2)
                print('Student Removed')

    if user_add_remove == 'add':
        new_student = {}
        new_student['ID'] = str(random.randint(1111111, 9999999))
        new_student['fist'] = input("Enter Student Firstname: ")
        new_student['last'] = input("Enter Student lastname: ")
        new_student['Type'] = input("Enter Student Type: ")
        my_DB.search('persons').table.append(new_student)
        print("Adding...")
        time.sleep(2)
        print("Student Added.")


def add_remove_project():
    user_input = input('Add or remove project? (Type add/remove): ')
    if user_input == 'Remove':
        remove_id = input('Enter Project ID: ')
        for i in my_DB.search('project').table:
            if i['ProjectID'] == remove_id:
                my_DB.search('project').table.pop(
                    my_DB.search('project').table.index(i))
                print('Removing...')
                time.sleep(3)
                print('Project Removed')


def change_role_or_add_admin():
    user_input = input('Change role in class or add people to project: ')
    if user_input == 'class':
        student_id = input('Enter ID: ')
        new_role = input('Enter Type: ')
        for i in my_DB.search('persons').table:
            if student_id == i['ID']:
                i['type'] = new_role
    if user_input == 'project':
        project_id = input('Enter Project ID: ')
        student_id = input('Enter Student ID: ')
        for i in my_DB.search('project').table:
            if i['ProjectID'] == project_id:
                if student_id in my_DB.search('project').table.index(i):
                    print('What role you wanna change it to?')
                    print("1. Lead")
                    print("2. Member1")
                    print("3. Member2")



# here are things to do in this function:
# add code that performs a login task
# ask a user for a username and password
# returns [ID, role] if valid, otherwise returning None

# define a function called exit
def exit():
    # myFile = open('demo_file.csv', 'w')
    # writer = csv.writer(myFile)
    # writer.writerow(['Name', 'Roll', 'Language'])
    # for dictionary in listOfDict:
    #     writer.writerow(dictionary.values())
    # myFile.close()
    pass


# here are things to do in this function:
# write out all the tables that have been modified to the corresponding csv files
# By now, you know how to read in a csv file and transform it into a list of dictionaries. For this project, you also need to know how to do the reverse, i.e., writing out to a csv file given a list of dictionaries. See the link below for a tutorial on how to do this:

# https://www.pythonforbeginners.com/basics/list-of-dictionaries-to-csv-in-python


# make calls to the initializing and login functions defined above

initializing()
val = login()
user_id = val[0]
# based on the return value for login, activate the code that performs activities according to the role defined for that person_id

if val[1] == 'admin':
    admin_commands()
elif val[1] == 'student':
    student()
# see and do student related activities
# elif val[1] = 'member':
# see and do member related activities
# elif val[1] = 'lead':
# see and do lead related activities
# elif val[1] = 'faculty':
# see and do faculty related activities
# elif val[1] = 'advisor':
# see and do advisor related activities

# once everything is done, make a call to the exit function
exit()
