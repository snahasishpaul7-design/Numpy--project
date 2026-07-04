import numpy as np

data1 = []

data2 = []

rows = int(input("Enter rows: "))

cols = int(input("Enter cols: "))

print("Enter values for First Array")

for i in range(rows):

    row = []

    for j in range(cols):

        num = int(input("Enter the values:-"))

        row.append(num)

    data1.append(row)

print("Enter values for Second Array")

for i in range(rows):

    row = []

    for j in range(cols):

        num = int(input("Enter the values:-"))

        row.append(num)

    data2.append(row)

arr1 = np.array(data1)

arr2 = np.array(data2)

print("\nYour first array is:-", arr1)

print("\nYour second array is:-", arr2)

while True:

    user_in2 = input(
        "\nPress 1 to use calculation\n"

        "Press 2 to change the datatype of array number\n"

        "Press 3 to know the size of data\n"

        "Press 4 to know the shape\n"

        "Press 5 to convert the array into identity array\n"

        "Press 6 to know about dimension\n"

        "Press 7 to stop the program:- "
    )

    if user_in2 == "1":

        plus = int(input(
            "\nWhich operation you want to perform:-\n"
            "1.Addition\n"
            "2.Subtraction\n"
            "3.Multiplication\n"
            "4.Division\n"
            "5.Modulus\n"
            "6.Exponentiation\n"
            "7.Floor Division\n"
            "Enter your choice:- "
        ))

        if plus == 1:

            print("\nAddition of two arrays is:-", arr1 + arr2)

        elif plus == 2:

            print("\nSubtraction of two arrays is:-", arr1 - arr2)

        elif plus == 3:

            print("\nMultiplication of two arrays is:-", arr1 * arr2)

        elif plus == 4:

            print("\nDivision of two arrays is:-", arr1 / arr2)

        elif plus == 5:

            print("\nModulus of two arrays is:-", arr1 % arr2)

        elif plus == 6:

            print("\nExponentiation of two arrays is:-", arr1 ** arr2)

        elif plus == 7:

            print("\nFloor Division of two arrays is:-", arr1 // arr2)

        else:

            print("\nInvalid choice")

    elif user_in2 == "2":

        user_input = input(
            "\nWhat data type do you want to convert to? Type int, float or str only:- "
        )

        if user_input.lower() in ["int", "in", "integer"]:

            cn_arr = arr1.astype(int)

            cn_arr1 = arr2.astype(int)

            print("\n", cn_arr)

            print("\n", cn_arr1)

            print("\nConverted to int.......")

        elif user_input.lower() == "float":

            cn_arr2 = arr1.astype(float)

            cn_arr3 = arr2.astype(float)

            print("\n", cn_arr2)

            print("\n", cn_arr3)

            print("\nConverted to float.......")

        elif user_input.lower() in ["string", "str"]:

            cn_arr4 = arr1.astype(str)

            cn_arr5 = arr2.astype(str)

            print("\n", cn_arr4)

            print("\n", cn_arr5)

            print("\nConverted to string.......")

        else:

            print("\nInvalid expression")

    elif user_in2 == "3":

        print("\nFirst Array size is", arr1.size)

        print("\nSecond Array size is", arr2.size)

    elif user_in2 == "4":

        print("\nThe shape of first array is:", arr1.shape)

        print("\nThe shape of second array is:", arr2.shape)

    elif user_in2 == "5":

        iden_1 = np.eye(arr1.shape[0])

        print("\nIdentity matrix of first array:")
        print(iden_1)

        iden_2 = np.eye(arr2.shape[0])

        print("\nIdentity matrix of second array:")
        print(iden_2)

    elif user_in2 == "6":

        print("\nFirst array dimension is", arr1.ndim)

        print("\nSecond array dimension is", arr2.ndim)

    elif user_in2 == "7":

        break

#FOR BETTER UNDERSTANDING ABOUT HOW EYE AND SHAPE USE TOGETHER
#Array:
# [[ 1  2  3  4]
#  [ 5  6  7  8]
#  [ 9 10 11 12]]

# Shape of the array: (3, 4)

# Number of rows (arr1.shape[0]): 3
# Number of columns (arr1.shape[1]): 4

# Identity matrix using the number of rows:
# [[1. 0. 0.]
#  [0. 1. 0.]
#  [0. 0. 1.]]

# Identity matrix using the number of columns:
# [[1. 0. 0. 0.]
#  [0. 1. 0. 0.]
#  [0. 0. 1. 0.]
#  [0. 0. 0. 1.]]
    
  
    
    
    
    
    

    
    
    
           
        
        
        
        
    
    
