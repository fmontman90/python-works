catNames = []

#Start of while, As long as not breaking it will loop and keep rolling
while True:
    print('Enter the name of a cat ' + str(len(catNames) + 1) + 
          ' ( Or enter nothing to stop):')
    name = input() #accept input
    if name == '':
        break

    catNames = catNames + [name] #List concatenation
    print('The cat names are:')
    for name in catNames:
        print(' ' + name)