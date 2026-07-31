import numpy as np  # Import NumPy library, used for creating and managing arrays

arrays = {}  # Dictionary that stores all arrays created by the user, using array name as key

# ---------- STEP 1: CREATE ARRAY ----------
print("1. 1D Array")
print("2. 2D Array")
choice = input("Enter Choice: ")  # Ask user whether they want a 1D or 2D array

if choice == "1":
    name = input("Enter Array Name: ")  # Name used to store/find this array later
    size = int(input("How many elements: "))  # Total number of elements in the 1D array
    data = []  # Temporary list to collect the entered values
    for i in range(size):
        value = int(input(f"Element {i+1}: "))  # Take one element at a time from user
        data.append(value)  # Add the entered value into the list
    arrays[name] = np.array(data)  # Convert the list into a NumPy array and save it
    print("\n1D Array Created Successfully.")

elif choice == "2":
    name = input("Enter Array Name: ")
    rows = int(input("Enter Rows: "))  # Number of rows for the 2D array
    cols = int(input("Enter Columns: "))  # Number of columns for the 2D array
    data = []  # Temporary list of lists (will hold each row)
    for i in range(rows):
        row = []  # Temporary list to hold one row's values
        print(f"Enter values for Row {i+1}")
        for j in range(cols):
            value = int(input(f"Element [{i}][{j}]: "))  # Take value for each cell
            row.append(value)
        data.append(row)  # Add the completed row into the main data list
    arrays[name] = np.array(data)  # Convert list of lists into a 2D NumPy array
    print("\n2D Array Created Successfully.")

else:
    print("Invalid Choice")
    exit()  # Stop the program if the choice is invalid

# ---------- STEP 2: SHOW ALL CREATED ARRAYS ----------
print("\nAll Arrays")
for n, a in arrays.items():  # Loop through every array stored in the dictionary
    print("Array Name:", n)
    print(a)

arr = arrays[name]  # This is the "active" array that all menu operations below will work on

# ---------- STEP 3: MENU LOOP ----------
while True:
    print("\n===== MENU =====")
    print("1. Show Array")
    print("2. Append")
    print("3. Insert")
    print("4. Delete")
    print("5. Slice")
    print("6. Stack")
    print("7. Split")
    print("8. Concatenate")
    print("9. Add (Arithmetic)")
    print("10. Exit")
    user_input = int(input("Enter choice: "))  # Read the menu option chosen by user

    # ---------- 1. SHOW ----------
    if user_input == 1:
        print("\nCurrent Array:")
        print(arr)  # Simply print the current state of the array

    # ---------- 2. APPEND ----------
    elif user_input == 2:
        if arr.ndim == 1:  # Check if the array is 1D
            val = int(input("Enter value: "))
            arr = np.append(arr, val)  # Add one value to the end of the 1D array
            arrays[name] = arr  # Update dictionary with the new array
            print(arr)
        else:  # Array is 2D
            print("1. Append Row")
            print("2. Append Column")
            app = input("Choice: ")
            if app == "1":
                row = []  # New row to be added at the bottom
                for i in range(arr.shape[1]):  # Loop equal to number of columns
                    val = int(input(f"Column {i+1}: "))
                    row.append(val)
                arr = np.append(arr, [row], axis=0)  # axis=0 means add as a new row
                arrays[name] = arr
                print(arr)
            elif app == "2":
                col = []  # New column to be added at the right side
                for i in range(arr.shape[0]):  # Loop equal to number of rows
                    val = int(input(f"Row {i+1}: "))
                    col.append([val])
                arr = np.append(arr, col, axis=1)  # axis=1 means add as a new column
                arrays[name] = arr
                print(arr)
            else:
                print("Invalid Choice")

    # ---------- 3. INSERT ----------
    elif user_input == 3:
        if arr.ndim == 1:
            index = int(input("Enter index: "))  # Position where the new value goes
            value = int(input("Enter value: "))
            arr = np.insert(arr, index, value)  # Insert value at the given index
            arrays[name] = arr
            print(arr)
        else:
            print("1. Insert Row")
            print("2. Insert Column")
            ope = int(input("Choice: "))
            if ope == 1:
                index = int(input("Row Index: "))  # Position where the new row goes
                row = []
                for i in range(arr.shape[1]):
                    value = int(input(f"Column {i+1}: "))
                    row.append(value)
                arr = np.insert(arr, index, [row], axis=0)  # Insert row at given index
                arrays[name] = arr
                print(arr)
            elif ope == 2:
                index = int(input("Column Index: "))  # Position where the new column goes
                col = []
                for i in range(arr.shape[0]):
                    value = int(input(f"Row {i+1}: "))
                    col.append(value)
                arr = np.insert(arr, index, np.array(col), axis=1)  # Insert column at given index
                arrays[name] = arr
                print(arr)
            else:
                print("Invalid Choice")

    # ---------- 4. DELETE ----------
    elif user_input == 4:
        if arr.ndim == 1:
            index = int(input("Enter index to delete: "))  # Position of element to remove
            arr = np.delete(arr, index)  # Remove element at that index
            arrays[name] = arr
            print(arr)
        else:
            print("1. Delete Row")
            print("2. Delete Column")
            dele = input("Choice: ")
            if dele == "1":
                index = int(input("Row Index: "))
                arr = np.delete(arr, index, axis=0)  # axis=0 means delete a whole row
                arrays[name] = arr
                print(arr)
            elif dele == "2":
                index = int(input("Column Index: "))
                arr = np.delete(arr, index, axis=1)  # axis=1 means delete a whole column
                arrays[name] = arr
                print(arr)
            else:
                print("Invalid Choice")

    # ---------- 5. SLICE ----------
    elif user_input == 5:
        if arr.ndim == 1:
            start = int(input("Start Index: "))  # Starting index (included)
            end = int(input("End Index: "))  # Ending index (excluded)
            print("Sliced Array:")
            print(arr[start:end])  # Standard Python slicing on a 1D array
        else:
            r1 = int(input("Row Start: "))
            r2 = int(input("Row End: "))
            c1 = int(input("Column Start: "))
            c2 = int(input("Column End: "))
            print("Sliced Array:")
            print(arr[r1:r2, c1:c2])  # Slice rows and columns together

    # ---------- 6. STACK ----------
    elif user_input == 6:
        print("1. Vertical Stack (vstack)")
        print("2. Horizontal Stack (hstack)")
        stk = input("Choice: ")
        if arr.ndim == 1:
            print(f"Enter {arr.shape[0]} values for the new array to stack:")
            new_data = []
            for i in range(arr.shape[0]):  # New array must be same length to stack
                val = int(input(f"Element {i+1}: "))
                new_data.append(val)
            new_arr = np.array(new_data)
            if stk == "1":
                arr = np.vstack((arr, new_arr))  # Places two 1D arrays as rows -> result becomes 2D
                print("Note: Array is now 2D after vertical stack.")
            elif stk == "2":
                arr = np.hstack((arr, new_arr))  # Joins two 1D arrays end-to-end into one longer 1D array
            else:
                print("Invalid Choice")
            arrays[name] = arr
            print(arr)
        else:
            if stk == "1":
                cols = arr.shape[1]
                print(f"Enter values for the new row, must have {cols} columns:")
                new_row = []
                for i in range(cols):
                    val = int(input(f"Column {i+1}: "))
                    new_row.append(val)
                arr = np.vstack((arr, new_row))  # Adds new row below the existing 2D array
            elif stk == "2":
                rows = arr.shape[0]
                print(f"Enter values for the new column, must have {rows} rows:")
                new_col = []
                for i in range(rows):
                    val = int(input(f"Row {i+1}: "))
                    new_col.append([val])
                arr = np.hstack((arr, new_col))  # Adds new column beside the existing 2D array
            else:
                print("Invalid Choice")
            arrays[name] = arr
            print(arr)

    # ---------- 7. SPLIT ----------
    elif user_input == 7:
        if arr.ndim == 1:
            parts = int(input("Split into how many parts: "))
            result = np.array_split(arr, parts)  # Splits 1D array into 'parts' near-equal pieces
            for i, p in enumerate(result):
                print(f"Part {i+1}:", p)
        else:
            print("1. Split by Row")
            print("2. Split by Column")
            sp = input("Choice: ")
            parts = int(input("Split into how many parts: "))
            if sp == "1":
                result = np.array_split(arr, parts, axis=0)  # Splits 2D array row-wise
            elif sp == "2":
                result = np.array_split(arr, parts, axis=1)  # Splits 2D array column-wise
            else:
                print("Invalid Choice")
                result = []
            for i, p in enumerate(result):
                print(f"Part {i+1}:")
                print(p)

    # ---------- 8. CONCATENATE ----------
    elif user_input == 8:
        if arr.ndim == 1:
            size2 = int(input("How many elements in new array: "))
            new_data = []
            for i in range(size2):
                val = int(input(f"Element {i+1}: "))
                new_data.append(val)
            new_arr = np.array(new_data)
            arr = np.concatenate((arr, new_arr))  # Joins two 1D arrays into one, back-to-back
        else:
            print("1. Concatenate Row-wise (axis=0)")
            print("2. Concatenate Column-wise (axis=1)")
            ax = input("Choice: ")
            if ax == "1":
                cols = arr.shape[1]
                print(f"Enter one new row with {cols} values:")
                new_row = []
                for i in range(cols):
                    val = int(input(f"Column {i+1}: "))
                    new_row.append(val)
                arr = np.concatenate((arr, [new_row]), axis=0)  # Adds row at the bottom
            elif ax == "2":
                rows = arr.shape[0]
                print(f"Enter one new column with {rows} values:")
                new_col = []
                for i in range(rows):
                    val = int(input(f"Row {i+1}: "))
                    new_col.append([val])
                arr = np.concatenate((arr, new_col), axis=1)  # Adds column at the right side
            else:
                print("Invalid Choice")
        arrays[name] = arr
        print(arr)

    # ---------- 9. ADD (ARITHMETIC) ----------
    elif user_input == 9:
        print("1. Add Scalar to Every Element")
        print("2. Add Another Array (Element-wise)")
        adc = input("Choice: ")
        if adc == "1":
            scalar = int(input("Enter number to add: "))
            arr = arr + scalar  # NumPy adds this number to every single element automatically
        elif adc == "2":
            if arr.ndim == 1:
                print(f"Enter {arr.shape[0]} values for the array to add:")
                new_data = []
                for i in range(arr.shape[0]):
                    val = int(input(f"Element {i+1}: "))
                    new_data.append(val)
                new_arr = np.array(new_data)
                arr = arr + new_arr  # Element-wise addition; both arrays must be the same shape
            else:
                print(f"Enter values for a {arr.shape[0]}x{arr.shape[1]} array to add:")
                new_data = []
                for i in range(arr.shape[0]):
                    row = []
                    for j in range(arr.shape[1]):
                        val = int(input(f"Element [{i}][{j}]: "))
                        row.append(val)
                    new_data.append(row)
                new_arr = np.array(new_data)
                arr = arr + new_arr  # Element-wise addition for two 2D arrays of the same shape
        else:
            print("Invalid Choice")
        arrays[name] = arr
        print(arr)

    # ---------- 10. EXIT ----------
    elif user_input == 10:
        print("Program Ended.")
        break

    else:
        print("Invalid Choice")