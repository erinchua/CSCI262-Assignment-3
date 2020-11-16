import os, sys

def initialInput():
    commandArg = sys.argv
    currentDir = os.path.dirname(os.path.abspath(__file__))
    eventFileDir = os.path.join(currentDir, commandArg[1])
    statsFileDir = os.path.join(currentDir, commandArg[2])
    noOfDays = commandArg[3]

    eventFile = open(eventFileDir, "r")
    statsFile = open(statsFileDir, "r")

    eventFileList = eventFile.read().split("\n")

    print(eventFileList)        

    for i in range(len(eventFileList)):
        splitByColon = eventFileList[i].split(":")
        print(splitByColon)
    # print(noOfDays + "\n" + eventFile.read() + "\n")
    # print(noOfDays + "\n" + statsFile.read() + "\n")


if __name__ == "__main__":
    initialInput()