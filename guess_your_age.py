##print("Choose(type) a number between one and ten: ")
##n=int(input())
##
##m=((n*2)+5)*50
##cb=str(input(("Have you celebrated your birthday this year? ").lower()))
##if cb=='yes':
##    cb=m+1770
##elif cb=='no':
##    cb=m+1771
##q=cb-1985
##
##qs=abs(q)%100
##print(qs)

import random
 
print("Welcome to the new and improved 'Guess My Number' game.")
print("This time you have a limited number of guesses, so guess wisely.\n")
 
 
the_number = random.randrange(100) + 1
 
guess = int(input("Take a guess: "))
tries = 1
 
 # guessing loop
while (guess != the_number):
    if tries >= 5:
        print("Out of guesses")
        break
    elif guess > the_number:
        print("Lower...")
        
    elif guess < the_number:
        print("Higher...")
 
    guess = int(input("Guess again: "))
    tries += 1
    
 
 
 # message of congratulations
print("You guessed it! The number was", the_number)
print("And it only took you", tries, "tries!\n")
