weight = int(input("What's your weight(lbs): "))
height = int(input("What's your height(inches): "))

bmi = (weight / (height * height)) * 703

if bmi < 18.5:
	print("Your underweight")
elif 18.5 <= bmi < 25:
	print("Normal weight")
elif 25 <= bmi < 30:
	print("Overweight")
else:
	print("Obese")
