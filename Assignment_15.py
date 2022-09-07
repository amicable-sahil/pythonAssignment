#Q1:-------------------------------------------------------------
s1 = "Abc"
s2 = """I am a boy"""
s3 = '452'
s4 = '''"Teacher's Day"'''
s5 = 1254
print(s4)
print(str(s5), "type:", type(str(s5)))


#Q2:-------------------------------------------------------------
myStr = 'iNeuron'
print(myStr[:5])


#Q3:-------------------------------------------------------------
myStr = 'Hello Learners'
print(myStr[2:7])


#Q4:-------------------------------------------------------------
a = 'Python'
b = 'Learners'
print(a+ " " +b)


#Q5:-------------------------------------------------------------
myStr = 'iNeuron'
count = 0
for e in myStr:
    count +=1
print("Total number of characters in " + myStr + " are", count)


#Q6:-------------------------------------------------------------
myStr = 'iNeuron'
print(myStr[::-1])


#Q7:-------------------------------------------------------------
myStr = 'He is a hero for his father'
print("he" in myStr)


#Q8  &  Q9:-------------------------------------------------------------
s1 = "123456"
s2 = "5sadc4s465s"
s3 ="rohan"
print(s1.isalnum())
print(s1.isdigit())
print(s1.isalpha())
print(s2.isalnum())
print(s2.isdigit())
print(s2.isalpha())
print(s3.isalnum())
print(s3.isdigit())
print(s3.isalpha())


#Q10:-------------------------------------------------------------
s = 1245
i = str(s)
print(type(i))