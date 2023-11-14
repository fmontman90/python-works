#This is meant to show functions and global variable 
# as well as local variable example
def spam():
    eggs = 'spam local'
    print(eggs) #will print spam local

def bacon():
    eggs = 'bacon local too'
    print(eggs) #prints bacon local
    spam()
    print(eggs) #prints bacon local

def cheese():
    global eggs #allowing for modify of global variable within function
    eggs = 'cheese'
    print(eggs)

eggs = 'global'
bacon()
print(eggs) #prints global
cheese() #prints cheese from function
