#prompt for  single task

task = str(input("Enter your task:"))
priority = str(input("Priority (high/medium/low):"))
time_bound = str(input("yes/no:"))

match priority:
    case "high":
        if time_bound == 'yes':
            print(f"{task}, is a {priority}, priority task that requires immediate attention today!")
        else:
            print(f"{task}, is a {priority}, priority task consider completing it as soon as possible.")
    
    case "medium":    
        if time_bound == 'yes': 
            print(f"{task}, is a {priority}, priority task that requires immediate attention today!.")
        else: 
            print(f"{task}, is a {priority}, priority task consider completing it as soon as possible.")
    
    case "low":
        if time_bound == 'yes':
            print(f"{task}, is a {priority}, priority task that requires immediate attention today!.")
        else:
            print(f"{task}, is a {priority}, priority task consider completing it when you have free time.")
    case _:
        print("One or more inputs are invalid!")

