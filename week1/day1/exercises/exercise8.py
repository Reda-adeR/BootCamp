sandwich_orders = ["Tuna sandwich", "Pastrami sandwich", "Avocado sandwich", "Pastrami sandwich", "Egg sandwich", "Chicken sandwich", "Pastrami sandwich"]
for sandwich in sandwich_orders:
    if sandwich == "Pastrami sandwich":
        sandwich_orders.remove(sandwich)

finished_sandwiches = []
orders_copy = sandwich_orders.copy()
for sandwich in orders_copy:
    finished_sandwiches.append(sandwich)
    sandwich_orders.remove(sandwich)

for sandwich in finished_sandwiches:
    print("I made your "+sandwich)