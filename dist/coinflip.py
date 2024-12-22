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

def coin_flip():
    coinSide = random.choice(['heads', 'tails'])
    print(f"The coin has landed on {coinSide}")

def main():
    while True:
        os.system('cls')
        print("Coin Flipper")
        flip = input("Flip Coin? (y/n): ")
        if flip.lower() == "y":
            coin_flip()
            input("Press enter to continue...")
        elif flip.lower() == "n":
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