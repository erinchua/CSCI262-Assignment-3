import numpy as np
import scipy.stats as stats
import matplotlib.pyplot as plt
import statistics

a, b = 0, 1440
mu, sigma = 150.5, 25


def generateData(min_val, max_val, mean, std, days):
    lowestDiff = None
    bestData = None
    for i in range(10):

        # define the distribution
        dist = stats.truncnorm((min_val-mean)/std, (max_val-mean)/std, loc=mean, scale=std)

        # define the number of days to train
        trainingData = (dist.rvs(days))

        # round training data to discrete values
        roundedData = [round(value, 0) for value in trainingData]

        # get the mean and stdev
        dataMean = statistics.mean(roundedData)
        dataStdev = statistics.stdev(roundedData)
        meanStdDiff = abs(mean-dataMean) + abs(std-dataStdev)
        if(lowestDiff == None):
            lowestDiff = meanStdDiff
            bestData = roundedData
        elif(meanStdDiff<lowestDiff):
            lowestDiff = meanStdDiff
            bestData = roundedData

        # print("Original Data", i , trainingData)
        # print("Rounded Data", roundedData)
        print("Mean: ", i , dataMean)
        print("St.dev: ", i , dataStdev)
        print("Current diff ",meanStdDiff)

    print("final data", bestData)
    print("lowestDiff = ", lowestDiff)
    print()
    return bestData

def generateOnline(min_val, max_val, mean, std, days):

    lowestDiff = None
    bestData = None
    for i in range(10):

        # define the distribution
        dist = stats.truncnorm((min_val-mean)/std, (max_val-mean)/std, loc=mean, scale=std)

        # define the number of days to train
        trainingData = (dist.rvs(days))

        roundedData = [round(value, 2) for value in trainingData]

        # get the mean and stdev
        dataMean = statistics.mean(roundedData)
        dataStdev = statistics.stdev(roundedData)
        meanStdDiff = abs(mean-dataMean) + abs(std-dataStdev)
        if(lowestDiff == None):
            lowestDiff = meanStdDiff
            bestData = roundedData
        elif(meanStdDiff<lowestDiff):
            lowestDiff = meanStdDiff
            bestData = roundedData

        # print("Original Data", i , trainingData)
        print("Rounded Data", roundedData)
        print("Mean: ", i , dataMean)
        print("St.dev: ", i , dataStdev)
        print("Current diff ",meanStdDiff)

    print("final data", bestData)
    print("lowestDiff = ", lowestDiff)
    print()

    # x = np.linspace(min_val, max_val, 30)
    # plt.plot(x,dist.pdf(x))
    # plt.xlim(0,1440)
    # plt.ylim(0, days)

    # plt.show()
    return trainingData
    

values = generateOnline(a,b,mu,sigma,5)
# def my_distribution(min_val, max_val, mean, std):
#     scale = max_val - min_val
#     location = min_val
#     # Mean and standard deviation of the unscaled beta distribution
#     unscaled_mean = (mean - min_val) / scale
#     unscaled_var = (std / scale) ** 2
#     # Computation of alpha and beta can be derived from mean and variance formulas
#     t = unscaled_mean / (1 - unscaled_mean)
#     beta = ((t / unscaled_var) - (t * t) - (2 * t) - 1) / \
#         ((t * t * t) + (3 * t * t) + (3 * t) + 1)
#     alpha = beta * t
#     # Not all parameters may produce a valid distribution
#     if alpha <= 0 or beta <= 0:
#         raise ValueError(
#             'Cannot create distribution for the given parameters.')
#     # Make scaled beta distribution with computed parameters
#     return stats.beta(alpha, beta, scale=scale, loc=location)


# np.random.seed(100)

# min_val = 0
# max_val = 1440
# mean = 150.5
# std = 25
# my_dist = my_distribution(min_val, max_val, mean, std)

# # Plot distribution PDF
# # x = np.linspace(min_val, max_val, 100)
# # plt.plot(x, my_dist.pdf(x))
# # Stats
# print('mean:', my_dist.mean(), 'std:', my_dist.std())
# # Get a large sample to check bounds
# sample = my_dist.rvs(size=20)
# print('min:', sample.min(), 'max:', sample.max())
# print(sample)
