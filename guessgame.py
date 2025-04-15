import random
number = random.randint(1,100)
chance = 0

while chance < 3:
    try:
        user_input = int(input("What's your number between 1 and 100? "))
        chance += 1

        if user_input == number:
            print("Congratulations, Welldone you guessed right.") 
            
            break
        elif user_input > number:
            print("Number too high")
        else:
            print("Number too low")
            
    except ValueError:
        print("Enter Valid Number!!")

if chance == 3 and user_input != number :
    print(f"Sorry you have run out of attempt, The correct number was {number}. Thank You!")
            

