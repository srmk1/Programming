##File operations

##File read
def read_file():
    try:
        f = open("Students.txt", "r")
        for student in f.readlines():
            print(student)
        f.close()
    except Exception:
        print("Could not read file")


##File append
def save_file(student):
    try:
        f = open("Students.txt", "a")
        f.write(student + "\n")
        f.close()
    except Exception:
        print("Could not append file")

##File read
def read_file():
    text_file = open("read_file.py")
    line_num = 0
    for line in text_file.readlines():
        print(str(line_num) + ": " + line.strip("\n\r"))
        line_num += 1

read_file()
