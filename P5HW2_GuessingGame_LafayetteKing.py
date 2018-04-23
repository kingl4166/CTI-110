
# Guess the secret number
# 4/20/2018
# CTI-110 P5HW2-Random Number Guessing Game
# Lafayette King
#

# use the random module
import random

def main():
    guess = 1
   


 
 
 

again = "Y"
secret_number = random.randint(1, 100)
guess = 1
guesses = 1

print("Guess the secret number! ")

while guess != secret_number:
  
   guess =int(input("is it... "))
   guesses = guesses + 1
   if guess == secret_number:
         
         print("You are correct !! , Great Job!!")
         print("It only took you",guesses, "guesses!") 

   elif guess > secret_number:
        print("Too high, try again.")
     
        
   elif guess < secret_number:
         print("You are too low , try again!!")
         
   if guesses > 10:
        print("Nice try, ")
        again=input("Play again? (y = yes):")



       
       
   

   

    
       
           


      
main()
