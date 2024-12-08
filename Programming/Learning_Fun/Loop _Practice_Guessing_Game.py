import random

number= random.randint(1,20)
#Create random number

guess= int(input('Guess a number between 1 and 20: '))
#Get initial guess from user

number_of_guesses = 1
#create a count

while number != guess: 
    number_of_guesses+= 1

    if number_of_guesses > 10: 
        break 
    #break after 10 guesses

    guess = int(input('Try again! Enter you new number here: '))
    

    
if number_of_guesses > 10: 
    print(f'Sorry, you took too many guesses. The number was {number}. ')
else:

    print(f'You got it, Congrats! You took {number_of_guesses} guess(es)!')