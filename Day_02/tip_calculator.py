print("Welcome to the Tip Calculator!")
bill = int(input("What was the bill? $"))
tip = int(input("How much tip would you like to give? 10 20 or 15? "))
total_people = int(input("How many people to split the bill? "))

total_bill = (bill + (bill * tip /100)) / total_people

print(f"Each person should pay: ${round(total_bill,2)}")