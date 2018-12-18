import sys
#import argparse

red_flag = False
blue_flag = False
green_flag = False

player1_name = None
player2_name = None
player3_name = None

def argParser(arg, arg2 = None):
    print(arg)
    if arg == "-help" or arg == "-h":
        help()
    if arg == "-red":
        red_flag = True
        print("Red Flag Set On")
    if arg == "-blue":
        blue_flag = True
        print("Blue Flag Set On")
    if arg == "-green":
        green_flag = True
        print("Green Flag Set On")
    if "-player" in arg:
        setPlayer(arg, arg2)

def setPlayer(arg, name):
    name = name.title()
    if "1" in arg:
        player1_name = name
        print("Set Player 1's name to... ", player1_name)
    if "2" in arg:
        player2_name = name
        print("Set Player 2's name to... ", player2_name)
    if "3" in arg:
        player3_name = name
        print("Set Player 1's name to... ", player3_name)


def help():
    print("HELP MENU")
    print("help text here help text here help text here help text here")
    print("help text here help text here help text here help text here")
    print("help text here help text here help text here help text here")
    print("help text here help text here help text here help text here")


print("SCRIPT NAME: ", sys.argv[0])
print("NUMBER OF ARGUMENTS: ", len(sys.argv))
print("ARGUMENTS: ", str(sys.argv))

if(len(sys.argv)>2):
    argParser(str(sys.argv[1]), str(sys.argv[2]))
else:
    argParser(str(sys.argv[1]))
