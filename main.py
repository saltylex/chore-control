import employee as empclass

employee_codes = []
chores_done = 0
chores_wip = 0
chores_ns = 0
chores_total = 0

"""
CHORE CONTROL: a task manager
"""


def read_employee_data():
    global employee_codes
    with open('employees_codes.csv') as data:
        for employee in data:
            employee = employee.split(';')
            employee_codes.append(empclass.Employee(employee[0], int(employee[1])))
    data.close()


def read_chore_data():
    global employee_codes, chores_ns, chores_wip, chores_total, chores_done
    with open('tasks_codes.csv') as data:
        for task in data:
            task = task.split(';')
            for emp in employee_codes:
                if emp.check_employee(int(task[0])):
                    chores_total += 1
                    if int(task[2]) == 0:
                        chores_ns += 1
                    elif int(task[2]) == 1:
                        chores_wip += 1
                    else:
                        chores_done += 1
                    emp.add_chore((task[1], int(task[2])))
                    break
    data.close()


def start():
    read_employee_data()
    read_chore_data()
    name = input("Hello! Who are you?: ")
    if name != "Manager":
        print("Good for you. Goodbye!")
        exit(0)
    print("Welcome, Manager!")
    while True:
        print("MENU\n1. Show all employees\n2. Statistics\n3. Exit\n")
        try:
            option = int(input("Option: "))
        except ValueError:
            continue
        if option == 3:
            print(f"Goodbye, Manager!")
            exit(0)
        elif option == 1:
            for e in employee_codes:
                print(e)
        elif option == 2:
            print(
                f"Total chores: {chores_total}\nPercentage of completed chores: {round(chores_done / chores_total * 100, 2)}%\nPercentage of started chores: {round(chores_wip / chores_total * 100, 2)}%\nPercentage of not started chores: {round(chores_ns / chores_total * 100, 2)}%\n")
        else:
            print("Invalid option!")


start()
