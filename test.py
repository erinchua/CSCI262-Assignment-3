import numpy as np
import scipy.stats as stats
import matplotlib.pyplot as plt
import statistics

a, b = 0, 9999
mu, sigma = 12, 4.5


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


generateData(a, b, mu, sigma, 5)
generateData(a, b, mu, sigma, 5)
generateData(a, b, mu, sigma, 5)
generateData(a, b, mu, sigma, 5)

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
# x = np.linspace(min_val, max_val, 100)
# plt.plot(x, my_dist.pdf(x))
# # Stats
# print('mean:', my_dist.mean(), 'std:', my_dist.std())
# # Get a large sample to check bounds
# sample = my_dist.rvs(size=100000)
# print('min:', sample.min(), 'max:', sample.max())
