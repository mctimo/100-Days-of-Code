welcome_prompt = "Welcome to the tip calculator"
print(welcome_prompt)
total_bill = input("What was total bill?")
tip = input("What percentage tip would you like to give? 10, 12 or 15?")
people_count = input("How many people to split the bill?")
print(f"Each person should pay: ${round((float(total_bill) + (float(total_bill) * (int(tip)/100))) / int(people_count), 2)}")
