import numpy as np

user_input = int(input("Enter the number:- "))

table = user_input * np.arange(1, 11)

for i, value in enumerate(table, start=1):
    print(user_input, "*", i, "=", value)