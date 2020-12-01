def makeNewFile(name):
    f = open(name + ".txt", "w+")

def ReadFile(filename):
    f = open(filename+".txt", "r")
    f1 = f.readlines()
    for x in  f1:
        print(x)
    print("_______________________________________________________________")
    f.close()

def AddTextInFile(filename):
    f = open(filename+".txt","a+")
    print("How many lines you want to add or \n how many names : \n ")
    numberOfLines = int(input())
    for i in range(numberOfLines):
        print("Line number : ",i+1)
        textToAdd = input()
        f.write(textToAdd + "\n")
    f.close()

def ClearAllTextFromFile(filename):
    f = open(filename+".txt","w")
    f.write(" ")

    f.close()


print("_____________________Welcome to List maker___________________")

listOn = True

while listOn:
    print("_________MENU___________")
    print("To make a new file enter 1")
    print("To read a file enter 2")
    print("To add text to file enter 3")
    print("To clear file data  enter 4")
    print("To exit enter 5")
    option = int(input())

    if (option == 1):
        print("Enter name for the new ")
        fileName = input()
        makeNewFile(fileName)
        print('\n \n The program will end to create a new file ,to edit rerun the script\n \n')
        listOn = False

    elif(option == 2):
        print("Enter the name of file (without file extension)")
        fileName = input()
        print("_________________________________________")
        ReadFile(fileName)

    elif(option == 3):
        print("++++++++++++++++++++++++++++++++==")
        print("Enter The File name to edit (creates a new one, if does not exit )")
        fileName = input()
        AddTextInFile(fileName)
        print("++++++++++++++++++++++++++++++++==")

    elif(option == 4):
        print("++++++++++++++++++++++++++++++++==")
        print("Enter the file name (creates a new one, if does not exit )")
        fileName = input()
        ClearAllTextFromFile(fileName)
        print("++++++++++++++++++++++++++++++++==")

    elif (option == 5):
        listOn = False

    else:
        print("Wrong Input , plz enter again")

