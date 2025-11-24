bill = int(input("What's the bill? "))
tip_percentage = int(input("What percentage would you like to tip? "))
percent = tip_percentage / 100
tip = bill * percent
print(f"The total bill (including tip) is: {bill + tip}")
