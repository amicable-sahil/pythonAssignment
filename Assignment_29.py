#Q1.

f= open("fileHandeling.txt", "w")
f.write("This file is created for file handeling purpose")
f.close()
print("b. Is file closed:",f.closed)
print("c. The file opening mode is:",f.mode)
print("d. The name of the file is:",f.name)



#Q2.

with open("myfile.txt", "w") as f:
    f.write(input("Enter some text "))



#Q3.

with open("myfile.txt", "r") as f:
    text = f.read()
    print(text)



#Q4.

cities = ["Hanumangarh", "Ganganamgar", "Chandigarh", "Banglore"]
f = open('cities.txt', 'w')
for item in cities:
    f.write(item + " ")
f.close()



#Q5.


cities = ["Mumbai", "Gurugram", "Delhi", "Chennei"]
f = open('cities.txt', 'a')
for item in cities:
    f.write(item + " ")
f.close()



#Q6. 

def search(fileName, word):
    f = open(fileName, "r")
    line_num = 0
    for content in f.readlines():
        line_num +=1
        str_word = content.split(" ")
        word_num = 0
        for w in str_word:
            word_num +=1
            if w == word:
                found = "Word found at l({}) w({})".format(line_num, word_num)
                return found
    else:
        return "Word not found"

search_word = search("cities.txt", "Delhi")

print(search_word)



#Q7.    

def count_keywords(fileName):
    import keyword
    keyWordList = keyword.kwlist
    f = open(fileName, "r")
    text = f.read()
    count = 0
    for kword in keyWordList:
        if kword in text:
            count +=1
    f.close()
    print("Total keywords used in file are:", count)

count_keywords("demo3.py")


#Q8.

f = open("cities.txt", "r")
text = f.read()
f.close()

f= open("cities1.txt", "w")
f.write(text)
f.close()

f = open("cities1.txt", "r")
text = f.read()
print(text)
f.close()



#Q9.

bookData = {"Engilsh": 500, "Hindi": 350, "Punjabi": 200, "Maths": 600}
toyData = {"Car": 850, "ELephant": 600, "Cycle": 200, "Puzzle": 500}

import pickle

f = open("bookfile", "wb")
pickle.dump(bookData, f)
pickle.dump(toyData, f)
f.close()



#Q10.

f = open("bookfile", "rb")
data = pickle.load(f)
for key in data:
    print("Book name is:", key, "and Price is:", data[key])
f.close()