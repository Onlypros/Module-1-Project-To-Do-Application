users_tasks = []
- creating an empty list that will later be populated with tasks inputed by the users via the .append() function

user_selection = ""
- creating the variable to trigger the while loop

while user_selection != 4
- setting the trigger for the while loop to STOP

core_features = ["Please press '1' to add tasks.", "Please press '2' to view tasks.", "Please press '3' to delete tasks.", "Please press '4' to quit the application."]
    print()
    for core, features in enumerate(core_features, start=1):
        print(f"{core}. {features}")

- Using enumerate to loop through the list of options aka features and print them so its presented in a nice, neat and orderly list instead of all on one line.



IDEAS
-I want to title case every event entry in case people type in lower to start

