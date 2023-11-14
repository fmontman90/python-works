import os
#The file gets appended to a specified location in this case the workspace

f = open('fillin.txt', 'a') # the a is for append to the file
f.write('Add to file woot')
f.close()
#Print the contents of the file created 
f = open('fillin.txt', 'r')
print(f.read())