#Tip Calculator Project
print("Welcome to the tip calculator.")
bill = float(input("What was the total bill? $"))
tip = int(input("What percentage tip would you like to give? 10, 12, or 15? "))
people = int(input("How many people to split the bill? "))
total_amt = bill + bill * (tip/100)
split = round(total_amt/people,2)
aft_split = "{:.2f}".format(split)
print(f"Each person should pay: ${aft_split}")