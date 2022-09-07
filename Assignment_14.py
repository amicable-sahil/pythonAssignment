#Q1:-------------------------------------------------------------
n =int(input("Enter a number "))
i = 1
myList =[]
while i<=n:
    myList.append(i)
    i +=1
print(myList)


#Q2:-------------------------------------------------------------
n = int(input("Enter a number "))
i = 1
myList = []
while i <= 2*n:
    myList.append(i)
    i += 2
print(myList)


#Q3:-------------------------------------------------------------
n = int(input("Enter a number "))
i = 1
myList = []
while i <= 2*n:
    myList.append(i+1)
    i += 2
print(myList)


#Q4:-------------------------------------------------------------
l1 = [50, 45, 46, 25, 14, 24, 18, 34]
print(max(l1))


#Q5:-------------------------------------------------------------
l1 = [50, 45, 46, 25, 14, 24, 18, 34]
print(min(l1))


#Q6:-------------------------------------------------------------
l1 = [50, 45, 46, 25, 14, 24, 18, 34]
print(sum(l1))


#Q7:-------------------------------------------------------------
myList = [10, "Sahil", 3+4j, True, 4.5, "Wow", 14, False, 75]

for item in myList:
    if type(item) is not int:     # This condition only removing str and bool but not float and complex ?
        myList.remove(item)
print(myList)


#Q8:-------------------------------------------------------------
l1 = [50, 45, 46, 25, 14, 24, 18, 34, 50, 50, 25, 18, 25]
l2 = []
for item in l1:
    if item not in l2:
        l2.append(item)
        print("Element:",item,"count value:", l1.count(item))


#Q9:----------------------------PENDING---------------------------------
l1 = [50, 45, 46, 25, 14, 24, 18, 34, 50, 50, 25, 18, 25]
i = 0
for item in l1: 
    print("On index: [" + str(i) + "] the value is: '" + str(item) + "'")
    i +=1


#Q10:-------------------------------------------------------------
l1 = [50, 45, 46, 25, 14, 24, 18, 34, 50, 50, 25, 18, 25]
l1.sort()
print(l1)
