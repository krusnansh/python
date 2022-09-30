print("Welcome my computer quiz")
play= input('Want to play ?  type yes to play  ').lower()
score = 0

if play != "yes":
    quit()
    
print("lets start the quiz")

ans = input("What does CPU stands for ?  ")

if ans == "cpu":
    print('correct answer')
    score += 1

else:
        print('wrong answer')

print("your final score is",score)