#Q1:  -------------------- class with some properties  --------------------
class User:

    def __init__(self, name, age, email):
        self.name = name
        self.age = age
        self.email = email


#Q2:  -------------------- Create a class to greet the user  --------------------
class User:

    def __init__(self, name, age, email):
        self.name = name
        self.age = age
        self.email = email


    def greet(self):
        print("Hello", self.name)
        print("Welcome to python programming")


#Q3:  -------------------- Create a class and object of it  --------------------
class User:

    def __init__(self, name, age, email):
        self.name = name
        self.age = age
        self.email = email

    def greet(self):
        print("Hello", self.name)
        print("Welcome to python programming")

sahil = User("Sahil", 30, "sahilparihar137@gmail.com")
guest = User("Guest", 25, "guest@gmail.com")


#Q4:  -------------------- Create a class and assign default values by init  --------------------
class User:

    def __init__(self, name, age, email):
        self.name = name
        self.age = age
        self.email = email
        self.course = "Full Stack Development with Python"
        self.courseFee = 4000
        self.courseLang = "Hindi"

    def greet(self):
        print("Hello", self.name)
        print("Welcome to python programming")


sahil = User("Sahil", 30, "sahilparihar137@gmail.com")
guest = User("Guest", 25, "guest@gmail.com")


sahil.greet()
print("Your course is:",sahil.course)
print("Your course fee is:",sahil.courseFee)


#Q5:  -------------------- Create a class and delete a property of it  --------------------
class User:

    def __init__(self, name, age, email):
        self.name = name
        self.age = age
        self.email = email
        self.course = "Full Stack Development with Python"
        self.courseFee = 4000
        self.courseLang = "Hindi"

sahil = User("Sahil", 30, "sahilparihar137@gmail.com")

del sahil.email

print(sahil.name)
print(sahil.age)
print(sahil.email)  # This will gives error because email has been deleted for user sahil


#Q6:  -------------------- Create a class and assign default values by init  --------------------
class User:

    def __init__(self, name, age, email):
        self.name = name
        self.age = age
        self.email = email

    def compareAge(u1, u2, u3):
            if u1.age < u2.age:
                if u1.age < u3.age:
                    print(u1.name, "is youngest")
                elif u1.age > u3.age:
                    print(u3.name, "is the youngest")
                else:
                    print("Both", u1.name, "and", u3.name, "are equal and youngest")
            elif u2.age < u1.age:
                if u2.age < u3.age:
                    print(u2.name, "is the youngest")
                elif u2.age > u3.age:
                    print(u3.name, "is the youngest")
                else:
                    print("Both", u3.name, "and", u2.name, "are equal and youngest")
            else:
                if u1.age > u3.age:
                    print(u3.name, "is the youngest")
                elif u1.age < u3.age:
                    print("Both", u1.name, "and", u2.name, "are equal and youngest")
                else:
                    print("All are at same age")


sahil = User("Sahil", 30, "sahil@gmail.com")
preet = User("Preet", 20, "preet@gmail.com")
jashan = User("Jashan", 25, "jashan@gmail.com")

sahil.compareAge(preet, jashan)


#Q7:  -------------------- Create a class Laptop and make two methods --------------------

class Laptop:
    def __init__(self, brand, ram, cpu, hdd):
        self.brand = brand
        self.ram = ram
        self.cpu = cpu
        self.hdd = hdd

    def config(self):
        print("Laptop configuration is:")
        print("Brand:", self.brand)
        print("RAM:", self.ram)
        print("CPU:", self.cpu)
        print("HDD:", self.hdd)
        print()

lap1 = Laptop("Apple", 32, "i9", 1024)
lap2 = Laptop("Hp", 16, "i7", 2048)
lap3 = Laptop("Lenovo", 8, "i5", 512)

lap1.config()


#Q8:  -------------------- Create class objects and store them into a list --------------------

class Laptop:
    def __init__(self, brand, ram, cpu, hdd):
        self.brand = brand
        self.ram = ram
        self.cpu = cpu
        self.hdd = hdd

lap1 = Laptop("Apple", 32, "i9", 1024)
lap2 = Laptop("Hp", 16, "i7", 2048)
lap3 = Laptop("Lenovo", 8, "i5", 512)

l1 = [lap1.__dict__, lap2.__dict__, lap3.__dict__]
print(sorted(l1, key=lambda a: a["ram"]))


#Q9:  -------------------- Create class variable and instance variable --------------------

class Student:

    course = "Full Stack Web Development with Python"

    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

sahil = Student("Sahil", 30, "Male")

print("My name is", sahil.name)
print("and my course is", Student.course)


#Q10:  -------------------- Create class and make instance variable and input a feild --------------------

class Employee:
    def __init__(self, empid, name, salary):
        self.empid = empid
        self.name = name
        self.salary = salary
        self.feild = input("Enter your feild ")

    def showEmpData(self):
        print("Employee ID:", self.empid)
        print("Employee Name:", self.name)
        print("Employee Salary:", self.salary)
        print("Employee Feild:", self.feild)

sahil = Employee(1158154, "Sahil", 1000000)

sahil.showEmpData()