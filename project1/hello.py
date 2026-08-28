name = input("What is your name? ")
print(f"Hello {name}!")

cheeseChecker = input("DO NOT TYPE AND ENTER \"Cheese\". It will do bad things. ")
if cheeseChecker == "Cheese":
    while True:
        print("Cheese")
else:
    print("Good Job :D")
