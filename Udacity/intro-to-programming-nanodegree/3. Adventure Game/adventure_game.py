import time
import random
firstAnswer = ["A", "a"]
secondAnswer = ["B", "b"]
notAllowedStatment = ("\nUse only A, B")
middleWay = ["left", "right", "forward", "backward"]
Score = 0
version = 0.2


def outro():
    global Score
    print("Your Score was "+str(Score))
    print("You need two or more to win")
    time.sleep(1)
    if Score >= 2:
        print("You WON")
    else:
        print("You Lost")
        print("Nice Play, Do you wanna play again?")
    print("Type yes to Confirm ,Or no to quit ")
    answer = input(":")
    if answer == "yes":
        print("okay")
        intro()
    elif answer == "no":
        print("Bye " + name)
        quit()
    else:
        print("I didn't understand that.\n")
        outro()


def village():
    print("You found yourself in a lovely village, game is over")
    time.sleep(1)
    outro()


def jail():
    print("You will be arrested for feeding the wild animals your body")
    time.sleep(1)
    print("game is over")
    outro()


def running():
    print("To your left, you see a bear.")
    time.sleep(1)
    print("To your right, there is more forest.")
    time.sleep(1)
    print("There is a rock wall directly in front of you.")
    time.sleep(1)
    print("Behind you is the forest exit.\n")
    time.sleep(1)
    print("What direction do you move?\nleft/right/forward/backward.\n")
    answer = input(":")
    if answer in middleWay:
        if answer == "left":
            print("The bear eats you. Farewell, " + name + ".")
            global Score
            outro()
        elif answer == "right":
            print("You head deeper into the forest.\n")
            time.sleep(1)
            print("You will start from the begining.\n")
            intro()
        elif answer == "forward":
            if random.randrange(1, 8) == 1:
                print("\nWelp, that was quick. ""\n\nYou died!")
                time.sleep(1)
                print("You cannot scale the wall.\n")
                outro()
            else:
                print("Nice climbing You win")
                print("And Now")
                global Score
                Score = Score + 1
                print("Your Score is "+str(Score))
                if random.randrange(1, 3) == 1:
                    jail()
                else:
                    village()
        elif answer == "backward":
            print("You leave the forest. Goodbye, ")
            Score = Score+1
            outro()
    else:
        print("Just reply forward, backaward, left Or Right")
        running()


def intro():
    global Score
    Score = 0
    print("You Can not see anything, SUDDENLY, You hear a ROOOAR")
    time.sleep(1)
    print("A wild bear is attacking you my friend,")
    print("You only have two choices Either")
    print("A. Grab a nearby rock and throw it at the Bear")
    print("B. Run away as fast as you can ")
    answer = input(">>> ")  # Here is your first choice.
    if answer in firstAnswer:
        if random.randrange(1, 8) == 1:
            print("\nWelp, that was quick. ""\n\nYou died!")
            outro()
        else:
            print("Nice shot mate...")
            time.sleep(1)
            Score = Score + 1
            print("Your Score is " + str(Score))
            print("The Bear is stunned,")
            time.sleep(1)
            print("but regains control.He begins running towards you again.")
            print("Now You are running")
            running()
    elif answer in secondAnswer:
        print("\nWelp, that was quick. ""\n\nYou died!")
        outro()
    else:
        print(notAllowedStatment)
        intro()


print("version:" + str(version))
name = input("What was your name again, I forgot\n")
print("Welcome back " + name + ". I missed you Bro. Lets start\n")
time.sleep(2)
print("You find yourself on the edge of a dark forest.")
time.sleep(1)
print("Can you find your way through?\n")
time.sleep(1)
intro()
