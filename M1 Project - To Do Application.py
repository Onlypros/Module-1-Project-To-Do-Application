print("\nWelcome to Module 1's Project: Use this To Do Application to organize your tasks today!")

users_tasks = []
user_selection = 0

# Functions
def print_features():
    for core, features in enumerate(core_features, start=1):
            print(f"{core}. {features}")

def display_tasks():
    print("\nTo Do List:")
    for task, tasks in enumerate(users_tasks, start=1):
                print(f"{task}. {tasks}")

# Program
while user_selection != 4:
    core_features = ["Enter '1' to add tasks.", "Enter '2' to view tasks.", "Enter '3' to delete tasks.", "Enter '4' to quit the application."]
    print("\nTo Do List Options:")
    print_features()
    
    try:
        user_selection = int(input("\nPlease select an option from the list above: ").strip())
        # print(F"\nTesting - User selected: {user_selection}")
    
        if user_selection not in [1, 2, 3, 4]:
            print("Invalid selection. Please pick a number 1-4.")
            continue
        elif user_selection == 4:
            print("\nCome back soon!")
            break

        elif user_selection == 1:
            add_tasks = input("\nAdd a new task: ").title().strip()
            if add_tasks == "":
                print("\nNo new task detected. Please try again.")
                continue
            users_tasks.append(add_tasks)
            print(f"\n{add_tasks} has been added to your to do list.")
            # print(f"Testing - user tasks = {users_tasks}")

        elif user_selection == 2:
            if users_tasks == []:
                print("\nYour to do list is empty. Let's add your first task!")
                continue
            display_tasks()

        elif user_selection == 3:
            if not users_tasks:
                #I learned how "not user_tasks:" is more efficent than "if users_tasks == []:"
                print("\nYour to do list is empty.")
                continue
            try:
                delete_task =int(input(f"\nEnter the index of the task you'd like to delete starting at 1: ").strip()) - 1
                if delete_task < 0:
                    print(f"\n{delete_task} is not a valid number. Please try again.\n")
                    continue
                elif delete_task >= len(users_tasks):
                    print(f"\nTask #{delete_task + 1} does not exist. Please try again.")
                    # print(f"\ntesting - delete tasks = {delete_task}")
                    # print(f"testing - user tasks = {users_tasks}")
                    continue
                else:
                    task_deleted = users_tasks.pop(delete_task)
                    # print(f"testing len of user tasks = {len(users_tasks)}")
                    print(f"\n{task_deleted} was removed from your list.")
                    display_tasks()
            except ValueError:
                print("\nInvalid selection. Please try again.")
    except ValueError:
        print("Invalid selection. Please pick a number 1-4.")