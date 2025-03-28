writing to file
with open("sample.txt","w") as file :
     file.write("Hello,welcome to file-handling in python!\n")
     file.write("This is the first line.\n")
     file.write("Lets master file handling!\n")


#Reading from the file 
print("Reading initial content:")
with open ("sample.txt", "r") as file:
     print(file.read())

#Appending to the file
with open("sample.txt","a") as file:
     file.write("Appending a new line to the file.\n")

#Reading updated content
print("\nReading updated content:")
with open ("sample.txt", "r") as file:
     print(file.read())
