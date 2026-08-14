import numpy as np


def create_array():
    """Create a new 1D or 2D array from user input. Returns (name, array)."""
    print("1. 1D Array")
    print("2. 2D Array")
    choice = input("Enter Choice: ")
    name = input("Enter Array Name: ")

    if choice == "1":
        size = int(input("How many elements: "))
        data = []
        for i in range(size):
            value = int(input(f"Element {i+1}: "))
            data.append(value)
        arr = np.array(data)
        print("\n1D Array Created Successfully.")

    elif choice == "2":
        rows = int(input("Enter Rows: "))
        cols = int(input("Enter Columns: "))
        data = []
        for i in range(rows):
            row = []
            print(f"Enter values for Row {i+1}")
            for j in range(cols):
                value = int(input(f"Element [{i}][{j}]: "))
                row.append(value)
            data.append(row)
        arr = np.array(data)
        print("\n2D Array Created Successfully.")

    else:
        print("Invalid Choice")
        return None, None

    return name, arr


def show_array(name, arr):
    print(f"\nArray Name: {name}")
    print(arr)


def append_value(arr):
    if arr.ndim == 1:
        val = int(input("Enter value to append: "))
        arr = np.append(arr, val)
        print("\nValue appended successfully.")

    else:
        print("For add row wise press 1")
        print("For add column wise press 2")
        choice = int(input("Enter your choice: "))

        if choice == 1:
            row = []
            for i in range(arr.shape[1]):
                value = int(input(f"Enter value for column {i+1}: "))
                row.append(value)
            arr = np.append(arr, [row], axis=0)
            print("\nRow added successfully.")

        elif choice == 2:
            col = []
            for i in range(arr.shape[0]):
                value = int(input(f"Enter value for row {i+1}: "))
                col.append(value)
            col = np.array(col).reshape(-1, 1)
            arr = np.append(arr, col, axis=1)
            print("\nColumn added successfully.")

        else:
            print("Invalid choice.")

    print(arr)
    return arr


def insert_value(arr):
    if arr.ndim == 1:
        index = int(input("Enter index to insert: "))
        value = int(input("Enter value to insert: "))
        arr = np.insert(arr, index, value)
        print("\nValue inserted successfully.")

    else:
        print("For insert row wise press 1")
        print("For insert column wise press 2")
        choice = int(input("Enter your choice: "))

        if choice == 1:
            index = int(input("Enter index to insert: "))
            row = []
            for i in range(arr.shape[1]):
                value = int(input(f"Enter value for column {i+1}: "))
                row.append(value)
            arr = np.insert(arr, index, row, axis=0)
            print("\nRow inserted successfully.")

        elif choice == 2:
            index = int(input("Enter index to insert: "))
            col = []
            for i in range(arr.shape[0]):
                value = int(input(f"Enter value for row {i+1}: "))
                col.append(value)
            arr = np.insert(arr, index, col, axis=1)
            print("\nColumn inserted successfully.")

        else:
            print("Invalid choice.")

    print(arr)
    return arr


def delete_value(arr):
    if arr.ndim == 1:
        index = int(input("Enter index to delete: "))
        arr = np.delete(arr, index)
        print("\nValue deleted successfully.")

    else:
        print("For delete row wise press 1")
        print("For delete column wise press 2")
        choice = int(input("Enter your choice: "))

        if choice == 1:
            index = int(input("Enter row index to delete: "))
            arr = np.delete(arr, index, axis=0)
            print("\nRow deleted successfully.")

        elif choice == 2:
            index = int(input("Enter column index to delete: "))
            arr = np.delete(arr, index, axis=1)
            print("\nColumn deleted successfully.")

        else:
            print("Invalid choice.")

    print(arr)
    return arr


def slice_array(arr):
    if arr.ndim == 1:
        start = int(input("Enter start index: "))
        end = int(input("Enter end index: "))
        print("\nSliced Array:")
        print(arr[start:end])

    else:
        row_start = int(input("Enter row start index: "))
        row_end = int(input("Enter row end index: "))
        col_start = int(input("Enter column start index: "))
        col_end = int(input("Enter column end index: "))
        print("\nSliced Array:")
        print(arr[row_start:row_end, col_start:col_end])


def stack_arrays(arr):
    print("\nEnter the second array to stack with:")
    _, arr2 = create_array()
    if arr2 is None:
        return arr

    print("For horizontal stack press 1")
    print("For vertical stack press 2")
    choice = int(input("Enter your choice: "))

    if choice == 1:
        result = np.hstack((arr, arr2))
    elif choice == 2:
        result = np.vstack((arr, arr2))
    else:
        print("Invalid choice.")
        return arr

    print("\nStacked Array:")
    print(result)
    return result


def split_array(arr):
    parts = int(input("Enter number of parts to split into: "))

    if arr.ndim == 1:
        result = np.array_split(arr, parts)
    else:
        print("For row wise split press 1")
        print("For column wise split press 2")
        choice = int(input("Enter your choice: "))

        if choice == 1:
            result = np.array_split(arr, parts, axis=0)
        elif choice == 2:
            result = np.array_split(arr, parts, axis=1)
        else:
            print("Invalid choice.")
            return

    print("\nSplit Result:")
    for i, part in enumerate(result):
        print(f"Part {i+1}:")
        print(part)


def concatenate_arrays(arr):
    print("\nEnter the second array to concatenate with:")
    _, arr2 = create_array()
    if arr2 is None:
        return arr

    if arr.ndim == 1:
        result = np.concatenate((arr, arr2))
    else:
        axis = int(input("Enter axis (0 for row, 1 for column): "))
        result = np.concatenate((arr, arr2), axis=axis)

    print("\nConcatenated Array:")
    print(result)
    return result

def main():
    arrays = {}

    name, arr = create_array()
    if arr is None:
        return
    arrays[name] = arr

    print("\nAll Arrays")
    for n, a in arrays.items(): #n is key  and a is value
        print("Array Name:", n) 
        print(a)

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
        print("9. Exit")
        user_input = int(input("Enter choice: "))

        if user_input == 1:
            show_array(name, arr)
        elif user_input == 2:
            arr = append_value(arr)
            arrays[name] = arr
        elif user_input == 3:
            arr = insert_value(arr)
            arrays[name] = arr
        elif user_input == 4:
            arr = delete_value(arr)
            arrays[name] = arr
        elif user_input == 5:
            slice_array(arr)
        elif user_input == 6:
            arr = stack_arrays(arr)
            arrays[name] = arr
        elif user_input == 7:
            split_array(arr)
        elif user_input == 8:
            arr = concatenate_arrays(arr)
            arrays[name] = arr
      
        elif user_input == 9:
            print("Exiting program. Bye!")
            break
        else:
            print("Invalid choice. Try again.")


if __name__ == "__main__":
    main()