import inventory

bag = inventory.create_inventory()

inventory.add_item(bag, "coin", "Moeda")
inventory.add_item(bag, "coin", "Moeda")
inventory.add_item(bag, "flower", "Flor")

print(bag)
print("Moedas:", inventory.count_item(bag, "coin"))
print("Flores:", inventory.count_item(bag, "flower"))