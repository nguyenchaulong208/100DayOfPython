
#Write a program tip calculator 
print('Welcome to the tip calculator.')
total_bill = float(input("What was the total bill? "))
percentage_tip = int(input("What percentage tip would you like to give? 10, 12, or 15? "))
people = int(input("How many people to split the bill? "))
payment = (total_bill * (1 + (percentage_tip/100)))/people
print(f"Each person should pay: {round(payment,2)}")