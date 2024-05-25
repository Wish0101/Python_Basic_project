print("Welcome to Tip calculator ")
bill = float(input("What was the total bill : $ "))
tip = int(input("How much tip woulf you like to give ? \n 10 , 12 , 15? : "))
split = int(input("HOw many people will going to split the bill : "))
per_Person = (bill * (tip/100) + bill)/split
Total ="{:.2f}".format(per_Person)
print(f"Each person should pay : ${Total}")