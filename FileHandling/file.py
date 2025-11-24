# ---------------------------------------------------------
# Why do we need to work with files
# ---------------------------------------------------------
# A program keeps all of its variables in RAM.
# RAM is volatile memory. This means when the program stops,
# everything stored in RAM is cleared.
# To keep data permanently we need files or databases.
# Files can store text, numbers, logs, results or any form of
# long-term information.
#
# Examples of files: txt, csv, json
# A file is a resource. So when we open a file, we must close it.
# ---------------------------------------------------------


# ---------------------------------------------------------
# Reading a File
# ---------------------------------------------------------

# Opening a file in read mode
try:
    file = open('myTextFile.txt', 'r')
    print("File object:", file)

    # Read entire content
    print("Full content:")
    print(file.read())

    # Move pointer back to start for next read
    file.seek(0)

    # Read specific number of characters
    print("First 7 characters:")
    print(file.read(7))

    # Move pointer back to start again
    file.seek(0)

    # Reading line by line
    print("Reading 3 lines:")
    for i in range(3):
        print(file.readline().strip())

    # Move pointer back to start again
    file.seek(0)

    # Read all lines as a list
    print("List of all lines:")
    print(file.readlines())

    # Accessing first line from readlines
    file.seek(0)
    print("First line using readlines indexing:")
    print(file.readlines()[0])

    file.close()

except FileNotFoundError:
    print("myTextFile.txt not found. Please create it first.")


# ---------------------------------------------------------
# Writing to a File
# ---------------------------------------------------------

try:
    file = open('myTextFile.txt', 'w')
    file.write("I am adding new line.")
    file.close()
    print("Write mode completed successfully.")

except Exception as e:
    print("Write error:", e)


# ---------------------------------------------------------
# Appending to a File
# ---------------------------------------------------------

try:
    file = open('myTextFile2.txt', 'a')
    file.write("\nI am adding second line.")
    file.close()
    print("Append mode completed successfully.")

except Exception as e:
    print("Append error:", e)


# ---------------------------------------------------------
# Deleting a File
# ---------------------------------------------------------

import os

# Uncomment to delete
# os.remove('myTextFile2.txt')
# print("myTextFile2.txt deleted.")


# ---------------------------------------------------------
# Removing Empty Folders
# ---------------------------------------------------------

try:
    os.removedirs('FileDemo')  # Only removes if all folders inside are empty
    print("Empty folder FileDemo removed.")
except FileNotFoundError:
    print("Folder FileDemo not found.")
except OSError:
    print("Folder FileDemo is not empty, so it cannot be removed.")


# ---------------------------------------------------------
# Removing Non-Empty Folders
# ---------------------------------------------------------

# os.rmdir('FileDemo')
# print("Non-empty folder removed.")