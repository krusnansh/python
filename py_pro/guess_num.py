import random

uplimit=input("type a upper limit of number : ")

if uplimit.isdigit():
    uplimit=int(uplimit)

    if uplimit <= 0 :
        print('enter a numer more than 0 ')
        quit()
        
else:
    print("enter a digit next time")
    quit()
track = 0
r=random.randint(0,uplimit)

while True :
    track += 1
    guess = input("enter you guess ")

    if guess.isdigit():
        guess=int(guess)

    else:
        print("enter a digit next time")
        continue

    if guess == r:
        print('got it ! ')
        print('in',track,"guess")
        break
   
    elif guess < r:
            print('guess a higher number next time')
    else:
            print('guess a lower number next time') 