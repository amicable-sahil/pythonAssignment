#Q1:---------------------------------------------------------------------------------
month = int(input("Enter a month number"))
match month:
    case month if month in (1,3,5,7,8,10,12):
        print("There are 31 days in this month")
    case month if month in (4,6,9,11):
        print("There are 30 days in this month")
    case 2:
        print("There are 28 or 29 days in this month")
    case _:
        print("Enter a valid month number")

#Q2:-----------------------------------------------------------------------------------
print("1. Addition")
print("2. Subtraction")
print("3. Multiplication")
print("4. Division")
choice = int(input("Enter you choice "))
match choice:
    case 1:
        print("Enter two values ")
        a,b = int(input()), int(input())
        c = a+b
        print("Sum is: ", c)
    case 2:
        print("Enter two values ")
        a, b = int(input()), int(input())
        c = a-b
        print("Difference is: ", c)
    case 3:
        print("Enter two values ")
        a, b = int(input()), int(input())
        c = a*b
        print("Product is: ", c)
    case 4:
        print("Enter two values ")
        a, b = int(input()), int(input())
        c = a/b
        print("Division is: ", c)
    case _:
        print("Invalid chice")


# Q3:----------------------------------------------------------------------------------------
print("1. Isosceles Trangle")
print("2. Rightangle Trangle")
print("3. Equilateral Trangle")
print("4. Exit")
n= int(input("Enter number which shape you want to check "))
match n:
    case 1:
        print("Enter lenth of triangle's sides a, b and c: ")
        a, b, c = int(input()), int(input()), int(input())
        if a == b or a == c or b == c:
            print("This is an isosceles triangle")
        else:
            print("It's not an isosceles triangle")
    case 2:
        print("Enter lenth of triangle's sides a, b and c: ")
        a, b, c = int(input()), int(input()), int(input())
        if a**2 + b**2 == c**2 or a**2 + c**2 == b**2 or b**2 + c**2 == a**2:
            print("Right angle triangle")
        else:
            print("Not a right angle triangle")
    case 3:
        print("Enter lenth of triangle's sides a, b and c: ")
        a, b, c = int(input()), int(input()), int(input())
        if a == b == c:
            print("It is an equilateral triangle")
        else:
            print("It's not an equilateral triangle")
    case 4:
            exit()


#Q4:-----------------------------------------------------------------------
age = int(input("Enter your age "))
match age:
    case age if age >= 60:
            print("Senior citizen")
    case age if age >= 40:
            print("Experienced")
    case age if age >= 20:
            print("Young")
    case age if age >= 10:
            print("Teen")
    case age if age > 0:
            print("Kid")
    case _:
        print("Enter a valid age")



#Q5:------------------------------------------------------------------
num = int(input("Enter a number "))
match num:
    case num if num%2 == 0:
        print("Saurabh Sukhla")
    case num if num%2 and num<0:
        print("Prateek Jain")
    case num if num%2 and num>0:
        print("Aditya Choudhary")


# Q6:---------------------------------------------------------------
myString = (input("Enter any word ")).strip()
# strip() function removes unnecessary spaces at begining and at last
match myString:
    case myString if ' ' in myString:
        print("Multi word string")
    case myString if ' ' not in myString:
        print("Single word string")


#Q7:---------------------------------------------------------------
num = int(input("Enter a number "))
match num:
    case num if num>0:
        print("Positive")
    case num if num<0:
        print("Negative")
    case num if num == 0:
        print("Zero")


#Q8:---------------------------------------------------------------
str1 = input("Enter string first ")
str2 = input("Enter string second ")

match (str1, str2):
    case (str1, str2) if str1 == str2:
        print("Both are identical strings")
    case (str1, str2) if str1 > str2:
        print("{} comes after {}". format(str1, str2))
    case (str1, str2) if str1 < str2:
        print("{} comes after {}". format(str2, str1))


#Q9:------------------------------------------------------------------
year = int(input("Enter a year "))
match year:
    case year if year%400 == 0:
        print("Century leap year")
    case year if year%100 == 0 and year%400:
        print("Century non-leap year")
    case year if year%4 == 0:
        print("Non-Century leap year")
    case year if year%4:
        print("Non-Century non-leap year")

#Q10:----------------------------------------------------------------
favColor = input("Enter your favourite color ")
colorList = ["yellow", "blue", "ornage", "while", "black", "red"]
for mycolor in colorList:
    if mycolor in favColor:
        colorName = mycolor
        break
else:
    colorName = "other"

match colorName:
    case "yellow":
        print("Yellow - Monday")
    case "blue":
        print("Blue - Tuesday")
    case "orange":
        print("Orange - Wednesday")
    case "white":
        print("White - Thursday")
    case "black":
        print("Black - Friday")
    case "red":
        print("Red - Saturday")
    case "other":
        print("For Other colours - Sunday")
