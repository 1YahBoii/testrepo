print("Welcome to the tip calculator!")
total_bill = float(input("What was the total bill?\n$"))
tip = int(input("How much tip would like to give? 10, 12, or 15? %"))
split = int(input("How many people to split the bill? "))
total_amount = total_bill + (total_bill*tip/100)
total_split = total_amount/split
print(f"Each person should pay: ${total_split:.2f}")
