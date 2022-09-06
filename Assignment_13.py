#Q1:-------------------------------------------------------
l1 = ["Java", "Python", "SQL", "C"]
print(l1)


#Q2:-------------------------------------------------------
l1 = []
print(type(l1))


#Q3:-------------------------------------------------------
myList = ["Java", "Python", "SQL", "C"]
print(myList[-1])


#Q4:-------------------------------------------------------
myList = ["Java", "Python", "SQL", "C", "Reactnative", "JavaScript"]
myList[2], myList[-1] = "NoSQL", "Flutter"
print(myList)


#Q5:-------------------------------------------------------
myList = ["Java", "SQL", "C", "Reactnative", "JavaScript"]
myList.append("Python")
print(myList)


#Q6:-------------------------------------------------------
firstlist = ["Java", "Python", "SQL"]
secondlist = ["C", "Cpp", "NoSQL"]
firstlist = firstlist + secondlist
print(firstlist)


#Q7:-------------------------------------------------------
thisList = ["Java", "SQL", "C", "Reactnative", "Javascript", "Python"]
i= 0
n = len(thisList)
while i<n:
    print(thisList[i], sep=",", end=" ")   # sep="," function is not working here
    i +=1


#Q8:-------------------------------------------------------
thisList = ["Java", "SQL", "C", "Reactnative", "Javascript", "Python"]
list2 = sorted(thisList)
print(list2)


#Q9:-------------------------------------------------------
print("How many cities you want to enter ")
n = int(input())
print("Enter city names")
myList = []
i = 0
while i<n:
    city = str(input())
    myList.append(city)
    i +=1
print(myList)


#Q10:-------------------------------------------------------
print("How many numbers you want to enter ")
n = eval(input())
print("Enter", n, "numbers")
myList = []
i = 0
while i < n:
    num = int(input())
    myList.append(num)
    i += 1
print(myList)
