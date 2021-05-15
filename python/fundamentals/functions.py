##Functions

#Lot of builtin functions
print("Hello World!")
str(3) == "3"
int("3") == 3

#use def keyword and () followed by :
def add_student(name, student_id):
    #create a dictionary/structure
    student = {"name": name, "student_id":student_id}
    students.append(student)


#default values for parameter
def add_student(name, student_id=3):
    #create a dictionary/structure
    student = {"name": name, "student_id":student_id}
    students.append(student)


#Variable arguments like print function
def var_args(name, *args):
    print(name)
    print(args)


#Variable arguments with description
def var_args_desc(name, **kwargs):
    print(name)
    print(kwargs["test"])
    print(kwargs["id"])

var_args("Srikanth",1,2,3,None,4,True,False)
var_args_desc("Srikanth", test="test123", id=3, extraarg=None, is_it=True)

add_student("Srikanth",1)
add_student("Ashwini",2)
add_student("Aditi",3)
add_student("Arjun",4)
