print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S,M or L:\n")
pepperoni = input("Do you want pepperoni on your pizza? Y or N.\n")
extraCheese = input("Do you want extra cheese? Y or N.\n")

# TODO 1: work out how they need to pay based on their size choice
bill = 0
if size == 'S':
    bill += 15
elif size == 'M':
    bill += 20
elif size == 'L':
    bill += 25
else:
    print("Please Choose ont of the following: S, M or L")

# TODO 2: work out how much to add to their bill based on their pepperoni choice
if pepperoni == "Y":
    if size == 'S':
        bill += 2
    elif size == 'M':
        bill += 3
    elif size == 'L':
        bill += 4

# TODO 3: work out their final amount based on whether if they want extra cheese
if extraCheese == 'Y':
    bill += 1


print(f'Your final bill is: {bill}$')