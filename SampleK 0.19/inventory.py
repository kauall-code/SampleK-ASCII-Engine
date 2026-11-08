
# SampleK Engine
# Inventory Module


def create_inventory():
    return []


def add_item(inventory, item_id, name):
    item = {
        "id": item_id,
        "name": name
    }

    inventory.append(item)


def count_item(inventory, item_id):
    count = 0

    for item in inventory:
        if item["id"] == item_id:
            count += 1

    return count
