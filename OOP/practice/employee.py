class Employee:
    def __init__(self, role, dept, salary):
        self.role = role
        self.dept = dept
        self.salary = salary

    def showDetails(self):
        print("role=", self.role)
        print("dept=", self.dept)
        print("salary=", self.salary)


class Engineer(Employee):
    def __init__(self, name, age):
        self.name = name
        self.age = age 
        super().__init__("Engineer", "IT", "75,000")

print("for employee...........")
e1 = Employee("accountant", "finance", "60,000")
e1.showDetails()

print("for engineer..............")
engg1 = Engineer("Elon Musk", 37)
engg1.showDetails()
