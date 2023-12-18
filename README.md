## What's the program about?
This program is about a project operating system which operates between student and teacher. Students can create a project and invite others to join as a member.
Student who creates project will have role as Lead and faculty who got invited will have an Advisor role. Student who have Lead as a role can assign work to the members.
After a final confirmation advisor can create a grading field for other persons with faculty roles to grade.

## Required Files

- database.py
- project_manage.py
- persons.csv
- login.csv
- request.csv
- project.csv
- grading.csv

### Backup Files

- persons backup.csv
- login backup.csv
- request backup.csv
- project backup.csv
- grading backup.csv

### Admin Action
|       role        | action                       | function                        | method | class |
|:-----------------:|:-----------------------------|:--------------------------------|:------:|:-----:|
|       admin       | view every student           | view_student()                  | search |  DB   |
|       admin       | view every project           | view_project()                  | search |  DB   |
|       admin       | View member of every project | view_member()                   | search |  DB   |
|       admin       | Change project status        | change_project_status()         | search |  DB   |
|       admin       | add or remove student        | add_remove_student()            | search |  DB   |
|       admin       | Remove project               | remove_project()                | search |  DB   |
|       admin       | Add project member for admin | add_member_admin()              | search |  DB   |
|       admin       | Add advisor to project       | add_advisor()                   | search |  DB   |

### Student Action
|       role        | action                       | function                        | method | class |
|:-----------------:|:-----------------------------|:--------------------------------|:------:|:-----:|
|      student      | search for lead              | -                               | select |  DB   |
|      student      | view notification            | add_member_admin()              | search |  DB   |
|      student      | Response to request          | response_request()              | search |  DB   |
|      student      | create project               | create_project()                |   -    |   -   |
|  student (Lead)   | Edit project                 | edit_project(user_id)           | search |  DB   |
|  student (Lead)   | Remove project               | -                               |   -    |   -   |
|  student (Lead)   | Assign work for members      | workload_giver()                | search |  DB   |
|  student (Lead)   | view every workload          | view_project_workload()         | search |  DB   |
| student (member)  | view own workload            | view_workload()                 | search |  DB   |
| student (member)  | view Project info            | -                               |   -    |   -   |

### Faculty Action
|       role        | action                       | function                        | method | class |
|:-----------------:|:-----------------------------|:--------------------------------|:------:|:-----:|
|      faculty      | View every student           | -                               | search |  DB   |
|      faculty      | View every project           | view_project()                  | search |  DB   |
|      faculty      | Notification                 | -                               | search |  DB   |
|      faculty      | Response request             | response_request()              | search |  DB   |
|      faculty      | Grading                      | grading()                       | search |  DB   |
| faculty (advisor) | View project info            | view_project()                  | search |  DB   |
| faculty (advisor) | View every workload          | view_project_workload()         | search |  DB   |
| faculty (advisor) | Create grading field         | create_grading()                |   -    |   -   |
| faculty (advisor) | Change project status        | change_project_status_advisor() | search |  DB   |

## Program's Bug

- When the program trying to write a new information back in, if there's nothing in the csv file it sometimes delete every table in the csv file. That's the reason I include a backup files.
