# #Q1:
# print("Positive" if int(input("Enter a number")) > 0  else "Negative")

# #Q2:
# print("Number is not divisible by 5" if int(input("Enter a number "))%5 else "Number is divisible by 5")

# #Q3:
# x = int(input("Enter a number"))
# print("Number is even" if x%2 == 0 else "Number is odd")

# #Q4:
# x = int(input("Enter first number"))
# y = int(input("Enter second number"))
# print(x if x>y else y)


# #Q5:
# str1 = input("Enter any word ")
# str2 = input("Enter any word ")
# if str1>str2:
#     print(str1, str2, sep="\n")
# else:
#     print(str2, str1, sep="\n")

# #new way =>  print((str2, str1) if str1>str2 else (str1, str2))



# #Q6:
# x= int(input("Enter a number"))
# if 99 < x < 1000 :
#     print("It is a three digit number", x)
# else:
#     print("It's not a three digit number")

# #Q7:
# x= int(input("Enter a number "))
# if x>0:
#     print("Number is positive")
# elif x<0:
#     print("Number is Negative")
# else:
#     print("Number is Zero")


# #Q8:
# print("Enter values of a, b and c of quadratic equation ")
# a, b, c = int(input()), int(input()), int(input())
# # distinct frmula =>  [ d = b**2 - 4*a*c ]
# d = b**2 - 4*a*c
# if d>0:
#     print("Real and distinct roots")
# elif d==0:
#     print("Real and equal roots")
# else:
#     print("Imaginary roots")


# #Q9:
# y = int(input("Enter any year "))
# if y % 100 == 0:
#     if y % 400 == 0:
#         print(y, "is a leap year")
#     else:
#         print(y, "is not a leap year")
# elif y % 4 == 0:
#     print(y, "is a leap year")
# else:
#     print(y, "is not a leap year")


# #Q 10:
# a = int(input("Enter first number "))
# b = int(input("Enter second number "))
# c = int(input("Enter third number "))
# if a>=b:
#     if a>=c:
#         print(a, "is greater")
#     else:
#         print(c, "is greater")
# else:
#     if b>=c:
#         print(b, "is greater")
#     else:
#         print(c, "is greater")

# #new way =>  print((a if a>c else c) if a>b else (b if b>c else c))



# #Q 11:
# m = int(input("Enter month "))
# if m == 1 or m == 3 or m == 5 or m == 7 or m == 8 or m == 10 or m == 12:
#     print("Days in this month are 31")
# elif m == 2:
#     print("Days in this month are 28/29")
# elif m == 4 or m == 6 or m == 9 or m == 11:
#     print("Days in this month are 30")
# else:
#     print("Enter a valid month")


# #Q 12:
# complexNumber = complex(input("Enter a complex number "))
# print(complexNumber.real  if complexNumber.real > complexNumber.imag else complexNumber.imag)