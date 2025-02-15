# build a CLI that 

# welcomes users and display a menu with options
    # to add tasks
    # to view tasks
    # to delete tasks
    # to quit the application

# tasks should be stored in a list 

print("\nWelcome to Module 1's Project: Use this To Do Application to organize your tasks today!")

users_tasks = []
user_selection = 0

while user_selection != 4:
    core_features = ["Enter '1' to add tasks.", "Enter '2' to view tasks.", "Enter '3' to delete tasks.", "Enter '4' to quit the application."]
    print("\nTo Do List Options: ")
    for core, features in enumerate(core_features, start=1):
        print(f"{core}. {features}")
    
    try:
        user_selection = int(input("\nPlease select an option from the list above: "))
        print(F"\nTesting - User selected: {user_selection}")
    
        # user_selection = int(user_selection)
        if user_selection not in [1, 2, 3, 4]:
            print("Invalid selection. Please try again. 1")
        elif user_selection == 4:
            print("\nHave a nice day.")
            break

        elif user_selection == 1:
            add_tasks = input("\nAdd a new task: ")
            users_tasks.append(add_tasks)
            # print(f"Testing - user tasks {users_tasks}")

        elif user_selection == 2:
            if users_tasks == []:
                print("\nYour to do list is currently empty. Let's add something! 1")
            print(f"\nTo Do List")
            for task, tasks in enumerate(users_tasks, start=1):
                print(f"{task}. {tasks}")

        elif user_selection == 3:
            if users_tasks == []:
                print("\nYour to do list is currently empty. Let's add something! 2")
            try:
                delete_task =int(input(f"\nEnter the index of the task you'd like to delete: ")) - 1
                if delete_task < 0:
                    print(f"\n{delete_task} is not a valid number. Please try again.")
                elif delete_task >= len(users_tasks):
                    print(f"\nTask #{delete_task} does not exist. Please try again.")
                    print(f"\ndelete tasks = {delete_task}")
                    print(f"user tasks = {users_tasks}")
                    
                else:
                    task_deleted = users_tasks.pop(delete_task)
                    print(len(users_tasks))
                    print(f"\nThe task {task_deleted} was removed.")
                    print(f"updated list after deleting {users_tasks}")
            except ValueError:
                print("\nInvalid selection. please try again. 3")
            except IndexError:
                print("\nInvalid selection. please try again. 4")
    except ValueError:
        print("Please enter a number.")

    # if user_selection == 4:
    #     print("Have a nice day.")
    #     break


    
    # try:
    #     user_selection = input("\nPlease select an option from the list above: ").lower()
    #     print(F"User selected: {user_selection}")
    #     if user_selection == "quit":
    #         print("Have a nice day.")
    #         break
        
    #     user_selection = int(user_selection)
    #     if user_selection == 1:
    #         add_tasks = input("Add a new task: ")
            
    #     if user_selection not in [1, 2, 3, 4]:
    #         print("Invalid selection, please try again.")

    # except ValueError:
    #     print("Invalid selection, please try again.")
    #     continue
    
    # # elif user_selection == "1":
    # #     try:
    # #         add_tasks = input("Add a new task: ")