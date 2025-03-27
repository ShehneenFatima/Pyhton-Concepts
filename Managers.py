#one-Liner IF-Else(Ternary Operator)
age = 20
status = "Adult" if age>=18 else "Minor"
print(status)

#One-Liner For loop with condition
#create a list of even numbersquares only
nums = [1,2,3,4,5,6,7,8,9]
squared_events = [x**2 for x in nums if  x%2==0]
print(squared_events)

#convert list elements based on a condition
nums = [1,2,3,4,5,6,7,8,9]
labels = ["Evens" if x%2==0 else "Odds" for x in nums]
print(labels)

#Managers 
#handle different types of data storage,I/O operations, and variable scopes

#StringIO allows you to handle strings as file-like objects
#can read and write to it like a file

from io import StringIO 


file =StringIO ("Hello,this is in-memory text!") #create a  StringIO object
print(file.read()) #Read from the StringIO object
 #Write to it
file.write("\nAdding more text!")
file.seek(0) #MOve cursor back to start
print(file.read()) 


#BytesIO (Binary data in memory)
#Its like previous one but for binary data
from io import BytesIO

# Create a BytesIO object
binary_stream = BytesIO(b"Binary Data Here")

# Read binary data
print(binary_stream.read())  # Output: b'Binary Data Here'

#BUffer (handling byte streams)
buffer = memoryview(b"Hello World")
print(buffer[:5].tobytes())  # Output: b'Hello'

#Local and Global variables
# Global variable
message = "Hello from Global Scope"

def greet():
    global message  # Accessing global variable
    message = "Hello from Local Scope"  # Modifying global variable
    local_message = "Local Variable Inside Function"  # Local variable
    print(local_message)  # Output: Local Variable Inside Function

# Call function
greet()

# Print modified global variable
print(message)  # Output: Hello from Local Scope

