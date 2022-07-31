class Employee:
    def __init__(self, n, c):
        if not isinstance(n, str):
            raise ValueError("Invalid name!")
        if not isinstance(c, int):
            raise ValueError("Invalid code!")
        self.__name = n
        self.__code = c
        self.__chores = []  # chores will be kept in tuples of the form (task, status)

    def __str__(self):
        s = ""
        s += f"EMPLOYEE #{self.__code}\nName: {self.__name}\nChores: "
        if len(self.__chores) == 0:
            s += "None.\n"
            return s
        s += '\n'
        for chore in self.__chores:
            if chore[1] == 1:  # WIP
                s += f"{chore[0]}. Status: Work in Progress\n"
            elif chore[1] == 2:  # complete
                s += f"{chore[0]}. Status: Complete\n"
            else:  # not started
                s += f"{chore[0]}. Status: Not Started\n"
        return s

    def check_employee(self, code):
        return code == self.__code

    def add_chore(self, ch):
        self.__chores.append(ch)

    @property
    def name(self):
        return self.__name

    @property
    def code(self):
        return self.__code

    @property
    def chores(self):
        return self.__chores
