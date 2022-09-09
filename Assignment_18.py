# Q1:---------------------------------------------------------------
d1 = {"name": "Sahil", "Age": 30, "Gender": "Male", "Qualification": "BA Greduate"}
print(d1, type(d1))

# Q2:---------------------------------------------------------------
d1 = {"name": "Sahil", "Age": 30, "Gender": "Male",
      "Qualification": "BA Greduate"}
print(d1["name"], d1["Gender"], sep=" / ")


# Q3:---------------------------------------------------------------
d1 = {"name": "Sahil", "Age": 30, "Gender": "Male", "Qualification": "BA Greduate"}
[print(d1[k]) for k in d1]


# Q4:---------------------------------------------------------------
d1 = {"name": "Sahil", "Age": 30, "Gender": "Male", "Qualification": "BA Greduate"}
d1["name"] = "Rinku"
print(d1)


# Q5:---------------------------------------------------------------
d1 = {"name": "Sahil", "Age": 30, "Gender": "Male", "Qualification": "BA Greduate"}
[print(k) for k in d1]


#Q6:---------------------------------------------------------------
myDictonay = {"d1": {"name": "Sahil", "Age": 30, "Gender": "Male"}, "d2": {105: "Mala", 106: "Varsha", 108: "Deepak"}, "d3": {"Arijit": "Singer", "MySirG": "Teacher", "Remo": "Dancer"}}
print(myDictonay)
print()
print(myDictonay["d3"]["MySirG"])  # for accessing a perticular data value


# Q7:---------------------------------------------------------------
d1 = {"name": "Sahil", "Age": 30, "Gender": "Male"}
d2 = {105: "Mala", 106: "Varsha", 108: "Deepak"}
d3 = {"Arijit": "Singer", "MySirG": "Teacher", "Remo": "Dancer"}

d4 = {"dict1": d1, "dict2": d2, "dict3": d3}
print(d4)
print(d4["dict2"][108]) # for accessing a perticular data value


# Q8:---------------------------------------------------------------
l1 = [1,2,3,4]
l2 = ["Sahil", "Kashish", "Laxmi", "Rinku"]
print({ l1[i]:l2[i] for i in range(0, len(l1)) })


#Q9:---------------------------------------------------------------
d1 = {"name": "Sahil", "Age": 30, "Gender": "Male"}
d2 = {105: "Mala", 106: "Varsha", 108: "Deepak"}
for k in d2:
    d1[k] = d2[k]
print(d1)  # d2 merged in d1


#Q10:---------------------------------------------------------------
myDict = {"Java": 95, "Python": 45, "C++": 108, "Angular": 63}
k1 =[myDict[k] for k in myDict]
minK = min(k1)
for k in myDict:
    if myDict[k] == minK:
        print("The key for lowest data value is:", k)
