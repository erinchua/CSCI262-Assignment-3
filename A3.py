import os

currentDir = os.path.dirname(os.path.abspath(__file__))
eventFileDir = os.path.join(currentDir, 'Events.txt')
statsFileDir = os.path.join(currentDir, 'Stats.txt')

eventFile = open(eventFileDir, "r")
statsFile = open(statsFileDir, "r")


print(eventFile.read())
print(statsFile.read())
