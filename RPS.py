import random
from DetermineWinner import winner
from insult import insult
#Declaring scoring variables
playerCounter = 0
computerCounter = 0
#creating def to decide action of user and computer
def action():
    #Creating array of possible actions
    possible_action = ["r","p","s"]    
    #Asking user to input their choice
    user_input =  input("Enter r, p, s \n")
    #Assigning a random choice to computer from the array
    computer_action = random.choice(possible_action)
    #Sending variables to printResults
    printResult(user_input, computer_action)
#Creating def to print the results
def printResult(user_input, computer_action):
    #Getting the scoring variables
    global playerCounter, computerCounter
    #Creating the result variable, retreiving the winner from the 'winner' logic.
    result = winner(user_input, computer_action)   

     
    if ( result== "Computer won"):  
        print("Computer won")
        computerCounter = computerCounter + 1
        print("Player: ", playerCounter, " Computer: ", computerCounter)
        print("You chose: ",user_input,", computer chose: ",computer_action)

        print(insult())  

    elif result == "You won":
        playerCounter = playerCounter + 1
        print("Player: ", playerCounter, " Computer: ", computerCounter)
        print("You chose: ",user_input,", computer chose: ",computer_action)
    
        print("Player Won")
        
    
    else:
        print("It's a tie!")

    tryAgain()

def tryAgain():
    play_again = input("\nDo you want to play again? Enter y or n ")

    if play_again == "y":
        action()
    else: 
        print("Bye Bye")