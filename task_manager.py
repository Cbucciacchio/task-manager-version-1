#=====importing libraries===========

from datetime import date


#====Login Section====

with open("user.txt", "r") as f: # open user.txt file to read usernames and passwords
    users = {} # read all lines from file and create a dictionary of usernames and passwords
    for line in f:
        username, password = line.strip().split(", ")
        users[username] = password

while True: # use a while loop to keep asking for login details until they are valid
    username = input("Enter your username: ") # get username and password from  user
    password = input("Enter your password: ")

    if username in users and users[username] == password: # check if the username exists and the password is correct
        print("Welcome!")
        break  # exit the loop if the login details are valid
    elif username not in users:
        print("Invalid username. Please try again.")
    else:
        print("Invalid password. Please try again.")


while True:
    #presenting the menu to the user and 
    # making sure that the user input is coneverted to lower case.
    menu = input('''Select one of the following Options below:
r - Registering a user (only for admin)
a - Adding a task
va - View all tasks
vm - view my task
s - statistics (only for adimin)
e - Exit
: ''').lower()


    if menu == 'r' and username == "admin": #registering a new user only allowed for the admin user 
        
        new_username = input("Please enter a new username: ")
        new_password = input("Please enter a new password: ")
        new_password_check = input("Please confirm the password: ")
        if new_password == new_password_check: #if both passwords match then add to the user.txt file 
            with open("user.txt", "a") as file:
                new_user = f"{new_username}, {new_password}\n"
                file.write(new_user)
                print("User added successfully.")
        else:
            print("Password confirmation failed. Please try again.")


    elif menu == 'a': #adding a new task

        new_task_user = input("Please enter the username of the person the task is assigned to: ")
        new_task_title = input("Please enter a title for this task: ")
        new_task_desc = input("Please describe this task: \n")
        new_task_duedate = input("Please enter the due date for this task: ")
        new_task_curdate = date.today()
        new_task_done = "No"
        with open("tasks.txt", "a") as file:
            new_task_all = f"{new_task_user}, {new_task_title}, {new_task_desc}, {new_task_duedate}, {new_task_curdate}, {new_task_done}\n"
            file.write(new_task_all)
            print("Task added successfully.")


    elif menu == 'va': #viewing all the tasks

        with open("tasks.txt", "r") as f:# open the tasks.txt file to read the tasks
            for line in f:# iterate over each line in the file and print the tasks in the desired format
                task_user, task_title, task_desc, task_duedate, task_curdate, task_done = line.strip().split(", ")
                print(f"Task assigned to: \t {task_user}")
                print(f"Task title: \t\t {task_title}")
                print(f"Task description: \t {task_desc}")
                print(f"Task due date: \t\t {task_duedate}")
                print(f"Task current date: \t {task_curdate}")
                print(f"Task complete? \t\t {task_done}")
                print("-" * 50)


    elif menu == 'vm': #veiwing the tasks depending on the user that is logged in 

        with open("tasks.txt", "r") as f:# open the tasks.txt file to read the tasks
            for line in f:# iterate over each line in the file and print the tasks in the desired format
                task_user, task_title, task_desc, task_duedate, task_curdate, task_done = line.strip().split(", ")
                if task_user == username:
                    print(f"Task assigned to: \t {task_user}")
                    print(f"Task title: \t\t {task_title}")
                    print(f"Task description: \t {task_desc}")
                    print(f"Task due date: \t\t {task_duedate}")
                    print(f"Task current date: \t {task_curdate}")
                    print(f"Task complete? \t\t {task_done}")
                    print("-" * 50)

    elif menu == 's' and username == "admin":

        with open('tasks.txt', 'r') as f:
            num_tasks = 0
            for line in f:
                num_tasks += 1
            print("-" * 50)
            print(f" Total number of tasks: \t {num_tasks}")
            print("-" * 50)

        with open('user.txt', 'r') as f2:
            num_user = 0
            for line in f2:
                num_user += 1
            print(f" Total number of users: \t {num_user}")
            print("-" * 50)
         


    elif menu == 'e':
        print('Goodbye!!!')
        exit()


    else:
        print("You have made a wrong choice, Please Try again")