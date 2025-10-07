# Task 1: Read a File and Handle Errors 


a = "sample.txt"  # Change to your file name

try:
    with open(a, "r") as f:
        b = f.read()
        print(b)
except FileNotFoundError:
    print(f"Error: The file '{a}' was not found.")
except Exception as e:

    print(f"An error occurred: {e}")

    

#task 2: Write and Append Data to a File

    filename = "sample.txt"

    try:
        with open(filename, "w") as f:
            f.write("This is the first line.\n")
            f.write("This is the second line.\n")
        print("Data written to file successfully.")
    except Exception as e:
        print(f"An error occurred while writing: {e}")

    # Append data to the file
    try:
        with open(filename, "a") as f:
            f.write("This is an appended line.\n")
        print("Data appended to file successfully.")
    except Exception as e:
        print(f"An error occurred while appending: {e}")

