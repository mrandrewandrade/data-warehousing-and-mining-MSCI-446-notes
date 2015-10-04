import csv
import matplotlib.pyplot as plt
import numpy as np

residuals = []
x = []
with open('residuals.csv', newline = '') as csvfile:
    spamreader = csv.reader(csvfile, delimiter=',')
    for row in spamreader:
    	residuals.append(float(row[1]))
    	x.append(float(row[0]))

# Scatter plot
plt.scatter(x, residuals)
plt.show()

# Frequency plot (Histogram)
# residuals = np.array(residuals)
# print(residuals)
# plt.hist(residuals, bins=10)
# plt.show()