import random
play_again = "y"
guess_amount = 0
user_guess = 12
#while user has pressed "y"
while play_again == "y":
    #the computer genereates a random number between 1 and 100
    random_int = random.randint(1, 100)
    #while the user has not guessed the number
    while user_guess != random_int:
        #ask the user to guess the number between 1 and 100
        user_guess = float(input("Guess a number between 1 and 100: "))
        #if the guess is < 1 or > 100 
        #   Print "Invalid guess. Please Try Again"
        if user_guess < 1 or user_guess > 100:
            print("\nInvalid guess. Please Try Again")
        #Increment the number of guesses  
        else:
            guess_amount += 1
        #if the guess it greater than the number 
        #   print "lower"
        if user_guess > random_int and user_guess < 101:
            print("\nThe number is lower, guess again!")
        #if the guess ie less than then number
        #   print "higher"
        elif user_guess < random_int and user_guess > 0:
            print("\nThe number is higher, guess again!")
        #if the guess is equal to the number
        #   print "Congradulations"
        elif user_guess == random_int:
            print("\nCongratulations!")

    #loop ends

    #Print the number of guesses
    print(f"\nYou guessed the number in {guess_amount} guesses.")
    #if number of guesses is  <= 3
    #   Print "You are amazing!"
    if guess_amount <= 3:
        print("Amazing!")
    #elif number of guesses <= 5
    elif guess_amount <=5:
        print("\nImpressive!")
    #   Print "Impressive"
    #elif number of guesses <= 7
    elif guess_amount <= 7:
        print("\nGood job!")
    #   Print "Good job!"
    #el if number of guesses <= 9
    elif guess_amount <= 9:
        print("\nTook a little longer, but you got there!")
    #   print "took a little longer, but you got it!"
    #else if number of guesses >=10
    elif guess_amount >= 10:
        print("\nYou need to lock in")
    #print  "You need to lock in"

    #ask user to press "y" if they want to play again 
    play_again = input("Do you want to play again? Type y for yes, or any other key for no: ")
    user_guess = 101
    guess_amount = 0
#loop