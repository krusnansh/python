name = input("enter your name: ")
print("welcome",name,"to this adventure")

ans = input("you are on a dirt road, you can go either RIGHT or LEFT ").lower()

if ans =="left":
    ans = input("A river appeared , Want to SWIM or CROSS THE BRIDGE ").lower()

    if ans == "swim":
        print("you swam the river but eaten by a aligator,YOU LOSE ")
    else:
        print("bridge broke and you fall over the bridge, YOU LOSE ")

elif ans =="right":
    print("A forest appeared and its going to be night in a while , want to cross the forest or find shelter ")
    ans = input("FOREST or SHELTER ").upper()
    if ans == "FOREST":
        print("A tiger appeared and you got eaten by the tiger,YOU LOSE ")
    elif ans == "SHELTER":
        print("its morning time someone found you while you were asleep and helped to get out of the forest, YOU WON ")
    else:
        print("Invalid option , you lose")
else:
    print("Not a valid option, you LOSE")