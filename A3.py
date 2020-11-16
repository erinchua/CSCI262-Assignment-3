import os, sys

def initialInput():
    commandArg = sys.argv
    currentDir = os.path.dirname(os.path.abspath(__file__))
    eventFileDir = os.path.join(currentDir, commandArg[1])
    statsFileDir = os.path.join(currentDir, commandArg[2])

    eventFile = open(eventFileDir, "r")
    statsFile = open(statsFileDir, "r")

    # print(eventFile.read() + "\n")
    # print(statsFile.read() + "\n")

    eventFileList = [item.split("\n") for item in eventFile.read().split("\n")]
    print(eventFileList)
    
    for i in range(len(eventFileList)):
        print(eventFileList[i])

    print("\n")
    statsFileList = [item.split("\n") for item in statsFile.read().split("\n")]
    print(statsFileList)
    
    for i in range(len(statsFileList)):
        print(statsFileList[i])
            

if __name__ == "__main__":
    initialInput()