import random
print("LETS PLAY A GUESSING GAME")
num = random.randint(1,9)
chances=0
print("GUESS ANY NUMBER BETWEEN 1 TO 9")
while chances<5:
    guess =int(input("ENTER YOUR GUESS"))
    if guess == num:
        print("Correct")
        print("YOU WIN! CONGRATULATIONS!")
        break
    elif guess < num:
        print("Your Guess is too Low")
        print("Guess a Number higher than this")
else:
         print("Your Guess is too hingh")
         print("Guess a Number lesser than this")
         chances+=1
if chances < 5 and guess!= num:
    print("YOU LOSE!!!")
    
