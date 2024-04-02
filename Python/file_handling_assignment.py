# File Creation
try:
    # Creating a new text file named "my_file.txt" in write mode ('w')
    with open("my_file.txt", "w") as file:
        # Code to Write at least three lines of text to the file
        file.write("This is line 1.\n")
        file.write("1234\n")  # Writing a number as well
        file.write("Line 3: Writing numbers and strings mix.\n")
except PermissionError as e:
    print("Permission denied:", e)
except Exception as e:
    print("An error occurred:", e)
finally:
    print("File creation process complete.")

# File Reading and Display
try:
    # Open "my_file.txt" in read mode ('r')
    with open("my_file.txt", "r") as file:
        # Read the contents of the file
        file_contents = file.read()
        # Display the contents on the console
        print("Contents of my_file.txt:")
        print(file_contents)
except FileNotFoundError:
    print("File not found. Please make sure the file exists.")
except PermissionError as e:
    print("Permission denied:", e)
except Exception as e:
    print("An error occurred:", e)

# File Appending
try:
    # Open "my_file.txt" in append mode ('a')
    with open("my_file.txt", "a") as file:
        # Appending three additional lines of text to the existing content
        file.write("This is line 4 (appended).\n")
        file.write("5678\n")  # Writing a number as well
        file.write("Line 6: Appending numbers and strings mix.\n")
except PermissionError as e:
    print("Permission denied:", e)
except Exception as e:
    print("An error occurred:", e)
finally:
    print("File appending process complete.")
