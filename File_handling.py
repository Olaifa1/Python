myfile = open('Test.txt')

contents = myfile.read()
print(contents)

##   Reading a file
fileObj = open('Test.txt', 'r')
contents = fileObj.read()
fileObj.close()


##  Write a file

##  fileObj = open('Test.txt)
##  fileObj.write("I am in Cohort 2")
##  fileObj.close()


## Write a file using "WITH" keyword

with open("cohort2/olaifa.txt", 'w+') as myfile:
               myfile.write('I am a humble guy')
               myfile.seek(0)
               contents1 = myfile.read()
               print(contents1)
               
