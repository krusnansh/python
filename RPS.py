import random
user=0
comp=0
option=["rock","paper","scissors"]
while True:
    user_input = input("type rock/paper/scissors or Q to quit  ").lower()
    if user_input =="q" :
        quit()
        # below is the way to check multiple items in one if statement
    if user_input not in option:
        print("entered value is invaled")
        print("plz try again")
        continue
        
    r_num = random.randint(0,2)
    comp_p=option[r_num]
    print('computer picked',comp_p + ".")
    
    if user_input == "rock" and comp_p == "scissors":
        print("you win")
        user+=1
        
    elif user_input == "scissors" and comp_p == "paper":
        print("you win!")
        user+=1
        
    elif user_input == "paper" and comp_p == "rock":
        print("you win!")
        user+=1
    else:
        print('you lost')
        comp+=1 


    print('you win ', user,'computer win',comp)
    print("Goodbye!")

 