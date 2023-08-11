#EOL,End Of Line characters like {,}use for terminating lines of a file
#opening a file ,we use open(),inside the parenthesis we specify the mode whic shows the the purpose of opening it
"""
r: open an existing file for a read operation.
w: open an existing file for a write operation. If the file already contains some data then it will be overridden but if the file is not present then it creates the file as well.
a:  open an existing file for append operation. It won’t override existing data.
 r+:  To read and write data into the file. The previous data in the file will be overridden.
w+: To write and read data. It will override existing data.
a+: To append and read data from the file. It won’t override existing data
"""

f = open('cathy.txt','r')
print(f.read())
f.close()
#using the split()function to split lines
with open("cathy.txt", "r") as file:
    data = file.readlines()
    for line in data:
        word = line.split()
        print (word)
        #creating a file using the write()function
        with open("cathy.txt", "w") as file:
            file.write("Hello World")
            f.close()
            #
            import os

try:
    # Open file for reading
    file = open("data.txt", "r")
    content = file.read()
    print(f"Contents of the file: {content}")

    # Split content into lines
    lines = content.split("\n")
    print(f"Number of lines in the file: {len(lines)}")

    # Remove the file
    os.remove("data.txt")
    print("File successfully removed.")

except FileNotFoundError:
    print("Error: The specified file does not exist.")
except PermissionError:
    print("Error: Permission denied. Unable to access the file.")
except IOError:
    print("Error: An input/output error occurred.")
except Exception as e:
    print(f"Error: {str(e)}")

finally:
    # Close the file (if it was successfully opened)
    if "file" in locals() and not file.closed:
        file.close()
#in summary
import os

try:
    # Open file for reading
    file = open("data.txt", "r")
    content = file.read()
    print(f"Contents of the file: {content}")

    # Split content into lines
    lines = content.split("\n")
    print(f"Number of lines in the file: {len(lines)}")

    # Remove the file
    os.remove("data.txt")
    print("File successfully removed.")

except FileNotFoundError:
    print("Error: The specified file does not exist.")
except PermissionError:
    print("Error: Permission denied. Unable to access the file.")
except IOError:
    print("Error: An input/output error occurred.")
except Exception as e:
    print(f"Error: {str(e)}")

finally:
    # Close the file (if it was successfully opened)
    if "file" in locals() and not file.closed:
        file.close()

