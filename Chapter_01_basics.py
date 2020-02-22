""""This code checks for the time if the presenttime is odd or not odd
this code is taken from book Head_first_python by paul Barry"""

# importing the dependencies
from datetime import datetime
import numpy as np
import random
import time

# creating list of odd Dataset
odds = np.arange(1,60,2)
# print(odds) # this to check if the list is created as required

# Creating loop for 5 times
for i in range(5):
    # creating variable to check the minute
    right_this_minute = datetime.today().minute
    # riting the conditions
    if right_this_minute in odds:
        print('this minute seems little odd')
    else:
        print('minute is not odd')
    # creating wait time
    wait_time = random.randint(1,60)
    time.sleep(wait_time)






