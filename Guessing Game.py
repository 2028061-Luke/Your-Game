import random

gtnList = []
potato = 1
Play = "y"
honk = 0
for x in range(0,100):
    myList.append(x)
    random.shuffle(myList)
while(play == "y"):
    while potato == 1:
        guess = input("guess a number 1-100 ")
       
        if int(guess) > 100 or int(guess) < 0:
            guess = input("invalid number, pick a number 1-100 ")
#        if  guess.isnumeric == False:
#            print("not a number")
#            guess = input("type in a NUMBER 1-100 ")
        if int(guess) > myList [1]:
            print("your guess was higher than the number")
            honk = honk + 1
        elif int(guess) < myList [1]:
            print("your guess was lower than the number")
            honk = honk + 1
        elif int(guess) == myList [1]:
            print("you got it right")
            honk = honk + 1
            print ("your number of guesses was " + str(honk))
            honk = 0
            play = input("do you want to play again y/n")
            random.shuffle(myList)

     
