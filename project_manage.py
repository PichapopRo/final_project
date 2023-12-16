# import database module
import database
import random
import time

# define a function called initializing
my_DB = database.DB()


def initializing():
    my_DB.read_csv('persons','persons.csv')
    my_DB.read_csv('login','login.csv')
    my_DB.read_csv('project','project.csv')
    my_DB.read_csv('request', 'request.csv')
    


# here are things to do in this function:

# create an object to read all csv files that will serve as a persistent state for this program

# create all the corresponding tables for those csv files

# see the guide how many tables are needed

# add all these tables to the database


# define a function called login

def login():
    print('Enter your username and password.')
    username = input('Enter Username: ')
    password = input('Enter your password: ')
    for i in my_DB.search('login').table:
        if i['username'] == username and i['password'] == password:
            print(
                f"Hello, {my_DB.search('persons').table[my_DB.search('login').table.index(i)]['fist']}"
                f" {my_DB.search('persons').table[my_DB.search('login').table.index(i)]['last']}")
            return i['ID'], i['role']
    print('Invalid username or password. Try again.')
    return None


def admin():
    print('/help to view every commands')
    while True:
        user_input = input('Input Number: ')
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
        if user_input == '1':
            view_student()
        elif user_input == '2':
            view_project()
        elif user_input == '3':
            view_member()
        elif user_input == '4':
            change_role_or_add_admin()
        elif user_input == '5':
            add_remove_student()
        elif user_input == '6':
            add_remove_project()


def student():
    while True:
        have_project = False
        notification = 0
        if user_id in my_DB.search('project').select(['Lead']) or user_id in my_DB.search('project').select(['Member1']) or my_DB.search('project').select(['Member2']):
            have_project = True
        for student_record in my_DB.search('request').table:
            print(student_record)
            if student_record['MemberID'] == user_id:
                notification += 1
        if have_project:
            if notification == 0:
                print(f"You don't have any notification")
            else:
                print(f"You have {notification} notifications.")
            for j in my_DB.search('project').table:
                if j['Lead'] == user_id:
                    print("Select function")
                    user_input = input("(edit / notification / exit / response): ")
                else:
                    print("Select function")
                    user_input = input("(view info / notification / exit / response): ")
                if user_input == 'exit':
                    return
                if user_input == 'response':
                    response_request('student')
                if user_input == 'edit':
                    # Edit Project
                    edit_project(user_id)
                if user_input == 'view member':
                    for _ in my_DB.search('project').table:
                        if _['Lead'] == user_id or _['Member1'] == user_id or _['Member2'] == user_id:
                            print(f"Project ID: {_['ProjectID']}")
                            print(f"Project Title: {_['Title']}")
                            for student_record in my_DB.search('persons').table:
                                if student_record['ID'] == _['Lead']:
                                    print(f"Lead: {_['Lead']} {student_record['fist']} {student_record['last']}")
                                if student_record['ID'] == _['Member1']:
                                    print(f"Member1: {_['Member1']} {student_record['fist']} {student_record['last']}")
                                if student_record['ID'] == _['Member2']:
                                    print(f"Member2: {_['Member2']} {student_record['fist']} {student_record['last']}")
                                if student_record['ID'] == _['Advisor']:
                                    print(f"Advisor: {_['Advisor']} {student_record['fist']} {student_record['last']}")
                if user_input == 'notification':
                    if notification > 0:
                        print('Notifications')
                        for student_record in my_DB.search('request').table:
                            if student_record['MemberID'] == user_id:
                                for j in my_DB.search('project').table:
                                    counter = 1
                                    if j['ProjectID'] == student_record['ProjectID']:
                                        print(f"{counter}. {j['ProjectID']} {j['Title']} project have invited you to join.")
                                        counter += 1
                    if notification == 0:
                        print("I told you. You don't have any notification"
                            "haiyaaa...")
        if not have_project:
            print("Looks like you don't have a project...")
            if notification == 0:
                print("You don't have any notification.")
            else:
                print(f"You have {notification} notifications")
            print("What's on your thoughts?")
            user_input = input("(create project / notification / exit): ")
            if user_input == 'create project':
                create_project()
            if user_input == 'exit':
                break
            if user_input == 'notification':
                if notification > 0:
                    print('Notification')
                    for student_record in my_DB.search('request').table:
                        if student_record['MemberID'] == user_id:
                            for j in my_DB.search('project').table:
                                counter = 1
                                if j['ProjectID'] == student_record['ProjectID']:
                                    print(f"{counter}. {j['ProjectID']} {j['Title']} project have invited you to join.")
                                    counter += 1
                if notification == 0:
                    print("I told you. You don't have any notification la "
                        "haiyaaa...")
def faculty():
    while True:
        have_project = False
        notification = 0
        if user_id in my_DB.search('project').select(['Advisor']):
            have_project = True
        for i in my_DB.search('request').table:
            if i['MemberID'] == user_id:
                notification += 1
        if notification == 0:
                print(f"You don't have any notification")
        else:
            print(f"You have {notification} notifications.")
        # Have project
        if have_project:
            print("Select function: ")
            user_input = input('d')



def response_request(request_type):
    if request_type == 'student':
        for _ in my_DB.search('request').table:
            if _['MemberID'] == user_id:
                for j in my_DB.search('project').table:
                    if j['ProjectID'] == _['ProjectID']:
                        print(
                            f"{j['ProjectID']} {j['Title']}.")
                print(f"{_['ProjectID']} {_['Title']}")
        project_id = input("Enter Project ID: ")
        response = input("What's your response? (Accept/Declined) : ")
        for i in my_DB.search('request').table:
            if i['MemberID'] == user_id and i['ProjectID'] == project_id:
                i['Response'] = response
            for j in my_DB.search('project').table:
                if j['ProjectID'] == project_id:
                    if j['Member1'] == '':
                        j['Member1'] = user_id
                    else:
                        j['Member2'] = user_id
    if request_type == 'faculty':
        project_id = input("Enter Project ID: ")
        response = input("What's your response?: ")
        for i in my_DB.search('request').table:
            if i['MemberID'] == user_id and i['ProjectID'] == project_id:
                i['Response'] = response
            for j in my_DB.search('project').table:
                if j['ProjectID'] == project_id:
                    j['advisor'] = user_id


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
    print("Adding...")
    time.sleep(1)
    print("Project Created.")


def invite_user(Project_ID, type_user):
    # ProjectID, to_be_member, Response, Response_date
    for i in my_DB.search('persons').filter(lambda x: x['type'] == type_user).table:
        print(f"{i['ID']} {i['fist']} {i['last']}")
    member_id = input(f'Enter {type_user} ID: ')
    new_member_request = {}
    if type_user == 'student':
        new_member_request['Type'] = 'to_be_member'
    if type_user == 'faculty':
        new_member_request['Type'] = 'to_be_advisor'
    new_member_request['ProjectID'] = Project_ID
    new_member_request['MemberID'] = member_id
    new_member_request['Response'] = 'Pending'
    new_member_request['Response_date'] = ''
    my_DB.search('request').table.append(new_member_request)


def edit_project(ID):
    print('What would you like to edit?')
    edit_input = input('(Title, Member1, Member2) ')
    if edit_input == 'Title' or edit_input == 'title':
        for i in my_DB.search('project').table:
            if i['Lead'] == ID or i['Member1'] == ID or i['Member2'] == ID:
                i['Title'] = input('Enter new title: ')
                print('Title changed.')
    if edit_input == 'Member1':
        for student_info in my_DB.search('persons').filter(
                lambda x: x['type'] == 'student').table:
            print(
                f"{student_info['ID']} {student_info['fist']} {student_info['last']}")
        new_member = input('Enter ID: ')
        for student_record in my_DB.search('project').table:
            if student_record['ProjectID'] == project_ID:
                student_record['Member1'] = new_member
    if edit_input == 'Member2':
        for student_record in my_DB.search('persons').filter(
                lambda x: x['type'] == 'student').table:
            print(
                f"{student_record['ID']} {student_record['fist']} {student_record['last']}")
        while True:
            new_member = input('Enter ID: ')
            for student_record in my_DB.search(
                    'project').table:
                if student_record['ProjectID'] == project_ID:
                    student_record['Member1'] = new_member
    if edit_input == 'exit':
        return

def view_student():
    for i in my_DB.search('persons').table:
        print(
            f"ID: {i['ID']} Fullname: {i['fist']} {i['last']} Type: {i['type']}")


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
                time.sleep(1)
                print('Student Removed')

    if user_add_remove == 'add':
        new_student = {}
        new_student['ID'] = str(random.randint(1111111, 9999999))
        new_student['fist'] = input("Enter Student Firstname: ")
        new_student['last'] = input("Enter Student lastname: ")
        new_student['Type'] = input("Enter Student Type: ")
        my_DB.search('persons').table.append(new_student)
        print("Adding...")
        time.sleep(1)
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
                time.sleep(1)
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
    my_DB.write_csv('persons.csv', my_DB.search('persons').table)
    my_DB.write_csv('login.csv', my_DB.search('login').table)
    my_DB.write_csv('project.csv', my_DB.search('project').table)
    my_DB.write_csv('request.csv', my_DB.search('request').table)
# here are things to do in this function:
# write out all the tables that have been modified to the corresponding csv files
# By now, you know how to read in a csv file and transform it into a list of dictionaries. For this project, you also need to know how to do the reverse, i.e., writing out to a csv file given a list of dictionaries. See the link below for a tutorial on how to do this:

# https://www.pythonforbeginners.com/basics/list-of-dictionaries-to-csv-in-python


# make calls to the initializing and login functions defined above
initializing()
val = login()
user_id = val[0]
project_ID = ''
for _ in my_DB.search('project').table:
    if _['Lead'] == user_id or _['Member1'] == user_id or _['Member2'] == user_id:
        project_ID = _['ProjectID']
# based on the return value for login, activate the code that performs activities according to the role defined for that person_id

if val[1] == 'admin':
    admin()
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
