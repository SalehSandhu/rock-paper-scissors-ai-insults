#Creating def to determine winner, retrieving send variables.
def winner(user_input, computer_action):   
#creating if statment to compare the two inputs.
    if user_input == computer_action:
        #If both inputs are the same then it is a tie.
        return "It's a tie!"
    #If the user chose Rock and the computer chose
    #Paper then the computer won else the user wins
    elif user_input == "r":
        if computer_action == "p":
            return "Computer won"
        else:
            return "You won"
    #If the user chose Paper and the computer chose
    #Scissors then the computer won else the user wins
    elif user_input == "p":
        if computer_action == "s":
            return "Computer won"
        else:
            return "You won"
        #If the user chose Scissors and the computer chose
    #Rock then the computer won else the user wins
    elif user_input == "s":
        if computer_action == "r":
            return "Computer won"
        else:
            return "You won"