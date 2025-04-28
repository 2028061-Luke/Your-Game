import random

holList = []

holplay = "y"
quack = 0
for x in range(0,100):
    holList.append(x)
while(holplay == "y"):
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