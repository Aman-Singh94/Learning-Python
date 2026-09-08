read=open("file1.txt","r")
#print(read.read())  
print(read.readline())  # This will read the first line of the file
read.close()
 #it is important to close the file after reading it to free up system resources.

# We only read the file and print the content of the file, which is in the folder of python(main folder).
#read1=open(r"C:\python's file\file1.txt","r")
#print(read.read())


