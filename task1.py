# EXCEPTION HANDLING
print("\nEXCEPTION HANDLING")
try:
    # Intentionally raise an error.
    print("Trying Dividing by 0")
    x = 1 / 0
except ZeroDivisionError as e:
    # Except clause:
    print("Error occurred:", e)
finally:
    # Finally clause:
    print("Terminating the program")



# FILE HANDLING
print("\nFILE HANDLING")
try:
   file = open("test.txt",'r')

   # Reading the entire file
   print("Read entire file")
   print(file.read())
   
   # Bringing the file cursor to initial position
   print("\nBring the cursor to initial position")
   print(file.seek(0))

   # Reading the 6 characters in the file starting at the cursor
   print("\nRead only 6 characters starting at the cursor")
   print(file.read(6))

   # Command to know the current position of the cursor
   print("\nPrint the current cursor in the file")
   print(file.tell())

   # Reading a single line in the file
   print("\nRead a single line in the file starting at the cursor")
   print(file.readline())

except:
	print("Error occured")

finally:
   file.close()