import os, sys

def initialInput():
    commandArg = sys.argv
    currentDir = os.path.dirname(os.path.abspath(__file__))
    eventFileDir = os.path.join(currentDir, commandArg[1])
    statsFileDir = os.path.join(currentDir, commandArg[2])
    noOfDays = commandArg[3]

    eventFile = open(eventFileDir, "r")
    statsFile = open(statsFileDir, "r")

    print(eventFile.read() + "\n")
    print(statsFile.read() + "\n")

    # eventFileList = eventFile.read().split("\n")

    # for i in range(len(eventFileList)):
    #     splitByColon = eventFileList[i].split(":")
    #     print(splitByColon)

if __name__ == "__main__":
    initialInput()