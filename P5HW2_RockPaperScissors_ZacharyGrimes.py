# This project is about the game rock, paper, scissors
# Tuesday September 25, 2018
# CTI-110 P5HW2 - Rock, Paper, Scissors Game
# Zachary Grimes
#

import random

def generateRandomNumber():
    randomNumber = random.randint(1, 3)
    return randomNumber
def getComputerChoice( randomNumber ):
    if randomNumber == 1:
        computerChoice = "rock"
    elif randomNumber == 2:
        computerChoice = "paper"
    elif randomNumber == 3:
        computerChoice = "scissors"

    return computerChoice
def getUserChoice():
    userChoice = input("Please enter your choice: ")
    return userChoice
def determinewinner( computerChoice, userChoice ):
    rockmessage = "The rock smashes the scissors"
    scissorsmessage = "Scissors cuts paper"
    papermessage = "Paper wraps rock"
    if computerChoice =="rock" and userChoice =="scissors":
        winner = "Computer"
        message = rockmessage
        
    elif computerChoice =="scissors" and userChoice =="rock":
        winner = "You"
        message = rockmessage
    if computerChoice =="scissors" and userChoice =="paper":
        winner = "Computer"
        message = scissormessage
    elif computerChoice =="scissors" and userChoice =="paper":
        winner = "You"
        message = scissormessage
    if computerChoice =="paper" and userChoice =="rock":
        winner = "Computer"
        message = papermessage
    return winner, message
def startAgain():
    randomNumber = generateRandomNumber()
    computerChoice = getComputerChoice( randomNumber )
    userChoice = getUserChoice()
    print("The computer chose",computerChoice )
    winner, message = determineWinner( computerChoice, userChoice )

    if winner != "no winner":
        print( winner, "won(", message, ")")
    return winner
def main():
    randomNumber = generateRandomNumber()
    computerChoice = getComputerChoice( randomNumber )
    userChoice = getUserChoice()
    print("The computer chose",computerChoice )
    winner, message = determinewinner( computerChoice, userChoice )

    if winner != "no winner":
        print( winner, "won(", message, ")")
    while winner =="no winner":
        print("Yoy both chose the same thing")
        winner = startAgain()
main()


 
        
