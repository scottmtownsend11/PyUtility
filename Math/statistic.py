# Imports

import math


# Core

# Calculates the mean
def mean(a):
    return sum(a) / len(a)

# Calculates the population variance
def variance(a):
    m = mean(a)
    a2 = [ math.pow(m - i,2) for i in a ] # Creates an array of the squared differences between the mean and each value in the original array
    return mean(a2)

# Calculates the population standard deviation
def standard_deviation(a):
    return math.sqrt(variance(a))

# Calculates the percent the index is compared to all values in the array
def percentage(a, i):
    return float(a[i]) / sum(a)
