import datetime
age = input("Saisir votre âge : ")
yearToday = (datetime.datetime.now())
print(f"you will turn 100 in {yearToday.year + (100-int(age))}")