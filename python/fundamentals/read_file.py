def read_file():
    text_file = open("read_file.py")
    line_num = 0
    for line in text_file.readlines():
        print(str(line_num) + ": " + line.strip("\n\r"))
        line_num += 1


read_file()
