import random
secnum = random.randint(1,20)# set to random numb between 1 & 20
print('I am thinking of a number between 1 & 20.')
#Start of the for loop in which it will break if not guessed correct
for guessTaken in range(1,7):
    print('Take a guess.')
    guess = int(input())

    if guess < secnum:
        print('Your guess is too Low. Try again')
    elif guess > secnum:
        print('Your guess is too High. Try again')
    else:
        break
#Guess matches it is then good to go
if guess == secnum:
    print('Good jobb you got it! You guessed in ' + str(guessTaken) + ' guesses!')
else:
    print('Nice try, but the number I was thinking of was ' +str(secnum))