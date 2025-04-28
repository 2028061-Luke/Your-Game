import random
print("disclaimer! You may have to answer some questions multiple times. This is normal, this is fine.")
butter = input("what game do your want to play, guess the number (type gtn), roshambo(type rps), or guess higher or lower (type hol) ")
while butter == "gtn":
    butter = input("what game do your want to play, guess the number (type gtn), roshambo(type rps), or guess higher or lower (type hol )")
    gtnList = []
    potato = 1
    gtnplay = "y"
    honk = 0
    for x in range(0,100):
        gtnList.append(x)
        random.shuffle(gtnList)
    while(gtnplay == "y"):
        while potato == 1:
            guess = input("guess a number 1-100 ")
       
            if int(guess) > 100 or int(guess) < 0:
                guess = input("invalid number, pick a number 1-100 ")
#        if  guess.isnumeric == False:
#            print("not a number")
#            guess = input("type in a NUMBER 1-100 ")
            if int(guess) > gtnList [1]:
                print("your guess was higher than the number")
                honk = honk + 1
            elif int(guess) < gtnList [1]:
                print("your guess was lower than the number")
                honk = honk + 1
            elif int(guess) == gtnList [1]:
                print("you got it right")
                honk = honk + 1
                print ("your number of guesses was " + str(honk))
                honk = 0
                gtnplay = input("do you want to play again y/n")
                random.shuffle(gtnList)

while butter == "rps":
    butter = input("what game do your want to play, guess the number (type gtn), roshambo(type rps), or guess higher or lower (type hol )")
    rpsList = ["rock", "paper", "scissors"]
    rpsplay = ("y")
    cluck = 0
    while rpsplay == ("y"):
        hand = input("choose one, rock, paper, or scissors ")
        random.shuffle(rpsList)

        while hand == ("scissors"):

            if rpsList[1] == "rock":
                print("lose")
                rpsplay = input("do you want to play again y/n ")
                hand = ("choose one, rock, paper, or scissors ")
            if rpsList[1] == "paper":
                print("win")
                cluck = cluck + 1
                rpsplay = input("do you want to play again y/n ")
                hand = ("choose one, rock, paper, or scissors ")
            if rpsList[1] == "scissors":
                print("tie")
                rpsplay = input("do you want to play again y/n ")
                hand = ("choose one, rock, paper, or scissors ")

        while hand == "rock":
            if rpsList[1] == "rock":
                print("tie")
                rpsplay = input("do you want to play again y/n ")
                hand = ("choose one, rock, paper, or scissors ")
            if rpsList[1] == "paper":
                print("lose")
                rpsplay = input("do you want to play again y/n ")
                hand = ("choose one, rock, paper, or scissors ")
            if rpsList[1] == "scissors":
                print("win")
                cluck = cluck + 1
                rpsplay = input("do you want to play again y/n ")
                hand = ("choose one, rock, paper, or scissors ")
        while hand == ("paper"):
        
            if rpsList[1] == "rock":
                print("win")
                cluck = cluck + 1
                rpsplay = input("do you want to play again y/n ")
                hand = ("choose one, rock, paper, or scissors ")
            if rpsList[1] == "paper":
                print("tie")
                rpsplay = input("do you want to play again y/n ")
                hand = ("choose one, rock, paper, or scissors ")
            if rpsList[1] == "scissors":
                print("lose")
                rpsplay = input("do you want to play again y/n ")
                hand = ("choose one, rock, paper, or scissors ")

    print(f"your score was {cluck}")
while butter == "hol":
    butter = input("what game do your want to play, guess the number (type gtn), roshambo(type rps), or guess higher or lower (type hol )")
    holList = []

    holplay = "y"
    quack = 0
    for x in range(0,100):
        holList.append(x)
    while holplay == "y":
        random.shuffle(holList)
        print("the number is " + str(holList[0]))
        n1 = (holList[0])
        a = input("higher or lower: ")
        while a != ("higher") and a != ("lower"):
            print("not an answer input a valid answer")
            a = input("higher or lower: ")

        n2 = (holList[1])
        if n1 > n2:
            if a == ("lower"):
                print("correct")
                quack = quack + 1
            else:
                print("incorrect")
                holplay = "n"
        else:
                if a == ("higher"):
                    print("correct")
                    quack = quack + 1
                else:
                    print("incorrect")
                    holplay = "n"
        print("the number was " + str(holList[1]))
        print("Your score was " + str(quack))
        holplay = input("Do you want to play again? y/n ")