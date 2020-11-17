'''
-----------------------------------------
Members' Names:
-----------------------------------------
    CSCI262 System Security Assignment 3
    VINCENT YAP WEI SHENG (6649750)
    CHUA CHIA EN, ERIN (6650338)
    BEATRICIA LIYU ZI LING (6650211)
'''
import os, sys
import scipy.stats as stats
import statistics
import datetime

def meanStdLog(meanStdFile):

    fileName = "TrainingMeanStd_" + dateTime() + ".txt"

    with open(fileName, "w") as writer:
        for meanStd in meanStdFile:
            for string in str(meanStd):
                writer.write(str(string))
            
        writer.close()

# get current datetime format
def dateTime():
    dateTime = datetime.datetime.now().strftime('%Y%m%d-%H%M%S')
    print("datetime = ", dateTime)

    return str(dateTime)

# writing to training log files
def logDailyEvent(logFile):

    fileName = "TrainingLogs_" + dateTime() + ".txt"
    
    with open(fileName, "w") as writer:
        for log in logFile:
            for string in str(log):
                writer.write(str(string))
            
        writer.close()
        

def generateData(min_val, max_val, mean, std, days):
    lowestDiff = None
    bestData = None
    for i in range(10):

        # define the distribution
        dist = stats.truncnorm((min_val-mean)/std, (max_val-mean)/std, loc=mean, scale=std)

        # define the number of days to train
        trainingData = (dist.rvs(days))

        # round training data to discrete values
        roundedData = [round(value) for value in trainingData]

        # get the mean and stdev
        dataMean = statistics.mean(roundedData)
        dataStdev = statistics.stdev(roundedData)
        
        # get absolute different for mean and std, lowest = best fit and store it as best fit data
        meanStdDiff = abs(mean-dataMean) + abs(std-dataStdev)
        if(lowestDiff == None):
            lowestDiff = meanStdDiff
            bestData = roundedData
        elif(meanStdDiff<lowestDiff):
            lowestDiff = meanStdDiff
            bestData = roundedData

        # print("Original Data", trainingData)
        print("Rounded Data", roundedData)
        print("Mean: ", dataMean)
        print("St.dev: ", dataStdev)

    return(bestData)

def generateOnline(min_val, max_val, mean, std, days):

    lowestDiff = None
    bestData = None
    for i in range(10):

        # define the distribution
        dist = stats.truncnorm((min_val-mean)/std, (max_val-mean)/std, loc=mean, scale=std)

        # define the number of days to train
        trainingData = (dist.rvs(days))

        # round training data to 2dp values
        roundedData = [round(value,2) for value in trainingData]

        # get the mean and stdev
        dataMean = statistics.mean(roundedData)
        dataStdev = statistics.stdev(roundedData)

        # get absolute different for mean and std, lowest = best fit and store it as best fit data
        meanStdDiff = abs(mean-dataMean) + abs(std-dataStdev)
        if(lowestDiff == None):
            lowestDiff = meanStdDiff
            bestData = roundedData
        elif(meanStdDiff<lowestDiff):
            lowestDiff = meanStdDiff
            bestData = roundedData

        print("Rounded Data", roundedData)
        print("Mean: ", i , dataMean)
        print("St.dev: ", i , dataStdev)
        print("Current diff ",meanStdDiff)

    return trainingData

def initialInput():
    statsDict = {}
    eventsDiscreteDict = {}
    eventsContinuousDict = {}
    loginExist = False
    timeOnlineExist = False
    emailSentExist = False
    emailOpenedExist = False
    emailDeletedExist = False

    eventsFile = open(eventFileDir, "r")
    statsFile = open(statsFileDir, "r")

    # Stats.txt
    statsFileList = statsFile.read().split("\n")
    statsFileList.pop(0)

    for i in range(len(statsFileList)):
        statsFileSplitByColon = statsFileList[i].split(":")
        statsDict[statsFileSplitByColon[0]] = statsFileSplitByColon[1:3]

    for keys in statsDict:
        if (keys == "Logins"):
            statsLoginMean = float(statsDict[keys][0])
            statsLoginStdDev = float(statsDict[keys][1])
            loginExist = True
            
        if (keys == "Time Online"):
            statsOnlineMean = float(statsDict[keys][0])
            statsOnlineStdDev = float(statsDict[keys][1])
            timeOnlineExist = True

        if (keys == "Emails sent"):
            statsEmailSentMean = float(statsDict[keys][0])
            statsEmailSentStdDev = float(statsDict[keys][1])
            emailSentExist = True

        if (keys == "Emails opened"):
            statsEmailOpenedMean = float(statsDict[keys][0])
            statsEmailOpenedStdDev = float(statsDict[keys][1])
            emailOpenedExist = True

        if (keys == "Emails deleted"):
            statsEmailDeletedMean = float(statsDict[keys][0])
            statsEmailDeletedStdDev = float(statsDict[keys][1])
            emailDeletedExist = True

    # print("Stats Dictionary: " + str(statsDict), "\n")
    # print("Stats Logins Mean: ", statsLoginMean)
    # print("Stats Logins Std Dev: ", statsLoginStdDev, "\n")

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
            print("Event does not exist!")  # Inconsistency because no C/D

    print("Continuous Dictionary: " + str(eventsContinuousDict) + "\n")
    print("Discrete Dictionary: " + str(eventsDiscreteDict) + "\n")

    for keys in eventsDiscreteDict:
        if (keys == "Logins" and loginExist == True):
            loginsMin = int(eventsDiscreteDict[keys][0])
            loginsName = keys
            if eventsDiscreteDict[keys][1] == '':
                loginsMax = int(statsLoginMean)*float(statsLoginStdDev)
            else:
                loginsMax = int(eventsDiscreteDict[keys][1])

        if (keys == "Emails sent" and emailSentExist == True):
            emailSentMin = int(eventsDiscreteDict[keys][0])
            emailSentName = keys
            if eventsDiscreteDict[keys][1] == '':
                emailSentMax = int(statsEmailSentMean)*float(statsEmailSentStdDev)
            else:
                emailSentMax = int(eventsDiscreteDict[keys][1])

        if (keys == "Emails opened" and emailOpenedExist == True):
            emailOpenedMin = int(eventsDiscreteDict[keys][0])
            emailOpenedName = keys
            if eventsDiscreteDict[keys][1] == '':
                emailOpenedMax = int(statsEmailOpenedMean)*float(statsEmailOpenedStdDev)
            else:
                emailOpenedMax = int(eventsDiscreteDict[keys][1])

        if (keys == "Emails deleted" and emailDeletedExist == True):
            emailDeletedMin = int(eventsDiscreteDict[keys][0])
            emailDeletedName = keys
            if eventsDiscreteDict[keys][1] == '':
                emailDeletedMax = int(statsEmailDeletedMean)*float(statsEmailDeletedStdDev)
            else:
                emailDeletedMax = int(eventsDiscreteDict[keys][1])

    ###############################################################################
    # Generate training data

    if (loginExist == True):
        loginData = generateData(loginsMin, loginsMax, int(statsLoginMean), float(statsLoginStdDev), int(noOfDays))
        print("Logins: " + str(loginData) + "\n")
        
    if (emailSentExist == True):
        emailSentData = generateData(emailSentMin, emailSentMax, int(statsEmailSentMean), float(statsEmailSentStdDev), int(noOfDays))
        print("Emails sent: " + str(emailSentData) + "\n")

    if (emailOpenedExist == True):
        emailOpenData = generateData(emailOpenedMin, emailOpenedMax, int(statsEmailOpenedMean), float(statsEmailOpenedStdDev), int(noOfDays))
        print("Emails opened: " + str(emailOpenData) + "\n")

    if (emailDeletedExist == True):
        emailDeletedData = generateData(emailDeletedMin, emailDeletedMax, int(statsEmailDeletedMean), float(statsEmailDeletedStdDev), int(noOfDays))
        print("Emails deleted: " + str(emailDeletedData) + "\n")

    i = 0
    logList = []
    meanStdList = []

    #Training Data
    while i < int(noOfDays):      
        logList.append(i+1)
        logList.append(":") 

        if (loginExist == True):
            logList.append(loginsName)
            logList.append("-")
            logList.append(loginData[i])
            logList.append(":")
        
        if (emailSentExist == True):
            logList.append(emailSentName)
            logList.append("-")
            logList.append(emailSentData[i])
            logList.append(":")

        if (emailOpenedExist == True):
            logList.append(emailOpenedName)
            logList.append("-")
            logList.append(emailOpenData[i])
            logList.append(":")

        if(emailDeletedExist == True):
            logList.append(emailDeletedName)
            logList.append("-")
            logList.append(emailDeletedData[i])
            logList.append(":")
        
        logList.append("\n")

        #Write to TrainingLogs_??.txt 
        logDailyEvent(logList)
            
        i+=1

    #Mean, Standard Deviation of Training Data    
    if (loginExist == True):
        meanStdList.append(loginsName)
        meanStdList.append("-")
        meanStdList.append(statistics.mean(loginData))
        meanStdList.append(",")
        meanStdList.append(statistics.stdev(loginData))
        meanStdList.append(":")
    
    if (emailSentExist == True):
        meanStdList.append(emailSentName)
        meanStdList.append("-")
        meanStdList.append(statistics.mean(emailSentData))
        meanStdList.append(",")
        meanStdList.append(statistics.stdev(emailSentData))
        meanStdList.append(":")

    if (emailOpenedExist == True):
        meanStdList.append(emailOpenedName)
        meanStdList.append("-")
        meanStdList.append(statistics.mean(emailOpenData))
        meanStdList.append(",")
        meanStdList.append(statistics.stdev(emailOpenData))
        meanStdList.append(":")

    if(emailDeletedExist == True):
        meanStdList.append(emailDeletedName)
        meanStdList.append("-")
        meanStdList.append(statistics.mean(emailDeletedData))
        meanStdList.append(",")
        meanStdList.append(statistics.stdev(emailDeletedData))
        meanStdList.append(":")
    
    meanStdList.append("\n")

    #Write to TrainingMeanStd_??.txt
    meanStdLog(meanStdList)   
            
    
    
###################################################################################


if __name__ == "__main__":
    running = False

    while not running:
        #Initial Inputs
        commandArg = sys.argv
        currentDir = os.path.dirname(os.path.abspath(__file__))
        eventFileDir = os.path.join(currentDir, commandArg[1])
        statsFileDir = os.path.join(currentDir, commandArg[2])
        noOfDays = commandArg[3]

        #Activity Simulation Engine and Logs
        activitySimulation(eventFileDir, statsFileDir, noOfDays)

        options = input("\nOptions: Enter C - Continue or Q - Quit: \n")

        if (options == "q" or options == "Q"):
            print("\nShutting down IDS...\n")
            sys.exit()

        elif (options == "c" or options == "C"):
            newStatsFile = input("Please insert a new set of Stats file and no. of days to be considered\n")

            lines = newStatsFile.split(" ")
            print(lines[0])
            print(lines[1])
            
            cont = input("Enter to continue...\n")

            if cont:
                running = False