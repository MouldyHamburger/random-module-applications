import os
import sys
import time
import random
import pygame

def music_load():
    try:
        pygame.mixer.init()
        pygame.mixer.music.load('audio.mp3')
        pygame.mixer.music.play(-1)
    except pygame.error:
        print("Unable to load music...")

def exit_program():
    os.system('cls')
    print("Goodbye")
    print("Exiting program...")
    time.sleep(1)
    pygame.mixer.music.stop()
    sys.exit()

def play_again():
        while True:
            playAgain = input("Would you like to play again? (y/n): ").lower().strip()
            if playAgain == "y":
                break
            elif playAgain == "n":
                exit_program()
                break
            else:
                print("Please enter only (y/n)")
                time.sleep(1)
                os.system('cls')

def rps_choice():
    while True:
        os.system('cls')
        aiChoice = random.choice(['rock', 'paper', 'scissors'])
        playerChoice = input("Pick (rock/paper/scissors): ").lower().strip()
        print(f"You picked: {playerChoice}")
        if playerChoice == aiChoice:
            print(f"AI picked {aiChoice}")
            print("It's a tie!")
            play_again()
        elif playerChoice == "rock" and aiChoice == "scissors":
            print(f"AI picked {aiChoice}")
            print("You win!")
            play_again()
        elif playerChoice == "paper" and aiChoice == "rock":
            print(f"AI picked {aiChoice}")
            print("You win!")
            play_again()
        elif playerChoice == "scissors" and aiChoice == "paper":
            print(f"AI picked {aiChoice}")
            print("You win!")
            play_again()
        elif playerChoice == "scissors" and aiChoice == "rock":
            print(f"AI picked {aiChoice}")
            print("You lose!")
            play_again()
        elif playerChoice == "rock" and aiChoice == "paper":
            print(f"AI picked {aiChoice}")
            print("You lose!")
            play_again()
        elif playerChoice == "paper" and aiChoice == "scissors":
            print(f"AI picked {aiChoice}")
            print("You lose!")
            play_again()
        else:
            print(f"{playerChoice} is an invalid entry, try again...")
            time.sleep(1.5)

def main():
    while True:
        os.system('cls')
        print("Rock Paper Scissors")
        usrInput = input("Would you like to play? (y/n): ").lower().strip()
        if usrInput == "y":
            rps_choice()
        elif usrInput == "n":
            exit_program()
        else:
            print("Please enter only (y/n)...")
            time.sleep(1)

if __name__ == "__main__":
    music_load()
    try:
        main()
    except KeyboardInterrupt:
        print("^C")
        time.sleep(0.5)
        exit_program()