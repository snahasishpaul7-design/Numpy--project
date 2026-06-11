
#now we need to use arange function

#arange(start,stop, step)

import numpy as np
user_input = input("Do you want to  create sequence of number:-").lower()

if user_input == "yes":
 

    start = int(input("Start: "))
    stop = int(input("Stop: "))
    step = int(input("Step: "))

    arr = np.arange(start, stop, step)

    print("Generated Array:")
    print(arr)
elif user_input =="no":
    exit()

else:
    print("Invalid expression")
    