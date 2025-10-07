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