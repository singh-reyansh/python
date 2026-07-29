# if else Match 
# 
# Input -- 34 , 23.5 ,  True , #5 
# recursion -- 1000 
# Invalid Operations -- 4 / 0 
# Memory Issues -- 
# Hardware Issues 


# try except finally each 

# try -- you try this specific block of code -- This is the actual code that I want to run 
# try:
#     print(x)
# except:
#     print("There is an error")
# x = "Python"
# try:
#   print("Hello")
# except:
#   print("Something went wrong")
# else:
#   print("Nothing went wrong")

# finally:
#   logic to close the file , database connection

# finally -- finally will always get executed -- even if there is an error or not.

# Resources -- file (text , json,csv) , Database etc. 
'''
try:
    first = int(input("Enter first number: "))
    second = int(input("Enter second number: "))
    print(first + second)
except:
    print("There is an error.")
else:
    print("Working fine.")
finally:
    print("Connections closed successfully!")
'''



def main():
    # 1. Invalid number input
    print("\n1. Invalid Number (ValueError)")
    try:
        num = int(input("Enter a number: "))
        print(f"You entered: {num}")
    except ValueError:
        print("Error: Not a valid integer!")

    # 2. Division by zero
    print("\n2. Division by Zero")
    try:
        x = 10 / int(input("Divide 10 by: "))
    except ZeroDivisionError:
        print("Error: Cannot divide by zero!")
    except ValueError:
        print("Error: Please enter a number.")
    else:
        print(f"Result: {x}")

    # 3. Variable not defined
    print("\n3. Undefined Variable (NameError)")
    try:
        print(undefined_var)
    except NameError:
        print("Error: Variable not defined!")

    # 4. Wrong data type operation
    print("\n4. TypeError (string + number)")
    try:
        result = "Age: " + 25
    except TypeError:
        print("Error: Cannot add string and integer!")
        result = f"Age: {25}"
        print("Fixed:", result)

    # 5. List index out of range
    print("\n5. IndexError")
    fruits = ["apple", "banana"]
    try:
        print(fruits[5])
    except IndexError:
        print("Error: Index out of range!")

    # 6. Key not in dictionary
    print("\n6. KeyError")
    user = {"name": "Alice", "age": 30}
    try:
        print(user["email"])
    except KeyError:
        print("Error: 'email' not found in user data.")

    # 7. File not found
    print("\n7. FileNotFoundError")
    try:
        with open("missing.txt", "r") as f:
            print(f.read())
    except FileNotFoundError:
        print("Error: File 'missing.txt' does not exist.")

    # 8. Permission error (simulate)
    print("\n8. PermissionError")
    try:
        with open("/root/secret.txt", "r") as f:
            print(f.read())
    except PermissionError:
        print("Error: Permission denied!")
    except FileNotFoundError:
        print("Error: File not found (or no access).")

    # 9. Safe file read with cleanup
    print("\n9. Safe File Read + Finally")
    file = None
    try:
        file = open("notes.txt", "w")
        file.write("Hello from Python!\n")
        print("Data written.")
    except Exception as e:
        print(f"Error: {e}")
    else:
        print("Write successful.")
    finally:
        if file and not file.closed:
            file.close()
            print("File closed safely.")

    # 10. Multiple exceptions + else + finally
    print("\n10. Full Structure: try-except-else-finally")
    try:
        value = int(input("Enter a positive number: "))
        if value < 0:
            raise ValueError("Number is negative!")
        result = 100 / value
    except ValueError as ve:
        print(f"Value Error: {ve}")
    except ZeroDivisionError:
        print("Error: Cannot divide by zero.")
    except Exception as e:
        print(f"Unexpected error: {e}")
    else:
        print(f"Success! 100 ÷ {value} = {result}")
    finally:
        print("Operation completed.\n")


if __name__ == "__main__":
    main()
