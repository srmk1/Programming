## ————————————————————————————————————————————————————————————————————————————————————————————————
## Lists: 
## - List can contain non-homogenous entries (unlike array of C)
## - List can indexed negatively to start from end
## - Lists can be appended, deleted based on index and values
## - Lists can be sliced i.e. select only few entries from list
## - You can list of list of lists and so on
## - Lists are usually used when the order of your data items matters, so that you can refer them using numeric index
## - Although, lists of mixed data types are possible, lists are most appropriate where you’re collecting data items of the same type
## 
## 
## 
## 
## 
## - nephews = ["Huey","Dewey","Louie"]
## - Indexing
## 	nephews[0]
## 	nephews[2]
## 	nephews[-1] - last element
## - Length of lists
## 	len(nephews)
## - Appending to list
## 	nephews.append(‘Donald’) OR
## 	nephews.extend(['May Duck','June Duck']) OR
## 	ducks = nephews + ['Donald Duck','Daisy Duck']
## - Insert into specific index
## 	nephews.insert(0,'Scrooge McDuck')
## - Delete an element by index
## 	del nephews[0]
## 	del nephews[-1]
## - Delete by value in the lists
## 	nephews.remove('Donald Duck')
## - Sort an list
## 	nephews.sort()
## - Slicing a list
## 	squares[0:2]	=> From 0 till index 2
## 	squares[1:3]	=> From 1 till index 3
## 	squares[:3]	=> From 0 till index 3 OR first 3 elements
## 	squares[1:]	=> From 1 till end of list
## 	squares[:]		=> From 0 till end of list
## 	squares[-3:-1]	=> From last one till last but three 
## - Modifying slices of lists
## 	squares[2:4] = ['4','9']		=> Replace multiple elements of lists
## 	del squares[-2:]			=> Delete from last but second till last
## - Getting index of elements in lists:
## 	for index, value in enumerate(squares):
##     		print("Element",index,"->",value)
## - List of lists
## 	tlas = [ 
##         #Name       num_of_tlas     enabled
##         ["nug",     4,              True],
##         ["Fec",     2,              True],
##         ];
## - Remove duplicate from a list
## 	- Convert the list to python construct “set” (which can contain only unique values)
## 		- It will remove duplicates
## 	- Convert the set back to list
## 	word_unique = list(set(words))
## ————————————————————————————————————————————————————————————————————————————————————————————————
## Dictionary:
## - Dictionaries lets you associate names with data and they’re most natural to use where data items can be given unique labels 
## - They’re most appropriate to collect data items of different kinds 
## - Syntax of dictionary:
## 	{ key:value, key1:value1,… so on }
## 
## 
## 
## 
## 
## - capitals = {'United States': 'Washington, DC','France': 'Paris','Italy': 'Rome'}
## - Indexing
## 	capitals[‘Italy’]
## - Adding an element
## 	capitals[‘Spain’] = ‘Madrid’
## - Updating dictionary
## 	more_capitals = { ‘Germany’: ‘Berlin’, ‘United Kingdom’: ‘London’ }
## 	capitals.update(more_capitals)
## - Deleting an element in dictionary
## 	del capitals[‘Germany’]
## - Looping through:
## 	for key in capitals:
## 		print(key, capitals[key])
## - Looping through using keys()
## 	for key in capitals.keys():
## 		print(key)
## - Looping through using values()
## 	for value in capitals.values():
## 		print(value)
## - Looping through using items():
## 	for key, value in capitals.items():
## 		print(key, value)
## ————————————————————————————————————————————————————————————————————————————————————————————————
## Comprehensions:
## - For loops/if conditionals on each element of list OR dictionary can be written in compact readable format called Comprehension
## - Comprehensions are a concise and expressive way to write a data transformation
## - They are quick to write, easy to parse and are surpassingly powerful
## 
## 
## 
## 
## 
## - Inlining for loop inside lists
## 	squares = [i**2 for i in range(10)]
## - Inlining for loop and if conditionals inside lists
## 	squares_divisible_by_3 = [i**2 for i in range(10) if i % 3 == 0]
## - Inlining for loop and if conditionals inside dictionary
## 	squares3_dict = { i: i**2 for i in range(10) if i % 3 == 0 }
## - Inlining lists and comprehensions inside built in function
## 	sum(i**2 for i in range(10))
## 
## Examples:
## - Remove “\n” at the end of all strings in list, convert it into lowercase.. for all words in wordlist[]
## 	word clean = [word.strip().lower() for word in wordlist)
## - Guess what this does
## 	wordclean = sorted(list(set([word.strip().lower() for word in open('words','r')])))
## 	- Opens file words in read mode
## 	- Read words to a list
## 	- Remove duplicates by converting it into a “set” and back to “list”
## 	- Sorts it in alphabetical order
## ————————————————————————————————————————————————————————————————————————————————————————————————
## File Operations:
## - Opening a file
## 	word = open('words','r')
## - Read operations
## 	- Read all contents into one big string
## 		word_string = word.read()
## 	- Read one line of the file to a string
## 		word_string = word.readline()		
## 	- Read separate lines of files into a list
## 		word_list = word.readlines()
## - Write Operations
## 	- Write a string to file
## 		word.write(“Welcome to file”)
## 	- Write a list of lines to a file
## 		word.writelines(word_list)
## - Close operation
## 	- file.close()
## - Print first ten lines of the file
## 	print(wordlist[:10])
## ————————————————————————————————————————————————————————————————————————————————————————————————
## String operations:
## - Strip terminal “\n”
## 	“Aditi\n”.strip() => “Aditi”
## - Sort the characters of string
## 	sorted(“Aditi”) => ['A', 'd', 'i', 'i', ’t]
## - Sort the characters of string and place it back in string
## 	‘’.join(sorted(“Aditi”))
## - Captalize all letter in string
## 	“Aditi”.captialize()
## - Replace all “i” in a word to “e”
## 	“Ashwini”.repalce(‘i’,’e’)
## - Split string separated by a delimiter to a list
## 	"Some, csv, values".split(",") == ["Some", "csv", "values"]
## - Check if string is alphanumeric or digit
## 	“Srikanth”.isalpha() => True
## 	“Srikanth”.isdigit() => False
## 	“123”.isalpha() => False
## 	“123”.isdigit() => True
## ————————————————————————————————————————————————————————————————————————————————————————————————
## 
## 
## 
## 
## 
## 
## 
## 
## 
## 
## 
## 
## 
print("Hello World")
myint = 42
mystring = "Srikanth" \
           "How" \
           "a" \
           "Strange" \
           "String"
print(myint)
print(mystring)

"Srikanth".capitalize()
"Srikanth".replace("e", "a")
"Srikanth".isalpha() == True
"Srikanth".isdigit() == True
"Some, csv, values".split(",") == ["Some", "csv", "values"]

name = "Srikanth"
machine = "Python3"
print("Nice to meet you {0}. I am {1}".format(name, machine))
print(f"Nice to meet you {name}. I am {machine}")

python_true = True
python_false = False
int(python_true) == 1
int(python_false) == 0
str(python_true) == "True"

#Python uses identation for curly braces
if python_true:
    print("python_true is defined and true")

if python_false or python_true:
    print("Either one is true")

if python_true and python_false:
    print("Both are true")

#Arrays
student_name = ["Srikanth", "Ashwini", "Aditi", "Arjun"]
student_name[0] == "Srikanth"
student_name[1] == "Ashwini"
student_name[-1] == "Arjun" #last element
#student_name[4] = "Ananth" #No cannot do this
student_name.append("Ananth")
"Srikanth" in student_name == True
len(student_name) == 5
del student_name[2] #Aditi is no longer in list and other strings will shift left

student_name = ["Srikanth", "Ashwini", "Aditi", "Arjun"]
student_name[1:] == ["Ashwini", "Aditi", "Arjun"] #first is slice is removed
student_name[1:-1] == ["Ashwini", "Aditi"] #first and last element is sliced out

#for loop
for student in student_name:
    print(student)

for index in range(10):
    print(index)

for index in range(11,15):
    print(index)

for index in range(16, 26, 2):
    print(index)

for stundent in student_name:
    if stundent == "Aditi":
        break
    if student == "Srikanth":
        continue
    print(stundent)

#while loop
x = 0
while x < 10:
    print("Count is {0}".format(x))
    x += 1

#Dictionary: (Key, Value)
#Useful for structured data
#Easy to convert them to JSON
Student = {
    "Name": "Srikanth",
    "Age": 35,
    "DOB": "15/04/1982"
}
print(Student)

All_Students = [
    {"id": 123, "name": "Srikanth" },
    {"id": 124, "name": "Ashwini"},
    {"id": 125, "name": "Arjun"},
    {"id": 126, "name": "Aditi"}
]
print(All_Students[0])
print(All_Students[1]["id"])
print(All_Students[2]["name"])
print(All_Students[3])

print(All_Students[0].keys())
print(All_Students[1].values())

#Exception handling
#If dont handle exceptions and
# python encounters exception it stops executing there
All_Students[0]["last_name"] = "MK"
try:
    last_name1 = All_Students[0]["last_name"]
    numbered_last_name = last_name1 + 3
except KeyError:
    print("Error finding last name")
except Exception:
    print("Unknown Error!!")

print('This code does not print exception since it is already handled')
		      
print("Hello World")
myint = 42
mystring = "Srikanth" \
           "How" \
           "a" \
           "Strange" \
           "String"
print(myint)
print(mystring)

"Srikanth".capitalize()
"Srikanth".replace("e", "a")
"Srikanth".isalpha() == True
"Srikanth".isdigit() == True
"Some, csv, values".split(",") == ["Some", "csv", "values"]

name = "Srikanth"
machine = "Python3"
print("Nice to meet you {0}. I am {1}".format(name, machine))
print(f"Nice to meet you {name}. I am {machine}")

python_true = True
python_false = False
int(python_true) == 1
int(python_false) == 0
str(python_true) == "True"

#Python uses identation for curly braces
if python_true:
    print("python_true is defined and true")

if python_false or python_true:
    print("Either one is true")

if python_true and python_false:
    print("Both are true")

#Arrays are called as Lists
#List are created using square brackets []
#List can contain hetrogenous elements
#String methods: Append
empty_string = []
student_name = ["Srikanth", "Ashwini", "Aditi", "Arjun", True, None, 1]
student_name[0] == "Srikanth"
student_name[1] == "Ashwini"
student_name[-1] == "Arjun" #last element
#student_name[4] = "Ananth" #No cannot do this
student_name.append("Ananth")
"Srikanth" in student_name == True
len(student_name) == 5
del student_name[2] #Aditi is no longer in list and other strings will shift left

student_name = ["Srikanth", "Ashwini", "Aditi", "Arjun"]
student_name[1:] == ["Ashwini", "Aditi", "Arjun"] #first is slice is removed
student_name[1:-1] == ["Ashwini", "Aditi"] #first and last element is sliced out

#for loop
for student in student_name:
    print(student)

for index in range(10):
    print(index)

for index in range(11,15):
    print(index)

for index in range(16, 26, 2):
    print(index)

for stundent in student_name:
    if stundent == "Aditi":
        break
    if student == "Srikanth":
        continue
    print(stundent)

#while loop
x = 0
while x < 10:
    print("Count is {0}".format(x))
    x += 1

#Dictionary: (Key, Value)
#Is created using empty braces
#Useful for structured data
#Easy to convert them to JSON
empty_dictionary = {}
Student = {
    "Name": "Srikanth",
    "Age": 35,
    "DOB": "15/04/1982"
}
print(Student)

All_Students = [
    {"id": 123, "name": "Srikanth" },
    {"id": 124, "name": "Ashwini"},
    {"id": 125, "name": "Arjun"},
    {"id": 126, "name": "Aditi"}
]
print(All_Students[0])
print(All_Students[1]["id"])
print(All_Students[2]["name"])
print(All_Students[3])

print(All_Students[0].keys())
print(All_Students[1].values())

#Exception handling
#If dont handle exceptions and
# python encounters exception it stops executing there
All_Students[0]["last_name"] = "MK"
try:
    last_name1 = All_Students[0]["last_name"]
    numbered_last_name = last_name1 + 3
except KeyError:
    print("Error finding last name")
except Exception:
    print("Unknown Error!!")

print('This code does not print exception since it is already handled')

#import statements
import math
from math import factorial
from math import factorial as fac

print(fac(6))
