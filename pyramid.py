'''
--*--
-***-
*****
is the intended goal
'''

#def pyramid():
#this will print the three lines a nested loop will help with the other part
def pyramid(n):
    j = 0
    for i in range(0,n,1):
        s =""
        j +=1
        for r in range(0,j,1):
            
            s += "*"#equivalent to index + 1
        print(' ' * (n-i), '* ' * i)
        

    # #neat one liner
    # for i in range(1,6):
    #     print(' ' * (5 - i), '* ' * i)

#Jared forced me to git good 
print("Enter stop to end program!!!")
inp = input("How big do you want the pyramid: ")
while inp != "stop":
    pyramid(int(inp))#intval is casting inp
    inp = input("How big do you want the pyramid: ")