# overall flaw in this implementation was made at the planning stage
# using sys.arg to parse this could not allow me to use inherit windows command
# line arguments like > or - so i had to create my own flags and system for
# arguments. this would have been remedied by using argparse library
# which would allow me to handle built in command line arguments


# cat.py
# concatenates files
import sys

files = []
write_file = None
write_file_obj = None

# flags
flag_E = False
flag_n = False


def argParser(args):
    global write_file
    global flag_E
    global flag_n
    for arg in args:
        # script name
        if ".py" in str(arg):
            continue
        # files
        if ".txt" in str(arg):
            files.append(str(arg))
            print("File added! ... ", str(arg))
        if "E" in str(arg):
            flag_E = True
        if "n" in str(arg):
            flag_n = True
        if "=" in str(arg):
            write_file = str(args[-1])
            print("Write destination added! ... ", write_file)
            break
    print("asd")
    concatenate()

def concatenate():
    file_num = 0
    for file in files:
        read_file_obj = open(file, 'r')
        for line in read_file_obj:
            printLine(line, file_num)
            file_num += 1
            if write_file != None:
                writeToFile(line)

def printLine(line, number):
    if flag_n == True:
        print(number, " ", line)
        return
    if flag_E == True:
        print(line[:-1], "$")
        return
    print(line)

def writeToFile(line):
    global write_file_obj
    if write_file_obj == None:
        write_file_obj = open(write_file, 'w')
    write_file_obj.write(line)



print("SCRIPT NAME: ", sys.argv[0])
print("NUMBER OF ARGUMENTS: ", len(sys.argv))
print("ARGUMENTS: ", str(sys.argv))

argParser(sys.argv)
