#Q1:---------------------------------------------------------
n = int(input("Enter a number "))
# range(beg, end, step) ---> by default 'beg' = 0   and   'step' = 1
r1 = range(n)
for a in r1:
    print("MySirG", end=" ")


#Q2:---------------------------------------------------------
n = int(input("Enter a number "))
r1 = range(n)     
for a in r1:
    print(a+1, end=" ")

#Q3:---------------------------------------------------------
for a in range(int(input("Enter a number ")), 0, -1):
    print(a, end=" ")



#Q4:---------------------------------------------------------
for a in range(1, 2*int(input("Enter a number "))+1, 2):
    print(a, end=" ")

#Q5:---------------------------------------------------------
for a in range(2*int(input("Enter a number "))-1, 0, -2):
    print(a, end=" ")


#Q6:---------------------------------------------------------
for a in range(2, 2*int(input("Enter a number "))+1, 2):
    print(a, end=" ")


#Q7:---------------------------------------------------------
for a in range(2*int(input("Enter a number ")), 1, -2):
    print(a, end=" ")


#Q8:---------------------------------------------------------
for a in range(int(input("Enter a number "))):
    print((a+1)**2, end=" ")


#Q9:---------------------------------------------------------
for a in range(int(input("Enter a number "))):
    print((a+1)**3, end=" ")


#Q10:---------------------------------------------------------
n = int(input("Enter a number "))
for a in range(10):
    print((a+1)*n, end=" ")