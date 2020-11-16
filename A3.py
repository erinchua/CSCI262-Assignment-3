import os, sys
import scipy.stats as stats
import statistics

def generateData(min_val, max_val, mean, std, days):

    # define the distribution
    dist = stats.truncnorm((min_val-mean)/std, (max_val-mean)/std, loc=mean, scale=std)

    # define the number of days to train
    trainingData = (dist.rvs(days))

    # round training data to discrete values
    roundedData = [round(value) for value in trainingData]

    # get the mean and stdev
    dataMean = statistics.mean(roundedData)
    dataStdev = statistics.stdev(roundedData)

    print("Original Data", trainingData)
    # print("Rounded Data", roundedData)
    print("Mean: ", dataMean)
    print("St.dev: ", dataStdev)

    return(roundedData)    

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

    # loginsKey = list(statsDict.keys())[0]  # Getting the "Logins" key
    # timeOnlineKey = list(statsDict.keys())[1]  # Getting the "Time online" key
    # emailSentKey = list(statsDict.keys())[2]  # Getting the "Email sent" key
    # emailOpenedKey = list(statsDict.keys())[3]  # Getting the "Email opened" key
    # emailDeletedKey = list(statsDict.keys())[4]  # Getting the "Email deleted" key

    for keys in statsDict:
        if (keys == "Logins"):
            statsLoginMean = float(statsDict[keys][0])
            statsLoginStdDev = float(statsDict[keys][1])
    
        if (keys == "Time Online"):
            statsOnlineMean = float(statsDict[keys][0])
            statsOnlineStdDev = float(statsDict[keys][1])

        if (keys == "Emails sent"):
            statsEmailSentMean = float(statsDict[keys][0])
            statsEmailSentStdDev = float(statsDict[keys][1])

        if (keys == "Emails opened"):
            statsEmailOpenedMean = float(statsDict[keys][0])
            statsEmailOpenedStdDev = float(statsDict[keys][1])

        if (keys == "Emails deleted"):
            statsEmailDeletedMean = float(statsDict[keys][0])
            statsEmailDeletedStdDev = float(statsDict[keys][1])

    print("Stats Dictionary: " + str(statsDict), "\n")
    print("Stats Logins Mean: ", statsLoginMean)
    print("Stats Logins Std Dev: ", statsLoginStdDev, "\n")

    ################################################################################

    # Events.txt
    eventsFileList = eventsFile.read().split("\n")
    eventsFileList.pop(0)

    print("Len: " + str(len(eventsFileList)))

    for i in range(len(eventsFileList)):
        eventsFileSplitByColon = eventsFileList[i].split(":")
        minVal = eventsFileSplitByColon[2]  #Min
        maxVal = eventsFileSplitByColon[3]  #Max

        if (eventsFileSplitByColon[1] == "C"):
            eventsContinuousDict[eventsFileSplitByColon[0]] = eventsFileSplitByColon[2:5]
        elif (eventsFileSplitByColon[1] == "D"):
            eventsDiscreteDict[eventsFileSplitByColon[0]] = eventsFileSplitByColon[2:5]
        else:
            print("Event does not exist!")  # Inconsistency because no C/D


    print("Continuous Dictionary: " + str(eventsContinuousDict) + "\n")
    print("Discrete Dictionary: " + str(eventsDiscreteDict) + "\n")
    print("Continuous Min: " + str(continuousMin))
    print("Continuous Max: " + str(continuousMax))
    print("Discrete Min: " + str(discreteMin))
    print("Discrete Max: " + str(discreteMax))

    for keys in eventsDiscreteDict:
        if (keys == "Logins"):
            loginsMin = int(eventsDiscreteDict[keys][0])
            if eventsDiscreteDict[keys][1] == '':
                loginsMax = int(statsLoginMean)*float(statsLoginStdDev)
            else:
                loginsMax = int(eventsDiscreteDict[keys][1])

        if (keys == "Emails sent"):
            emailSentMin = int(eventsDiscreteDict[keys][0])
            if eventsDiscreteDict[keys][1] == '':
                emailSentMax = int(statsEmailSentMean)*float(statsEmailSentStdDev)
            else:
                emailSentMax = int(eventsDiscreteDict[keys][1])

        if (keys == "Emails opened"):
            emailOpenedMin = int(eventsDiscreteDict[keys][0])
            if eventsDiscreteDict[keys][1] == '':
                emailOpenedMax = int(statsEmailOpenedMean)*float(statsEmailOpenedStdDev)
            else:
                emailOpenedMax = int(eventsDiscreteDict[keys][1])

        if (keys == "Emails deleted"):
            emailDeletedMin = int(eventsDiscreteDict[keys][0])
            if eventsDiscreteDict[keys][1] == '':
                emailDeletedMax = int(statsEmailDeletedMean)*float(statsEmailDeletedStdDev)
            else:
                emailDeletedMax = int(eventsDiscreteDict[keys][1])

###################################################################################
    # Generate training data

    for keys in eventsDiscreteDict:
        if (keys == "Logins"):
            loginData = generateData(loginsMin, loginsMax, int(statsLoginMean), float(statsLoginStdDev), int(noOfDays))
            print("Logins " + str(loginData) + "\n")

        if (keys == "Emails sent"):
            emailSentData = generateData(emailSentMin, emailSentMax, int(statsEmailSentMean), float(statsEmailSentStdDev), int(noOfDays))
            print("Emails sent " + str(emailSentData) + "\n")

        if (keys == "Emails opened"):
            emailOpenData = generateData(emailOpenedMin, emailOpenedMax, int(statsEmailOpenedMean), float(statsEmailOpenedStdDev), int(noOfDays))
            print("Emails opened " + str(emailOpenData) + "\n")

        if (keys == "Emails deleted"):
            emailDeletedData = generateData(emailDeletedMin, emailDeletedMax, int(statsEmailDeletedMean), float(statsEmailDeletedStdDev), int(noOfDays))
            print("Emails deleted " + str(emailDeletedData) + "\n")

###################################################################################


if __name__ == "__main__":
    initialInput()
