"""This will show example of input and 
    create a file if it is not already 
    created.    
"""
my_file = open('xmen.txt', 'w+')
my_file.write('Beast\n')
my_file.write('Cyclops\n')
my_file.writelines([
    'Nightcrawler, ',
    'Bishop, ',
    'Iceman',
])
#Flushes and closes file handle
my_file.close()

#Print out file
# alternate way this does not need .close()
# it is run behind the scenes without it being 
# in the code.
my_file = open('xmen.txt', 'r')
with my_file:
    print(my_file.read())
    