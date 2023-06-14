print("Welcome to Pick the safest Option Game!")
name = input("What is your name? ")
age = int(input("What is your age? "))

lives = 10

print("Hello", name, "you are", age, "years old")

if age >= 18:
    print("You are of age and can play")    
    if_user_wants_to_play = input("Do you want to play? ")
    if if_user_wants_to_play == "Yes":
        print("Lets play!!!")
else:
    print("You are underage!")
    exit()

    
print ("You are offered two fruits an Apple and an Orange. One of them is poisoned and one of them is safe to eat to progress to more paths. ")

fruit_choice = input("This is the first choice - Pick between the apple or the Orange. Pick Wisely (Apple/Orange) " )

if fruit_choice == "Apple":
    print("Great you have picked the Apple!. The Apple is not poisoned and you can move ahead to the next level.")
elif fruit_choice == "Orange":
    print("Oh no! You have selected the poisoned fruit as the Orange was poisoned. You have lost 5 lives!.")
    lives -= 5

Cake_Choice = input("Well done you are now in the second path. You now notice a stall with desserts. There is a strawberry tart and a lemon cheesecake. One dessert is poisoned. Pick wisely (Tart/Cheesecake) ")
if Cake_Choice == "Strawberry Tart":
    print ("Great! You have picked the cake which is not poisoned. You may progress to the next path. ")
elif Cake_Choice == "Lemon Cheesecake":
    print("Oh no you have selected the cake which was poisoned! You now lost an extra 5 lives! ")
    lives -= 5

if lives <=0:
    print("You have 0 lives left. Game over")
    exit()
else:
    print("You have survived. You win!")
