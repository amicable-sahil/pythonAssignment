#Q1:  -------------------- script to create an Arithmatic error  --------------------

a = 2
b = 0
c = a/b
print(c)



#Q2:  -------------------- script to create a Value error  --------------------

a = 2
b = "sahil"
c = a/b
print(c)



#Q3:  -------------------- script to handle an Arithmatic error  --------------------

a = 2

try:
    b = int(input("Enter a number "))
    c = a/b
except ZeroDivisionError:
    print("Number cannnot be divisible by zero")
else:
    print(c)



#Q4:  -------------------- script to handle a Value error  --------------------

a = 2

try:
    b = int(input("Enter a number "))
    c = a/b
except ValueError:
    print("Enter a valid number")
else:
    print(c)



#Q5:  -------------------- script to handle multiple exception in one try  --------------------

a = 10

try:
    b = int(input("Enter a number "))
    c = a/b
except ZeroDivisionError:
    print("Number cannnot be divisible by zero")
except ValueError:
    print("Enter a valid number")
except Exception:
    print("Are you dumb")
else:
    print(c)



#Q6:  -------------------- create a calculator and handle multiple exceptions  --------------------

try:
    num1 = eval(input("Enter first number "))
    num2 = eval(input("Enter second number "))

    sum = num1 + num2
    print("Sum of two numbers is",sum)

    sub = num1 - num2
    print("Subtraction of two numbers is",sub)

    mul = num1 * num2
    print("Multiplication of two numbers is",mul)

    div = num1 / num2
    print("Division of two numbers is",div)

except ValueError:
    print("Please enter valid values")
except ZeroDivisionError:
    print("Number cannot be divisible by zero")
except Exception:
    print("I'll handle all this")



#Q7:  -------------------- add finally block in above code  --------------------

try:
    num1 = eval(input("Enter first number "))
    num2 = eval(input("Enter second number "))

    sum = num1 + num2
    print("Sum of two numbers is",sum)

    sub = num1 - num2
    print("Subtraction of two numbers is",sub)

    mul = num1 * num2
    print("Multiplication of two numbers is",mul)

    div = num1 / num2
    print("Division of two numbers is",div)

except ValueError:
    print("Please enter valid values")
except ZeroDivisionError:
    print("Number cannot be divisible by zero")
except Exception:
    print("I'll handle all this")
finally:
    print("Program is completed succusfully")


#Q8:  -------------------- script for try, except and else --------------------

try:
    a = int(input("Enter first number "))
    b = int(input("Enter second number "))
    c = a/b
except ZeroDivisionError:
    print("Number cannnot be divisible by zero")
except ValueError:
    print("Enter a valid number")
except Exception:
    print("Are you dumb")
else:
    print(c)



#Q9:  -------------------- script to handle multiple exception in one try  --------------------

try:
    a = int(input("Enter first number "))
    b = int(input("Enter second number "))
    if a == b:
        raise ArithmeticError()
    c = a/b

   
except ZeroDivisionError:
    print("Number cannnot be divisible by zero")
except ArithmeticError:
    print("Numbers cannot be same") 
except ValueError:
    print("Enter a valid number")
except Exception:
    print("Are you dumb")
else:
    print(c)


#Q10:  -------------------- Nested try-except block --------------------

try:
    a = int(input("Enter first number "))
    b = int(input("Enter second number "))
    try:
        c = a/b
    except ZeroDivisionError:
        print("Number cannnot be divisible by zero")
    except ArithmeticError:
        print("Numbers cannot be same") 
    except ValueError:
        print("Enter a valid number")
    except Exception:
        print("Are you dumb")
    else:
        print("Division is", c)
    finally:
        print("Inner finally")
except ValueError:
    print("Please enter valid values")
else:
    print("Outer else")
finally:
    print("Outer finally")