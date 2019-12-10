##  A programm that guess the square root of any number provided by the User
##  Guess the square root of the number
##  Divide the working number by the guess
##  Average the quotient(from2) and the guess.
##  Make the new guess the average from step 3.
##  If the new guess is "sufficiently different from the old guess, go back to step2, else halt.


##  import the random integer generator
from random import randint

##  Prompt user to enter the number, colect with keyword input, cast from string to int and assign to variable n
number = int(input("Enter the number: "))

##  prompt user to guess the square root of n
guess = randint(1, number)

##  The closeness of the square root to actual number
difference = 1;

##  Keep running until closenes is achieved
while difference > 0.0001:
    
    ##   Find the quotient
    quotient = number / guess

    ##  find the Average of the quotient and the guess
    new_guess = (quotient + guess)/ 2

    ##   Check the closenes
    difference = abs(guess - new_guess)
    
    ##  update the guess
    guess = new_guess

    ##  display the square root number
    print("Square root is %0.2f"% guess)
    

            

        
