# import database module
import database
import random
import time
import datetime

my_DB = database.DB()
time_atm = datetime.datetime.now()


def initializing():
    my_DB.read_csv('persons', 'persons.csv')
    my_DB.read_csv('login', 'login.csv')
    my_DB.read_csv('project', 'project.csv')
    my_DB.read_csv('request', 'request.csv')
    my_DB.read_csv('workload', 'workload.csv')
    my_DB.read_csv('grading', 'grading.csv')


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
    print('Invalid username or password.')
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
            print('4. Changes project status')
            print('5. Add student or remove student')
            print('6. Remove project')
            print('7. Add member to project')
            print('8. Add advisor')
            print('Type exit to exit')
        if user_input == '1':
            view_student()
        elif user_input == '2':
            view_project()
        elif user_input == '3':
            view_member()
        elif user_input == '4':
            change_project_status()
        elif user_input == '5':
            add_remove_student()
        elif user_input == '6':
            remove_project()
        elif user_input == '7':
            add_member_admin()
        else:
            print('Invalid input')


def student():
    while True:
        have_project = False
        notification = 0
        if user_id in my_DB.search('project').select(
                ['Lead']) or user_id in my_DB.search('project').select(
            ['Member1']) or my_DB.search('project').select(['Member2']):
            have_project = True
        for student_record in my_DB.search('request').table:
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
                    print('1. Edit')
                    print('2. Notification')
                    print('3. Response')
                    print('4. Remove project')
                    print('5. Assign work')
                    print('6. View all workload')
                    print('7. View my workload.')
                    print('exit')
                    user_input = input("Input number: ")
                    if user_input == '1':
                        edit_project(user_id)
                    elif user_input == '4':
                        print('Are you sure?')
                        remove_input = input('(yes/no): ')
                        if remove_input == 'yes':
                            for i in my_DB.search('project').table:
                                if i['ProjectID'] == project_ID:
                                    my_DB.search('project').table.pop(
                                        my_DB.search('project').table.index(i))
                            print('Project removed.')
                        elif remove_input == 'no':
                            break
                        else:
                            print('Invalid input.')
                    elif user_input == '5':
                        workload_giver()
                    elif user_input == '6':
                        view_project_workload()
                    elif user_input == '7':
                        view_workload()
                    elif user_input == '3':
                        response_request('student')
                        if response_request('student') == '':
                            print("You don't have any request to response.")
                    elif user_input == '1':
                        for _ in my_DB.search('project').table:
                            if _['Lead'] == user_id or _[
                                'Member1'] == user_id or \
                                    _['Member2'] == user_id:
                                print(f"Project ID: {_['ProjectID']}")
                                print(f"Project Title: {_['Title']}")
                                for student_record in my_DB.search(
                                        'persons').table:
                                    if student_record['ID'] == _['Lead']:
                                        print(
                                            f"Lead: {_['Lead']} "
                                            f"{student_record['fist']} "
                                            f"{student_record['last']}")
                                    if student_record['ID'] == _['Member1']:
                                        print(
                                            f"Member1: {_['Member1']} "
                                            f"{student_record['fist']} "
                                            f"{student_record['last']}")
                                    if student_record['ID'] == _['Member2']:
                                        print(
                                            f"Member2: {_['Member2']} "
                                            f"{student_record['fist']} "
                                            f"{student_record['last']}")
                                    if student_record['ID'] == _['Advisor']:
                                        print(
                                            f"Advisor: {_['Advisor']} "
                                            f"{student_record['fist']} "
                                            f"{student_record['last']}")
                    elif user_input == '2':
                        if notification > 0:
                            print('Notifications')
                            for student_record in my_DB.search(
                                    'request').table:
                                if student_record['MemberID'] == user_id:
                                    for j in my_DB.search('project').table:
                                        counter = 1
                                        if j['ProjectID'] == student_record[
                                            'ProjectID']:
                                            print(
                                                f"{counter}. {j['ProjectID']} {j['Title']} project have invited you to join.")
                                            counter += 1
                    else:
                        print('Invalid input.')
                else:
                    print("Select function")
                    print("1. View project's info")
                    print('2. Notification')
                    print('3. Response')
                    print('4. View my workload')
                    print('exit')
                    user_input = input("Input number: ")
                    if user_input == '4':
                        view_workload()
                    if user_input == 'exit':
                        return
                    elif user_input == '3':
                        response_request('student')
                        if response_request('student') == '':
                            print("You don't have any request to response.")
                    elif user_input == '1':
                        for _ in my_DB.search('project').table:
                            if _['Lead'] == user_id or _[
                                'Member1'] == user_id or \
                                    _['Member2'] == user_id:
                                print(f"Project ID: {_['ProjectID']}")
                                print(f"Project Title: {_['Title']}")
                                for student_record in my_DB.search(
                                        'persons').table:
                                    if student_record['ID'] == _['Lead']:
                                        print(
                                            f"Lead: {_['Lead']} {student_record['fist']} {student_record['last']}")
                                    if student_record['ID'] == _['Member1']:
                                        print(
                                            f"Member1: {_['Member1']} {student_record['fist']} {student_record['last']}")
                                    if student_record['ID'] == _['Member2']:
                                        print(
                                            f"Member2: {_['Member2']} {student_record['fist']} {student_record['last']}")
                                    if student_record['ID'] == _['Advisor']:
                                        print(
                                            f"Advisor: {_['Advisor']} {student_record['fist']} {student_record['last']}")
                    elif user_input == '2':
                        if notification > 0:
                            print('Notifications')
                            for student_record in my_DB.search(
                                    'request').table:
                                if student_record['MemberID'] == user_id:
                                    for j in my_DB.search('project').table:
                                        counter = 1
                                        if j['ProjectID'] == student_record[
                                            'ProjectID']:
                                            print(
                                                f"{counter}. {j['ProjectID']} {j['Title']} project have invited you to join.")
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
            print("Select function")
            print('1. Create project')
            print('2. Notification')
            print('3. Response')
            print('exit')
            user_input = input("Select number: ")
            if user_input == '1':
                create_project()
            elif user_input == 'exit':
                break
            elif user_input == '2':
                if notification > 0:
                    print('Notification')
                    for student_record in my_DB.search('request').table:
                        if student_record['MemberID'] == user_id:
                            for j in my_DB.search('project').table:
                                counter = 1
                                if j['ProjectID'] == student_record[
                                    'ProjectID']:
                                    print(
                                        f"{counter}. {j['ProjectID']} {j['Title']} project have invited you to join.")
                                    counter += 1
                if notification == 0:
                    print("I told you. You don't have any notification la "
                          "haiyaaa...")
            elif user_input == '3':
                response_request('student')


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
            print('1. View every student')
            print('2. View every project')
            print('3. Notification')
            print('4. Response')
            print('5. View project info')
            print('6. View every workload')
            print('exit')
            user_input = input('Input number: ')
            if user_input == '1':
                for student_info in my_DB.search('persons').filter(
                        lambda x: x['type'] == 'student').table:
                    print(
                        f"{student_info['ID']} {student_info['fist']} {student_info['last']}")
            elif user_input == '2':
                view_project()
            elif user_input == '3':
                if notification > 0:
                    print('Notifications')
                    for student_record in my_DB.search('request').table:
                        if student_record['MemberID'] == user_id:
                            for j in my_DB.search('project').table:
                                counter = 1
                                if j['ProjectID'] == student_record[
                                    'ProjectID']:
                                    print(
                                        f"{counter}. {j['ProjectID']} {j['Title']} project have invited you to join.")
                                    counter += 1
                if notification == 0:
                    print("I told you. You don't have any notification"
                          "haiyaaa...")
            elif user_input == '4':
                response_request('faculty')
                if response_request('student') == '':
                    print("You don't have any request to response.")
            elif user_input == '5':
                for i in my_DB.search('project').table:
                    if i['ProjectID'] == project_ID:
                        print(f"Project ID: {i['ProjectID']}")
                        for j in my_DB.search('persons').table:
                            if i['Lead'] == j['ID']:
                                print(
                                    f"Lead: {j['ID']} {j['fist']} {j['last']}")
                        for j in my_DB.search('persons').table:
                            if i['Member1'] == j['ID']:
                                print(f": {j['ID']} {j['fist']} {j['last']}")
                        for j in my_DB.search('persons').table:
                            if i['Member2'] == j['ID']:
                                print(f": {j['ID']} {j['fist']} {j['last']}")
                        for j in my_DB.search('persons').table:
                            if i['Advisor'] == j['ID']:
                                print(f": {j['ID']} {j['fist']} {j['last']}")
            elif user_input == 'exit':
                break
            elif user_input == '6':
                view_workload()
            if not have_project:
                print("Select function: ")
                print('1. View every student')
                print('2. View every project')
                print('3. Notification')
                print('4. Response')
                print('5. Create grading field')
                print('6. Grading')
                print('exit')
                user_input = input('Input number: ')
                if user_input == '1':
                    for student_info in my_DB.search('persons').filter(
                            lambda x: x['type'] == 'student').table:
                        print(
                            f"{student_info['ID']} {student_info['fist']} {student_info['last']}")
                elif user_input == '2':
                    view_project()
                elif user_input == '3':
                    if notification > 0:
                        print('Notifications')
                        for student_record in my_DB.search('request').table:
                            if student_record['MemberID'] == user_id:
                                for j in my_DB.search('project').table:
                                    counter = 1
                                    if j['ProjectID'] == student_record[
                                        'ProjectID']:
                                        print(
                                            f"{counter}. {j['ProjectID']} {j['Title']} project have invited you to join.")
                                        counter += 1
                    if notification == 0:
                        print("I told you. You don't have any notification"
                              "haiyaaa...")
                elif user_input == '4':
                    response_request('faculty')
                    if response_request('student') == '':
                        print("You don't have any request to response.")
                elif user_input == 'exit':
                    break
                elif user_input == '5':
                    create_grading()
                elif user_input == '6':
                    grading()


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
                        response = input(
                            "What's your response? (accept/decline): ")
                        for i in my_DB.search('request').table:
                            if (i['MemberID'] == user_id and
                                    i['ProjectID'] == project_id):
                                i['Response'] = response
                                i[
                                    'Response_date'] = f'{time_atm.strftime("%d")} {time_atm.strftime("%b")} {time_atm.strftime("%Y")}'
                            for j in my_DB.search('project').table:
                                if j['ProjectID'] == project_id:
                                    if j['Member1'] == '':
                                        j['Member1'] = user_id
                                    else:
                                        j['Member2'] = user_id
                                        return

    if request_type == 'faculty':
        project_id = input("Enter Project ID: ")
        response = input("What's your response? (accept/decline): ")
        for i in my_DB.search('request').table:
            if i['MemberID'] == user_id and i['ProjectID'] == project_id:
                i['Response'] = response
                i[
                    'Response_date'] = f'{time_atm.strftime("%d")} {time_atm.strftime("%b")} {time_atm.strftime("%Y")}'
            if response == 'accept':
                for j in my_DB.search('project').table:
                    if j['ProjectID'] == project_id:
                        j['advisor'] = user_id
                for project in my_DB.search('project').table:
                    if project['ProjectID'] == project_id:
                        project['Status'] = 'Approved'
                        return
            if response == 'decline':
                for project in my_DB.search('project').table:
                    if project['ProjectID'] == project_id:
                        project['Status'] = 'Rejected'
                        return
    return ''


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
    for i in my_DB.search('persons').filter(
            lambda x: x['type'] == type_user).table:
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
    edit_input = input('(title, member1, member2) ')
    if edit_input == 'Title' or edit_input == 'title':
        for i in my_DB.search('project').table:
            if i['Lead'] == ID or i['Member1'] == ID or i['Member2'] == ID:
                i['Title'] = input('Enter new title: ')
                print('Title changed.')
    if edit_input == 'member1':
        for student_info in my_DB.search('persons').filter(
                lambda x: x['type'] == 'student').table:
            print(
                f"{student_info['ID']} {student_info['fist']} {student_info['last']}")
        new_member = input('Enter ID: ')
        for student_record in my_DB.search('project').table:
            if student_record['ProjectID'] == project_ID:
                student_record['Member1'] = new_member
    if edit_input == 'member2':
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
        if i['ProjectID'] == project_id_input:
            print(
                f"Lead: {i['Lead']} Member1: {i['Member1']} Member2: {i['Member1']} ")
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


def remove_project():
    while True:
        remove_id = input('Enter Project ID: ')
        if remove_id in my_DB.search('project').select(['ProjectID']):
            break
    for i in my_DB.search('project').table:
        if i['ProjectID'] == remove_id:
            my_DB.search('project').table.pop(
                my_DB.search('project').table.index(i))
            print('Removing...')
            time.sleep(1)
            print('Project Removed')


def change_project_status():
    user_input = input('Input project ID: ')
    for i in my_DB.search('project').table:
        if i['ProjectID'] == user_input:
            status_input = input('Status: ')
            i['Status'] = status_input


def workload_giver():
    new_workload = {}
    new_workload['ProjectID'] = project_ID
    new_workload['WorkID'] = str(random.randint(1111111, 9999999))
    new_workload['Title'] = input('Input work title: ')
    for i in my_DB.search('project').table:
        if i['ProjectID'] == project_ID:
            for j in my_DB.search('persons').table:
                if i['Lead'] == j['ID']:
                    print(
                        f"Lead: {j['ID']} {j['fist']} {j['last']}")
            for j in my_DB.search('persons').table:
                if i['Member1'] == j['ID']:
                    print(f": {j['ID']} {j['fist']} {j['last']}")
            for j in my_DB.search('persons').table:
                if i['Member2'] == j['ID']:
                    print(f": {j['ID']} {j['fist']} {j['last']}")
    while True:
        new_workload['Handler'] = input('Enter member ID: ')
        project_filtered = my_DB.search('project').filter(
            lambda x: x['ProjectID'] == project_ID)
        if new_workload['Handler'] in project_filtered.table:
            break
    new_workload['deadline'] = input('Enter deadline: ')
    new_workload['Status'] = 'Assigned'


def change_workload_status():
    for i in my_DB.search('workload').table:
        if i['ProjectID'] == project_ID and i['Handler'] == user_id:
            print(f"Workload ID: {i['WorkID']} Title: {i['Title']}")
            i['status'] = input('Enter Status: ')
        else:
            print("Work not found.")


def view_workload():
    if len(my_DB.search('workload').table) > 0:
        for i in my_DB.search('workload').table:
            if i['ProjectID'] == project_ID and i['Handler'] == user_id:
                print(f"Workload ID: {i['WorkID']} Title: {i['Title']}")
            else:
                print('Congrats! There are no work for you.')
    else:
        print('Congrats! There are no work for you.')


def view_project_workload():
    for i in my_DB.search('workload').table:
        if i['ProjectID'] == project_ID:
            print(f"{i['Title']}")
            for j in my_DB.search('persons').table:
                if i['Handler'] == j['ID']:
                    print(f"Responsible member: {j['fist']} {j['last']}")
        else:
            print('There are no work that have been assigned.')


def create_grading():
    graded_project = {}
    for i in my_DB.search('project').table:
        print(f"Project ID: {i['ProjectID']} Title: {i['Title']}")
    while True:
        project_input = input('Input project ID: ')
        if project_input in my_DB.search('project').select(['ProjectID']):
            break
        else:
            print('Invalid ID.')
    # ProjectID,examiner1,examiner2,examiner3,score1,score2,score3,total
    graded_project['ProjectID'] = project_input
    graded_project['examiner1'] = ''
    graded_project['examiner2'] = ''
    graded_project['examiner3'] = ''
    graded_project['score1'] = 0
    graded_project['score2'] = 0
    graded_project['score3'] = 0
    graded_project['total'] = ''
    my_DB.search('grading').table.append(graded_project)


def grading():
    for i in my_DB.search('grading').table:
        for j in my_DB.search('project'):
            if j['ProjectID'] == i['ProjectID']:
                print(f"Project ID: {i['ProjectID']} Title: {i['Title']}")
    while True:
        user_input = input('Input project ID: ')
        if user_input in my_DB.search('grading').select(['ProjectID']):
            break
    for i in my_DB.search('grading').table:
        if i['ProjectID'] == project_ID:
            if i['examiner1'] == '':
                i['examiner1'] = user_id
            if i['examiner2'] == '':
                i['examiner2'] = user_id
            if i['examiner3'] == '':
                i['examiner3'] = user_id
    while True:
        score_input = int(input('Input score (0-100): '))
        if 0 < score_input <= 100:
            break
        else:
            print('Invalid score')
    for i in my_DB.search('grading').table:
        if i['ProjectID'] == project_ID:
            if i['score1'] == 0:
                i['score1'] = score_input
            if i['score2'] == 0:
                i['score2'] = score_input
            if i['score3'] == 0:
                i['score3'] = score_input
        total_calculation = [i['score1'], i['score2'], i['score3']]
        i['total'] = f'{sum(total_calculation) / len(total_calculation):.2f}'


def add_member_admin():
    for i in my_DB.search('project').table:
        print(f"Project ID: {i['ProjectID']} Title: {i['Title']}")
    while True:
        project_input = input('Enter project ID: ')
        if project_input in my_DB.search('project').select(['ProjectID']):
            break
        print('Invalid Project ID')
    for i in my_DB.search('project').table:
        if i['ProjectID'] == project_input:
            if i['Member1'] == '' or i['Member2'] == '':
                for j in my_DB.search('persons').filter(
                        lambda x: x['type'] == 'student').table:
                    print(f"{j['ID']} {j['fist']} {j['last']}")
                member_id = input('Enter student ID: ')
                if i['Member1'] == '':
                    i['Member1'] = member_id
                elif i['Member2'] == '':
                    i['Member2'] = member_id
            else:
                print('Member full.')


def add_advisor():
    for i in my_DB.search('project').table:
        print(f"Project ID: {i['ProjectID']} Title: {i['Title']}")
    while True:
        project_input = input('Enter project ID: ')
        if project_input in my_DB.search('project').select(['ProjectID']):
            break
        print('Invalid Project ID')
    for i in my_DB.search('project').table:
        if i['ProjectID'] == project_input:
            if i['Advisor'] == '':
                for j in my_DB.search('persons').filter(
                        lambda x: x['type'] == 'faculty').table:
                    print(f"{j['ID']} {j['fist']} {j['last']}")
                member_id = input('Enter faculty ID: ')
                if i['Advisor'] == '':
                    i['Advior'] = member_id
            else:
                print('This project already had an advisor.')


def exit():
    my_DB.write_csv('persons.csv', my_DB.search('persons').table)
    my_DB.write_csv('login.csv', my_DB.search('login').table)
    my_DB.write_csv('project.csv', my_DB.search('project').table)
    my_DB.write_csv('request.csv', my_DB.search('request').table)
    my_DB.write_csv('workload.csv', my_DB.search('workload').table)
    my_DB.write_csv('grading.csv', my_DB.search('grading').table)


initializing()
val = login()
while val is None:
    val = login()
user_id = val[0]
project_ID = ''
for _ in my_DB.search('project').table:
    if (_['Lead'] == user_id or _['Member1'] == user_id or _['Member2']
            == user_id or _['Advisor'] == user_id):
        project_ID = _['ProjectID']

if val[1] == 'admin':
    admin()
elif val[1] == 'student':
    student()
elif val[1] == 'faculty':
    faculty()
exit()