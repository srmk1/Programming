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
