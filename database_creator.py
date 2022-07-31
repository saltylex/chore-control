import random as rand
import os

names = ["Jennifer", "Sylvie", "Mirelle", "Izabella", "John", "Peter", "Gregory", "Jeffrey", "Clay", "Christopher",
         "Melanie", "Amber", "Benny", "Ash", "Bay", "Harper", "Kai", "Rue", "Blossom", "Gerda", "Nat"]

surnames = ["Julien", "Henry", "Merline", "Paddington", "Gherkin", "Copperfield", "Washington", "Johnson", "Cohen",
            "Gomez", "Nagato", "Stark", "Murmann", "Zimmermann", "Zucker", "Sander"]

tasks = ["Create a new database", "Bring coffee to office", "Deliver financial report", "Fix the bugs in your project",
         "Brainstorm for the new project"]


def create_employee_file():
    global names, surnames
    if os.path.exists(R"C:\Users\lexig\PycharmProjects\choreControl\employees_codes.csv"):
        return
    with open('employees_codes.csv', 'a') as emp_file:
        for i in range(1000, 1100):
            emp_file.write(rand.choice(names) + ' ' + rand.choice(surnames) + ';' + str(i) + '\n')
        emp_file.close()


def create_task_file():
    global tasks
    if os.path.exists(R"C:\Users\lexig\PycharmProjects\choreControl\tasks_codes.csv"):
        return
    with open('tasks_codes.csv', 'a') as tsk_file:
        for i in range(50):
            tsk_file.write(
                str(rand.randint(1000, 1100)) + ';' + rand.choice(tasks) + ';' + str(rand.randint(0, 2)) + '\n')
        tsk_file.close()


if __name__ == "__main__":
    create_employee_file()
    create_task_file()
