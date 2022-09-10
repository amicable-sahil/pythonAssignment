#Q1:  -------------------- Function to Print Unique List  --------------------
def uniqueList(argList):
    newSet = (set(argList))
    newList = list(newSet)
    print(newList)

myList = [12, 25, "Hello", 25, 45, "Hello", 12, 20]
uniqueList(myList)


#Q2:  -------------------- Function to find prime number  --------------------
def checkPrimeNumber(num):
    if num>1:
        for e in range(2, 10):
            if e != num and num%e == 0:
                print("number is not prime")
                break
        else:
            print("number is prime")
    else:
        print("Number should be greater than 1")

checkPrimeNumber(9)
checkPrimeNumber(3)
checkPrimeNumber(2)
checkPrimeNumber(0)


#Q3:  -------------------- Function to print even numbers from list  --------------------
def evenNumber(aList):
    l2 = []
    for e in aList:
        if e%2 ==0:
            l2.append(e)
    print(l2)

myList = [45,25,64,24,15,78,15,26]
evenNumber(myList)


#Q4:  -------------------- Function to check palindrome string  --------------------
def checkPalindrome(str1):
    str2 = str1[::-1]
    print("Palindrome" if str1 == str2 else "Not Palindrome")

checkPalindrome("mom")
checkPalindrome("Hurry")
checkPalindrome("step on no pets")
checkPalindrome("15051")


#Q5:  -------------------- Function to check palindrome string  --------------------
def checkMin(a, b, c):
    d = min(a, b, c)
    print("Minimum value is", d)

checkMin(45,24,15)


#Q6:  -------------------- ?????????????????  --------------------
def squareNums():
    square_list = []
    for e in range(2,30):
        square_list.append(e**2) 
    print(square_list)

squareNums()


#Q7:  -------------------- Recursive Function  --------------------
# Example 1:
def sumOfnNumbers(n):
    if n==1:
        return 1
    return sumOfnNumbers(n-1) + n

print(sumOfnNumbers(10))


 # Example 2:
def print_N_Numbers(n):
    if n>0:
        print_N_Numbers(n-1), print(n)

print_N_Numbers(10)


#Q8:  -------------------- Function to count upper and lower case  --------------------
def counCase():
    str1 = input("Enter a string ")
    countUpper = 0
    countLower = 0
    for e in str1:
        if e.upper() == e and e != " ":
            countUpper += 1
        elif e.lower() == e and e != " ":
            countLower +=1
    print("Total number of uppercase are:", countUpper)
    print("Total number of lowercase are:", countLower)

counCase()


#Q9:  -------------------- Function to check Pangram  --------------------
def checkPangram():
    alpha = "abcdefghijklmnopqrstuvwxyz"
    str1 = input("Please enter a string ")
    for e in alpha:
        if e not in str1.lower():
            print("Entered string is not a pangram")
            break
    else:
        print("Entered string is a pangram")


checkPangram()


#Q10:  -------------------- Function to check Anagram  --------------------
def checkAnagram():
    print("Enter two strings to check anagram")
    str1, str2 = input(), input()
    s1, s2 = str1.lower(), str2.lower()
    sort_str1 = sorted(s1)
    sort_str2 = sorted(s2)
    if len(str1) == len(str2):
        if sort_str1 == sort_str2:
            print("'{}' and '{}' are Anagram". format(str1, str2))
        else:
            print("'{}' and '{}' are not Anagram". format(str1, str2))
    else:
        print("'{}' and '{}' are not Anagram". format(str1, str2))

checkAnagram()

