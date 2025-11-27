print("Welcome to my computer quiz")

playing = input("Do you want to play?")

if playing != "yes":
    quit()

print("Okay! Let's play :)")

answer = input("What does CPU stand for? ")
if answer == "central processing unit":
    print("Correct!")
else:
    print("Incorrect!")
    print("The correct answer is 'central processing unit'.")

answer = input("What does GPU stand for? ")
if answer == "graphics processing unit":
    print("Correct!")
else:
    print("Incorrect!")
    print("The correct answer is 'graphics processing unit'.")
answer = input("What does RAM stand for? ")
if answer == "random access memory":
    print("Correct!")
else:
    print("Incorrect!")
    print("The correct answer is 'random access memory'.")
answer = input("What does PSU stand for? ")
if answer == "power supply unit":
    print("Correct!")
else:
    print("Incorrect!")
    print("The correct answer is 'power supply unit'.")
answer = input("What does HDD stand for? ")
if answer == "hard disk drive":
    print("Correct!")
else:
    print("Incorrect!")
    print("The correct answer is 'hard disk drive'.")
print("Thanks for playing!")