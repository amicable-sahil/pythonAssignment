#Q1:  -------------------- Create a class and some attributes in it  --------------------
class Profile:
    
    def __init__(self, name, age, email):
        self.name = name
        self.age = age
        self.email = email

std1 = Profile("Sahil", 30, "sahil@gmail.com")
std2 = Profile("Param", 31, "param@gmial.com")

print(std1.name)
print(std2.name)


#Q2:  -------------------- Create a class and some attributes with encapsulation  --------------------
class Profile:

    def __init__(self):
        self.name = ""
        self.age = None
        self.email = ""

    def get_name(self):
        return self.name

    def set_name(self, name):
        self.name = name

    def get_age(self):
        return self.age

    def set_age(self, age):
        self.age = age


    def get_email(self):
        return self.email

    def set_email(self, email):
        self.email = email
    


std1 = Profile()
std2 = Profile()

std1.set_name("Sahil")
std1.set_age(30)
std1.set_email("sahil@gmail.com")

std2.set_name("Param")
std2.set_age(31)
std2.set_email("param@gmail.com")

print(std1.get_name())
print(std1.get_age())
print(std1.get_email())
print()
print(std2.get_name())
print(std2.get_age())
print(std2.get_email())


#Q3:  -------------------- Create a class and some attributes with encapsulation  --------------------
class Profile:

    def __init__(self):
        self.name = ""
        self.__age = None
        self.__email = ""

    def get_name(self):
        return self.name

    def set_name(self, name):
        self.name = name

    def get_age(self):
        return self.age

    def set_age(self, age):
        self.age = age

    def get_email(self):
        return self.email

    def set_email(self, email):
        self.email = email


std1 = Profile()
std2 = Profile()

std1.set_name("Sahil")
std1.set_age(30)
std1.set_email("sahil@gmail.com")

std2.set_name("Param")
std2.set_age(31)
std2.set_email("param@gmail.com")


std1.name = "Rinku"
std1.__email = "spam"
std1.__age = 25


print(std1.get_name())
print(std1.get_age())  # Output is "30" not "25" which i gave from outside the method
print(std1.get_email())
print()
print(std2.get_name())
print(std2.get_age())
print(std2.get_email())


#Q4:  -------------------- Create a class and some attributes with encapsulation  --------------------
from sys import platform


class Profile:

    platform = "iNeuron"

    def __init__(self):
        self.name = ""
        self.__age = None
        self.__email = ""

    def get_name(self):
        return self.name

    def set_name(self, name):
        self.name = name

    def get_age(self):
        return self.age

    def set_age(self, age):
        self.age = age

    def get_email(self):
        return self.email

    def set_email(self, email):
        self.email = email

    @classmethod
    def get_class_variable(cls):
        return cls.platform


std1 = Profile()
std2 = Profile()

print(Profile.get_class_variable())
print(std1.get_class_variable())


#Q5:  -------------------- Create a class Calculator for addition and subtraction  --------------------
class Calculator:

    def __init__(self):
        self.a = 0
        self.b = 0

    def add(self, a, b):
        return a+b

    def subtraction(self, a, b):
        return a - b

obj1 = Calculator()
obj2 = Calculator()

print(obj1.add(5, 7))
print(obj2.add(6, 8))
print(obj2.subtraction(26, 8))
print(obj2.subtraction(4, 14))


#Q6:  -------------------- Inheritence  --------------------
class Calculator:

    def __init__(self):
        self.a = 0
        self.b = 0

    def add(self, a, b):
        return a+b

    def subtraction(self, a, b):
        return a - b


class Calculator_2 (Calculator):

    def product(self, a, b):
        return a * b

    def divide(self, a, b):
        return a/b

obj1 = Calculator_2()
obj2 = Calculator_2()

print(obj1.add(5, 7))
print(obj2.add(6, 8))

print(obj1.subtraction(26, 8))
print(obj2.subtraction(4, 14))

print(obj1.product(4,6))
print(obj2.product(3,7))

print(obj1.divide(30,6))
print(obj2.divide(21,7))


#Q7:  -------------------- Phone class with two methods  --------------------

class Phone:

    def __init__(self, name):
        self.name = name

    def calling(self):
        print("{}, You have a call".format(self.name))

    def sms(self):
        print("{}, You have a message".format(self.name))


user1 = Phone("Sahil")
user2 = Phone("Rinku")

user1.calling()
user1.sms()

user2.calling()
user2.sms()


#Q8:  -------------------- SmartPhone class with multiple inheritence  --------------------

class Phone:

    def __init__(self, name):
        self.name = name

    def calling(self):
        print("{}, You have a call".format(self.name))

    def sms(self):
        print("{}, You have a message".format(self.name))

class Calculator_2_1:

    def add(self, a, b):
        return a+b

    def subtraction(self, a, b):
        return a - b

    def product(self, a, b):
        return a * b

    def divide(self, a, b):
        return a/b


class SmartPhone (Phone, Calculator_2_1):

    def fun(self):
        pass

user1 = SmartPhone("rinku")


user1.calling()


#Q9:  -------------------- TrueCaller class --------------------

class TrueCaller:

    def __init__(self):
            self.name = ""
            self.number = None

    def fetch_name(self, num):
        if self.number == num:
            print(self.name)
        else:
            print("No data available")

    def add_new_contact(self, name, number):
        self.name = name
        self.number = number
    
user1 = TrueCaller()
user2 = TrueCaller()

user1.add_new_contact("Sahil", 7014301693)
user2.add_new_contact("Rinku", 7339972393)

user1.fetch_name(7014301693)
user2.fetch_name(7014301693)


#Q10:  -------------------- fetch TrueCaller class data in Smartphone class--------------------

class TrueCaller:

    def __init__(self):
        self.name = ""
        self.number = None

    def fetch_name(self, num):
        if self.number == num:
            print(self.name)
        else:
            print("No data available")

    def add_new_contact(self, name, number):
        self.name = name
        self.number = number


tc1 = TrueCaller()
tc2 = TrueCaller()

tc1.add_new_contact("Sahil", 7014301693)
tc2.add_new_contact("Rinku", 7339972393)


class SmartPhone ():

    def fun(self):
        pass

    def fetch_truecallermethof(self, tc, num):
        tc.fetch_name(num)


user1 = SmartPhone()
user1.fetch_truecallermethof(tc1, 7014301693)
user1.fetch_truecallermethof(tc2, 7339972393)
