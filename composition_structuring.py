from typing import Dict, List

# Represents inventory of [Vegetable, count]
inventory: Dict[str, int] = {
    "Blueberry": 20,
    "Cucumber": 10,
    "Tomato": 5,
    "Strawberry": 8,
}

# Task: Buy 10 of all red vegetables


def do_my_task(inventory):
    # Without knowing the task, it is difficult to understand what the task was
    # E.g. was it buy 10 of Tomato and Strawberry or was it buy 10 for the last two?
    # I also need to read the code to figure it out

    # Pretty clear, but why do I need to loop over all vegetables?
    for vegetable in inventory:
        # I need to handcode this for each red vegetable
        if vegetable == "Tomato" or vegetable == "Strawberry":
            inventory[vegetable] += 10  # is this "buying" or just adding to inventory?


do_my_task(inventory)
assert inventory["Strawberry"] == 18
assert inventory["Tomato"] == 15

# ====================================================================================

# Better:

# Can change this at any time (e.g. using list comprehensions, without touching my buy_10 function)
def collect_matching_items(
    inventory: Dict[str, int], match: List[str]
) -> Dict[str, int]:
    result: Dict[str, int] = dict()
    for item in inventory:
        if item in match:
            result[item] = inventory[item]

    return result


# Works for all inventories, not only vegetables
def buy_items(inventory: Dict[str, int], count: int):
    for item in inventory:
        inventory[item] += count


# Way easier to read now, title states task (single responsibility)
def buy_10_of_all_red_vegetables_composition(inventory):
    red_veggys = ["Tomato", "Strawberry"]
    # Using composition makes this immediately clear what that does
    found_veggys = collect_matching_items(inventory, red_veggys)
    # Same here, no need to read "code", it's plain english
    buy_items(found_veggys, count=10)
    # Only tricky line here, but it's a python standard method (merges the found into inventory)
    inventory.update(found_veggys)


# Represents inventory of [Vegetable, count]
inventory: Dict[str, int] = {
    "Blueberry": 20,
    "Cucumber": 10,
    "Tomato": 5,
    "Strawberry": 8,
}

buy_10_of_all_red_vegetables_composition(inventory)

assert inventory["Strawberry"] == 18
assert inventory["Tomato"] == 15

# ====================================================================================

# generalization makes this also reusable for ANY type of inventory and ANY filter
def buy_x_of_matching_items(items, count, match):
    # Internally using composition makes it easy to read
    found_items = collect_matching_items(items, match)
    buy_items(found_items, count=10)
    items.update(found_items)


# specialization + composition, very easy to understand and might be all I need to know
def buy_10_of_all_red_vegetables_specialization(inventory):
    red_veggys = ["Tomato", "Strawberry"]
    buy_x_of_matching_items(items=inventory, count=10, match=red_veggys)


inventory: Dict[str, int] = {
    "Blueberry": 20,
    "Cucumber": 10,
    "Tomato": 5,
    "Strawberry": 8,
}

buy_10_of_all_red_vegetables_specialization(inventory)

assert inventory["Strawberry"] == 18
assert inventory["Tomato"] == 15
