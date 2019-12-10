#   import the random number generator
from random import randint

#   get the random number between 1 and 100 inclusive
random_number = randint(1, 100)

#   the counter for tracking trials
counter = 0

# the counter for counting trials   
while True:

    
    counter += 1
#   get the player's guess
    guess = int(input("Guess a number from 1 to 100: "))

#   if guess is in range 1 to 100
    if 1<= guess <= 100:

#   if guess is same as random number
        if guess == random_number:
            print(f'You guess RIGHT! After {counter} attempt(s)')
            break
        distance = abs(guess - random_number)
        

        if counter == 1:
            if distance <= 10:
                print("WARM")

            else:
                print("COLD")


        else:
            if distance < lasat_distance:
                    print("WARMER")

                else:
print("COLDER")

            else:
                print("OUT OF BOUND!!")

                        
            




