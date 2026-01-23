print("Welcome to the Tip Calculator!")
bill=float(input("How many is the total bill? $"))
tip=int(input("Wich percent you'll give? 10$, 12$ or 15$? "))
persons=int(input("How many people are with you? "))
per_person_tip=round(((bill+(bill*(tip/100)))/persons), 2)

print(f"Each one will contribute with {per_person_tip: .2f} dollars\n")