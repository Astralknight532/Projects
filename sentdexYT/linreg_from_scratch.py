# -*- coding: utf-8 -*-
"""
Created on Tue Oct 13 16:27:16 2020

@author: hanan
"""

# Definition of a line
# y = mx + b
# m is the slope of the (hopefully best-fit) line, 
# b is the y-intercept of the line

# The best fit line is also called the y-hat/regression line, 
# among other things

# Remember PEMDAS for order of operations
# equation for m:
# ((mean(x) * mean(y)) - mean(xy)) / (mean(x) ^ 2 - mean(x^2))

# R-squared - coefficient of determination
# Formula for R-squared (where y represents the y-values of the dataset):
# r ^ 2 = 1 - (SE of y-hat line) / (SE of mean(y))
# Squared error - SE, y-hat line refers to the best fit line itself
# generally having the y-hat line's SE be significantly
# less than mean(y)'s SE is desired

from statistics import mean
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import style
import random # only pseudo-random, not actually random

style.use('fivethirtyeight')

#xs = np.array([1, 2, 3, 4, 5, 6], dtype = np.float64)
#ys = np.array([5, 4, 6, 5, 6, 7], dtype = np.float64)

# Function to create a sample dataset for testing purposes
def create_dataset(hm, variance, step = 2, correlation = False):
    val = 1
    ys = []
    
    for i in range(hm):
        y = val + random.randrange(-variance, variance)
        ys.append(y)
        if correlation and correlation == 'pos':
            val += step
        elif correlation and correlation == 'neg':
            val -= step
    
    xs = [i for i in range(len(ys))]
    return np.array(xs, dtype = np.float64), np.array(ys, dtype = np.float64)

# Function to calculate the slope & y-intercept of the best fit line
def best_fit_slope_and_intercept(xs, ys):
    m = (((mean(xs) * mean(ys)) - mean(xs * ys)) /
         ((mean(xs) ** 2) - mean(xs ** 2)))
    
    b = mean(ys) - m * mean(xs)
    return m, b

# Function to calculate the squared error
def squared_error(ys_orig, ys_line):
    return sum((ys_line - ys_orig) ** 2)

# Function to calculate the coefficient of determination (aka r-squared or r ^ 2)
def coefficient_of_determination(ys_orig, ys_line):
    y_mean_line = [mean(ys_orig) for y in ys_orig]
    squared_error_regr = squared_error(ys_orig, ys_line)
    squared_error_y_mean = squared_error(ys_orig, y_mean_line)
    return 1 - (squared_error_regr / squared_error_y_mean)

xs, ys = create_dataset(40, 80, 2, correlation = 'pos')

m, b = best_fit_slope_and_intercept(xs, ys)
#print("Best fit slope: %s\nBest fit y-intercept: %s" % (m, b))

regression_line = [(m * x) + b for x in xs]

predict_x = 8
predict_y = (m * predict_x) + b

r_squared = coefficient_of_determination(ys, regression_line)
#print("Coefficient of determination (r-squared): %s" % r_squared)

plt.scatter(xs, ys)
plt.scatter(predict_x, predict_y, s = 100, color = 'g')
plt.plot(xs, regression_line)
plt.show()
