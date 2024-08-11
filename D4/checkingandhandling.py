# acivity for errors
fileName = input("Please enter hte name of the file you would like to read: ")
myfile = open(fileName, 'r') # Open a file for reading.
contents = myfile.readlines() # Read in the content by line.
myfile.close() # Explicitly close the file
print(contents) #print the contents of the file

'''
test code:

f = FileManipulator("tmp.txt")
print(f.contents)
f.reverse("tmp2.txt")
'''

2. Error Handling
Your task for this activity is to complete the program by gracefully handling any errors that might come your way. There are many ways to do this, but for this activity you will be creating a class to manipulate files, called FileManipulator. To successfully create this class, complete the following steps:

Create the FileManipulator class and implement the constructor. The constructor should accept the name of a file to read in and should continually prompt for input if the name given causes an error. Make sure that you give an informative message if an error is raised.