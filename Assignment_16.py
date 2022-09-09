# Q1:---------------------------------------------------------------
t = ("Java", "Python", "SQL", "C")
print(t, type(t))


# Q2:---------------------------------------------------------------
t = (10,)
print(t, type(t))


# Q3:---------------------------------------------------------------
t = ("Java", "Python", "SQL", "C")
t = t[::-1]
print(t)

# Q4:---------------------------------------------------------------
t1 = ("Java", "Python", "SQL", "C")
t2 = 1,2,3,5
temp = t1
t1 = t2
t2 = temp
print(t1, t2, sep="\n")


# Q5:---------------------------------------------------------------
t1 = ("Java", "Python", "SQL", "C")
t2 = 1, 2, 3, 5
t3 = ("Java", "Python", "C", "SQL")

print(t1 == t2)
print(t1 == t3)
print(t1 != t2)


# Q6:---------------------------------------------------------------
t1 = ("Java", "Python", "SQL", "C")
a,b,c,d = t1
print(a, b, c, d)


# Q7:---------------------------------------------------------------
t1 = (1,2,3,4,5)
t2 = (t1[3], t1[4])
print(t2)

# Q8:---------------------------------------------------------------
t1 = (("a", 25), ("c", 15), ("d", 20), ("b", 45))
t1 = (e[::-1] for e in t1)
print(sorted(t1))


# Q9:---------------------------------------------------------------
t1 = ("Python", [10, 20, 30], (2, 4, 16))
print(t1[1][1])

# Q10:---------------------------------------------------------------
t1 = (11, [22, 33], 44, 55)
t1[1][0] = 222   # we can't edit a tuple value but we can edit a list value in tuple
print(t1[1][0])
