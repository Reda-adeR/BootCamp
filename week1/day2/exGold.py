birthdays = {
    "Alice" : "1999/07/15",
    "Bob" : "1998/05/20",
    "Charlie" : "2003/03/25",
    "David" : "1988/01/30",
    "Eve" : "2000/12/05",
}


for name, date in birthdays.items():
    print(f"{name}")
    print("*"*10)
print("Welcome to the birthday dictionary.")


person = input("Enter a name: ")
if person in birthdays:
    print(f"{person}'s birthday is {birthdays[person]}.")
else:
    print(f"sorry, we don't have {person}'s birthday.")