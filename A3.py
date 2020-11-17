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

def analysisEngine(finalList, meanStdFileOpen, weightList):
    print(finalList)
    print(meanStdFileOpen)
    print(weightList)

    a = 0
    b = 1
    c = 2
    d = 3
    e = 4
    loginCounterList = []
    timeOnlineCounterList = []
    emailsSentCounterList = []
    emailsOpenedCounterList = []
    emailsDeletedCounterList = []

    while a < (len(finalList)):
        loginData = finalList[a]
        timeOnlineData = finalList[b]
        emailsSentData = finalList[c]
        emailsOpenedData = finalList[d]
        emailsDeletedData = finalList[e]        

        print("loginData: " + str(loginData))
        print("timeOnlineData: " + str(timeOnlineData))
        print("emailsSentData: " + str(emailsSentData))
        print("emailsOpenedData: " + str(emailsOpenedData))
        print("emailsDeletedData: " + str(emailsDeletedData))
        
        #meanStdFileOpen Splits
        meanStdSplitByEvent = meanStdFileOpen.split(":")
        print(meanStdSplitByEvent[:4])
        for i in range(len(meanStdSplitByEvent[:4])):
            meanStdSplitByDash = meanStdSplitByEvent[i].split("-")
            print(meanStdSplitByDash)
            for j in meanStdSplitByDash[1]:
                meanStdSplitByCommas = meanStdSplitByDash[1].split(",")
            mean = meanStdSplitByCommas[0]
            stdDev = meanStdSplitByCommas[1]
            print(mean)
            print(stdDev)

            loginCounterList = ((float(mean) - int(loginData))/float(stdDev))*int(weightList[0])
            timeOnlineCounterList = ((float(mean) - int(timeOnlineData))/float(stdDev))*int(weightList[1])
            emailsSentCounterList = ((float(mean) - int(emailsSentData))/float(stdDev))*int(weightList[2])
            emailsOpenedCounterList = ((float(mean) - int(emailsOpenedData))/float(stdDev))*int(weightList[3])
            emailsDeletedCounterList = ((float(mean) - int(emailsDeletedData))/float(stdDev))*int(weightList[4])

            print("\nlogin: ", abs(loginCounterList))
            print("\ntimeOnline: ", abs(timeOnlineCounterList))
            print("\nemailsSent: ", abs(emailsSentCounterList))
            print("\nemailsOpened: ", abs(emailsOpenedCounterList))
            print("\nemailsDeleted: ", abs(emailsDeletedCounterList))

        a+=5
        b+=5
        c+=5
        d+=5
        e+=5

   

# get current datetime format
def dateTime():
    dateTime = datetime.datetime.now().strftime('%Y%m%d-%H%M%S')
    print("datetime = ", dateTime)

    return str(dateTime)


def generateData(min_val, max_val, mean, std, days, type):
    lowestDiff = None
    bestData = None
    for i in range(10):

        # define the distribution
        dist = stats.truncnorm((min_val-mean)/std, (max_val-mean)/std, loc=mean, scale=std)

        # define the number of days to train
        trainingData = (dist.rvs(days))

        if(type=='D'):
            # round training data to discrete values
            roundedData = [round(value) for value in trainingData]
        else:
             # round training data to 2dp continuous values
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

        # print("Original Data", trainingData)
        print("Rounded Data", roundedData)
        print("Mean: ", dataMean)
        print("St.dev: ", dataStdev)

    return(bestData)

def activitySimulation(eventsFileDir, statsFileDir, noOfDays):
    statsDict = {}
    eventsDiscreteDict = {}
    eventsContinuousDict = {}
    loginExist = False
    timeOnlineExist = False
    emailSentExist = False
    emailOpenedExist = False
    emailDeletedExist = False
    totalWeights =[]
    threshold = 0

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
            
        if (keys == "Time online"):
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

    print("Stats Dictionary: " + str(statsDict), "\n")
    # print("Stats Logins Mean: ", statsLoginMean)
    # print("Stats Logins Std Dev: ", statsLoginStdDev, "\n")
    
    ################################################################################

    # Events.txt
    eventsFileList = eventsFile.read().split("\n")
    eventsFileList.pop(0)
    weightList = []

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

    for keys in eventsContinuousDict:
        if (keys == "Time online" and timeOnlineExist == True):
            timeOnlineMin = int(eventsContinuousDict[keys][0])
            timeOnlineName = keys
            timeOnlineWeight = int(eventsContinuousDict[keys][2])
            weightList.insert(1, timeOnlineWeight)
            if eventsContinuousDict[keys][1] == '':
                timeOnlineMax = int(statsOnlineMean)*float(statsOnlineStdDev)
            else:
                timeOnlineMax = int(eventsContinuousDict[keys][1])

    for keys in eventsDiscreteDict:
        if (keys == "Logins" and loginExist == True):
            loginsMin = int(eventsDiscreteDict[keys][0])
            loginsName = keys
            loginsWeight = int(eventsDiscreteDict[keys][2])
            weightList.insert(0, loginsWeight)
            if eventsDiscreteDict[keys][1] == '':
                loginsMax = int(statsLoginMean)*float(statsLoginStdDev)
            else:
                loginsMax = int(eventsDiscreteDict[keys][1])

        if (keys == "Emails sent" and emailSentExist == True):
            emailSentMin = int(eventsDiscreteDict[keys][0])
            emailSentName = keys
            emailSentWeight = int(eventsDiscreteDict[keys][2])
            weightList.insert(2, emailSentWeight)
            if eventsDiscreteDict[keys][1] == '':
                emailSentMax = int(statsEmailSentMean)*float(statsEmailSentStdDev)
            else:
                emailSentMax = int(eventsDiscreteDict[keys][1])

        if (keys == "Emails opened" and emailOpenedExist == True):
            emailOpenedMin = int(eventsDiscreteDict[keys][0])
            emailOpenedName = keys
            emailOpenedWeight = int(eventsDiscreteDict[keys][2])
            weightList.insert(3, emailOpenedWeight)
            if eventsDiscreteDict[keys][1] == '':
                emailOpenedMax = int(statsEmailOpenedMean)*float(statsEmailOpenedStdDev)
            else:
                emailOpenedMax = int(eventsDiscreteDict[keys][1])

        if (keys == "Emails deleted" and emailDeletedExist == True):
            emailDeletedMin = int(eventsDiscreteDict[keys][0])
            emailDeletedName = keys
            emailDeletedWeight = int(eventsDiscreteDict[keys][2])
            weightList.insert(4, emailDeletedWeight)
            if eventsDiscreteDict[keys][1] == '':
                emailDeletedMax = int(statsEmailDeletedMean)*float(statsEmailDeletedStdDev)
            else:
                emailDeletedMax = int(eventsDiscreteDict[keys][1])

    for keys in eventsContinuousDict:
        if(keys=='Time online'):
            totalWeights.append(eventsContinuousDict[keys][2])
    ###############################################################################

    # Calculating threshold
    for weight in totalWeights:
        threshold+=int(weight)
    threshold*=2
    print("Individual weights",totalWeights)
    print("Total threshold",threshold)
    
    ###############################################################################
    # Generate training data

    if (loginExist == True):
        loginData = generateData(loginsMin, loginsMax, int(statsLoginMean), float(statsLoginStdDev), int(noOfDays),'D')
        print("Logins: " + str(loginData) + "\n")

    if (timeOnlineExist == True):
        timeOnlineData = generateData(timeOnlineMin, timeOnlineMax, int(statsOnlineMean), float(statsOnlineStdDev), int(noOfDays),'C')
        print("Time online: " + str(timeOnlineData) + "\n")
        
    if (emailSentExist == True):
        emailSentData = generateData(emailSentMin, emailSentMax, int(statsEmailSentMean), float(statsEmailSentStdDev), int(noOfDays),'D')
        print("Emails sent: " + str(emailSentData) + "\n")

    if (emailOpenedExist == True):
        emailOpenData = generateData(emailOpenedMin, emailOpenedMax, int(statsEmailOpenedMean), float(statsEmailOpenedStdDev), int(noOfDays),'D')
        print("Emails opened: " + str(emailOpenData) + "\n")

    if (emailDeletedExist == True):
        emailDeletedData = generateData(emailDeletedMin, emailDeletedMax, int(statsEmailDeletedMean), float(statsEmailDeletedStdDev), int(noOfDays),'D')
        print("Emails deleted: " + str(emailDeletedData) + "\n")

    i = 0
    logList = []
    meanStdList = []
    finalList = []

    #Training Data
    while i < int(noOfDays):      
        logList.append(i+1)
        logList.append(":") 

        if (loginExist == True):
            logList.append(loginsName)
            logList.append("-")
            logList.append(loginData[i])
            finalList.append(loginData[i])
            logList.append(":")

        if (timeOnlineExist == True):
            logList.append(timeOnlineName)
            logList.append("-")
            logList.append(timeOnlineData[i])
            finalList.append(timeOnlineData[i])
            logList.append(":")
        
        if (emailSentExist == True):
            logList.append(emailSentName)
            logList.append("-")
            logList.append(emailSentData[i])
            finalList.append(emailSentData[i])
            logList.append(":")

        if (emailOpenedExist == True):
            logList.append(emailOpenedName)
            logList.append("-")
            logList.append(emailOpenData[i])
            finalList.append(emailOpenData[i])
            logList.append(":")

        if(emailDeletedExist == True):
            logList.append(emailDeletedName)
            logList.append("-")
            logList.append(emailDeletedData[i])
            finalList.append(emailDeletedData[i])
            logList.append(":")
        
        logList.append("\n")

        #Get current dateTime
        currentDateTime = dateTime()

        #Write to TrainingLogs_??.txt 
        logFileName = "TrainingLogs_" + currentDateTime + ".txt"
        with open(logFileName, "w") as writer:
            for log in logList:
                for string in str(log):
                    writer.write(str(string))
                
            writer.close()
            
        i+=1

    #Mean, Standard Deviation of Training Data    
    if (loginExist == True):
        meanStdList.append(loginsName)
        meanStdList.append("-")
        meanStdList.append(round(statistics.mean(loginData), 2))
        meanStdList.append(",")
        meanStdList.append(round(statistics.stdev(loginData), 2))
        meanStdList.append(":")

    if (timeOnlineExist == True):
        meanStdList.append(timeOnlineName)
        meanStdList.append("-")
        meanStdList.append(round(statistics.mean(timeOnlineData), 2))
        meanStdList.append(",")
        meanStdList.append(round(statistics.stdev(timeOnlineData), 2))
        meanStdList.append(":")
    
    if (emailSentExist == True):
        meanStdList.append(emailSentName)
        meanStdList.append("-")
        meanStdList.append(round(statistics.mean(emailSentData), 2))
        meanStdList.append(",")
        meanStdList.append(round(statistics.stdev(emailSentData), 2))
        meanStdList.append(":")

    if (emailOpenedExist == True):
        meanStdList.append(emailOpenedName)
        meanStdList.append("-")
        meanStdList.append(round(statistics.mean(emailOpenData), 2))
        meanStdList.append(",")
        meanStdList.append(round(statistics.stdev(emailOpenData), 2))
        meanStdList.append(":")

    if(emailDeletedExist == True):
        meanStdList.append(emailDeletedName)
        meanStdList.append("-")
        meanStdList.append(round(statistics.mean(emailDeletedData), 2))
        meanStdList.append(",")
        meanStdList.append(round(statistics.stdev(emailDeletedData), 2))
        meanStdList.append(":")
    
    meanStdList.append("\n")

    #Write to TrainingMeanStd_??.txt
    meanFileName = "TrainingMeanStd_" + currentDateTime + ".txt"
    with open(meanFileName, "w") as writer:
        for meanStd in meanStdList:
            for string in str(meanStd):
                writer.write(str(string))
            
        writer.close()

    cont = input("\nSuccessfully generated and logged events. Press 'Enter' to begin analysing...\n")

    logFile = open(logFileName, 'r')
    logFileOpen = logFile.read()

    meanStdFile = open(meanFileName, 'r')
    meanStdFileOpen = meanStdFile.read()

    analysisEngine(finalList, meanStdFileOpen, weightList)      

    return cont
    
###################################################################################

# Alert Engine 

def alertEngine():
    dailyCounterFile = open('DailyCounter','r').read()
    print(dailyCounterFile)


###################################################################################

if __name__ == "__main__":
    running = False
    counter = 1

    while not running:
        
        #Run the first initial training
        if (counter == 1):
            #Initial Input
            commandArg = sys.argv
            currentDir = os.path.dirname(os.path.abspath(__file__))
            eventFileDir = os.path.join(currentDir, commandArg[1])
            statsFileDir = os.path.join(currentDir, commandArg[2])
            noOfDays = commandArg[3]

            print("Files have been successfully read. The activity engine will begin generating and logging now...")
            #Activity Simulation Engine and Logs
            activitySimulation(eventFileDir, statsFileDir, noOfDays)
            counter+=1

        #Subsequent steps
        else:
            if (counter == 2):
                options = input("\nOptions: Enter C - Continue or Q - Quit: \n")

                if (options == "q" or options == "Q"):
                    print("\nShutting down IDS...\n")
                    sys.exit()

                elif (options == "c" or options == "C"):
                    newStatsFile = input("\nPlease insert a new set of Stats file and no. of days to be considered\n")

                    lines = newStatsFile.split(" ")

                    if (len(lines) == "2" or len(lines) == 2):
                        print("Files have been successfully read. The activity engine will begin generating and logging now...")

                        if activitySimulation("Events.txt", lines[0], lines[1]):
                            running = False
                    else:
                        counter = 2
                else:
                    print("\nInvalid options!")
