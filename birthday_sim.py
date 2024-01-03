import numpy as np
import pandas as pd
import statistics as stat
import matplotlib.pyplot as plt

trial_list = [] # make an array to store values
bday_list = []
n = 1000 # trials
counter = 0

# code from Jochen Ritzel on stackoverflow to determine if a list contains duplicates
def has1dup(lst):
    return len(lst)-1 == len(set(lst))

for i in range(n): # running the loop n times
    counter = 0
    res = False
    bday_list.clear()
    while res == False: 
        x = np.random.randint(1, 366) # 365 days in year
        bday_list.append(x)
        res = has1dup(bday_list)
        counter = counter + 1
    trial_list.append(counter)

# stats
print("Mean: " + str(stat.mean(trial_list)))
print("Median: " + str(stat.median(trial_list)))
print("Mode: " + str(stat.mode(trial_list)))
print("Standard Deviation: " + str(stat.stdev(trial_list)))

# histogram of values
plt.hist(trial_list, density=True)
plt.xlabel("N people")
plt.ylabel("Density")
plt.show()
