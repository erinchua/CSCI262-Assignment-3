import os, sys

commandArg = sys.argv
currentDir = os.path.dirname(os.path.abspath(__file__))
eventFileDir = os.path.join(currentDir, commandArg[1])
statsFileDir = os.path.join(currentDir, commandArg[2])
noOfDays = commandArg[3]

eventFile = open(eventFileDir, "r")
statsFile = open(statsFileDir, "r")

print(noOfDays + "\n" + eventFile.read() + "\n")
print(noOfDays + "\n" + statsFile.read() + "\n")
