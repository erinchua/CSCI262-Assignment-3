import os, sys
import scipy.stats as stats
import matplotlib.pyplot as plt
import statistics

def generateData(min_val, max_val, mean, std, days):

    # define the distribution
    dist = stats.truncnorm(
        (min_val-mean)/std, (max_val-mean)/std, loc=mean, scale=std)

    # define the number of days to train
    trainingData = (dist.rvs(days))

    # round training data to discrete values
    roundedData = [round(value, 0) for value in trainingData]

    # get the mean and stdev
    dataMean = statistics.mean(roundedData)
    dataStdev = statistics.stdev(roundedData)

    print("Original Data", trainingData)
    print("Rounded Data", roundedData)
    print("Mean: ", dataMean)
    print("St.dev: ", dataStdev)

def initialInput():
    statsDict = {}
    eventsDiscreteDict = {}
    eventsContinuousDict = {}

    commandArg = sys.argv
    currentDir = os.path.dirname(os.path.abspath(__file__))
    eventFileDir = os.path.join(currentDir, commandArg[1])
    statsFileDir = os.path.join(currentDir, commandArg[2])
    noOfDays = commandArg[3]

    eventsFile = open(eventFileDir, "r")
    statsFile = open(statsFileDir, "r")

    # Stats.txt
    statsFileList = statsFile.read().split("\n")
    statsFileList.pop(0)

    for i in range(len(statsFileList)):
        statsFileSplitByColon = statsFileList[i].split(":")
        statsDict[statsFileSplitByColon[0]] = statsFileSplitByColon[1:3]
    
    loginsKey = list(statsDict.keys())[0] #Getting the "Logins" key

    for keys in statsDict:
        if (keys == loginsKey):
            statsLoginMean = statsDict[keys][0]
            statsLoginStdDev = statsDict[keys][1]

    print("Stats Dictionary: " + str(statsDict) + "\n")    
    print("Stats Logins Mean: " + statsLoginMean)
    print("Stats Logins Std Dev: " + statsLoginStdDev + "\n")

    ################################################################################

    # Events.txt
    eventsFileList = eventsFile.read().split("\n")
    eventsFileList.pop(0)

    for i in range(len(eventsFileList)):
        eventsFileSplitByColon = eventsFileList[i].split(":")
        if (eventsFileSplitByColon[1] == "C"):
            eventsContinuousDict[eventsFileSplitByColon[0]] = eventsFileSplitByColon[2:5]
        elif (eventsFileSplitByColon[1] == "D"): 
            eventsDiscreteDict[eventsFileSplitByColon[0]] = eventsFileSplitByColon[2:5]
        else:
            print("Event does not exist!")  #Inconsistency because no C/D

    print("Continuous Dictionary: " + str(eventsContinuousDict) + "\n")
    print("Discrete Dictionary: " + str(eventsDiscreteDict) + "\n")

    generateData(0, int(statsLoginMean)*float(statsLoginStdDev), int(statsLoginMean), float(statsLoginStdDev), int(noOfDays))

###################################################################################
if __name__ == "__main__":
    initialInput()