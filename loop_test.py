'''The goal of this is to print stars in increasing descending order
The below loop will show how it should look.
def print_stars(count):
    for i in range(1, count):
        print('*' * i
print_stars(6)'''

# In the for loop ( 0 , 5, 1) is doing this below
# (0 = start value, 5 = end value, 1= increment value) if you add a two at end will change the value
# Try adding a two in the 1's place to see what the change is.
# What could you adjust to print a ladder effect?
'''for i in range(0, 5, 1):
    s = ""
    j =1

    for r in range(0, j, 1):
        s += "*"
    print(s)'''

'''The adjustment we initialize j before the first loop then whe alter j=1 to 
j +=1'''
j = 0
for i in range(0, 5, 1):
    s = ""
    j += 1

    for r in range(0, j, 1):
        s += "*"
    print(s)