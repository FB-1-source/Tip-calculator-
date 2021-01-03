print("Welcome to the tip calculator.")

print("What was the total bill?")

total = float (input())

print("What percentage tip would you like to give? 10, 15 or 20")

tip = int (input())

print("How many people to split the bill?")

split = int (input())

tip1 = tip / 100 + 1

bill = round(total * tip1 / split,2)

print("Each person should pay: $" + str(bill))
