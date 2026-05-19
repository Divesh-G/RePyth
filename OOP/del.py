class Student:
    def __init__(self, name):
        self.name = name
    
s1 = Student("Dibash")
del s1

class Account:
    def __init__(self, acc_no, acc_pass):
        self.acc_no = acc_no
        self.__acc_pass = acc_pass

    def reset_pass(self):
        print(self.__acc_pass)

acc1 = Account("123456", "abcdef")
print(acc1.acc_no)
print(acc1.reset_pass())


class Person:
    __name = "anonymous"

    def __hello(self):
        print("Hello Person")

    def welcome(self):
        self.__hello()

p1 = Person()
print(p1.welcome())