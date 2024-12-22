import os
import sys
import time
import random
import pygame

def music_load():
    try:
        pygame.mixer.init()
        pygame.mixer.music.load("audio.mp3")
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

def dice_roll():
    dice1 = random.randint(1, 6)
    print(f"Dice #1 has landed on {dice1}")
    dice2 = random.randint(1, 6)
    print(f"Dice #2 has landed on {dice2}")

def main():
    while True:
        os.system('cls')
        print("Double Dice roller")
        roll = input("Roll Dice? (y/n): ")
        if roll.lower() == "y":
            dice_roll()
            input("Press enter to continue...")
        elif roll.lower() == "n":
            exit_program()
            break
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