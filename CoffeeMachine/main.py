MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 1000,
    "milk": 200,
    "coffee": 100,
}

profit = 0

to_continue = 1

while to_continue == 1:
    drink = input("What would you like? (espresso/latte/cappuccino): ").lower()

    if drink == "off":
        break
    elif drink == "report":
        print(f"{resources}\n{profit}")
        continue

    required_water = MENU[drink]['ingredients']['water']
    supply_water = resources["water"]
    if drink != "espresso":
        required_milk = MENU[drink]['ingredients']['milk']
        supply_milk = resources["milk"]
    else:
        required_milk = 0
        supply_milk = resources["milk"]
    required_coffee = MENU[drink]['ingredients']['coffee']
    supply_coffee = resources["coffee"]

    if required_water > supply_water:
        print("Not enough water")
        to_continue = 0
        break
    if required_milk > supply_milk:
        print("Not enough milk")
        to_continue = 0
        break
    if required_coffee > supply_coffee:
        print("Not enough coffee")
        to_continue = 0
        break

    resources["water"] = supply_water - required_water
    resources["milk"] = supply_milk - required_milk
    resources["coffee"] = supply_coffee - required_coffee

    print(f"The price for {drink} is {MENU[drink]['cost']}. Please insert coin: ")

    quarter = int(input("Enter the number of quarter: "))
    dime = int(input("Enter the number of dime: "))
    nickel = int(input("Enter the number of nickel: "))
    penny = int(input("Enter the number of penny: "))

    money = float((quarter * 25) + (dime * 10) + (nickel * 5) + penny)

    change = 0
    price = (MENU[drink]["cost"]) * 100

    if price > money:
        print("Not enough money")
    elif price < money:
        change = float((money - price) / 100)
        print(f"Here's {change} in change.\nHere is your {drink}. Enjoy!")
    elif price == money:
        print(f"Here's {change} in change.\nHere is your {drink}. Enjoy!")

    profit += (MENU[drink]["cost"])
    # for m_drink, m_info in MENU.items(): ###Works, but too costly
    #     if m_drink == drink:
    #         for ingredient, measure in m_info.items():
    #             if ingredient == "cost":
    #                 if money > (measure * 100):
    #                     print(f"The price for {m_drink} is {measure}")
    #                     change = float((money - (measure * 100)) / 100)
    #                     print(f"Here's {change} in change. Here is your {drink}. Enjoy!")
    #                     to_continue = 0
    #                 else:
    #                     print(f"The price for {m_drink} is {measure}, Not Enough Money")
    #                     to_continue = 0

# def enough_supply(MENU, chosen_drink): ### does not work
#     supply = 0
#     if MENU[chosen_drink]['ingredients']['water'] > resources["water"]:
#         supply = 1
#     elif MENU[chosen_drink]['ingredients']['water'] < resources["water"]:
#         print("Not enough water.")
#         supply = 0
#         return supply
#     if MENU[chosen_drink]['ingredients']['milk'] > resources["milk"]:
#         supply = 1
#     elif MENU[chosen_drink]['ingredients']['milk'] < resources["milk"]:
#         print("Not enough milk.")
#         supply = 0
#         return supply
#     if MENU[chosen_drink]['ingredients']['coffee'] > resources["coffee"]:
#         supply = 1
#     elif MENU[chosen_drink]['ingredients']['coffee'] < resources["coffee"]:
#         print("Not enough coffee")
#         supply = 0
#         return supply
#     return supply

# def enough_supply(MENU): ###works
#     supply = 0
#     for key, value in resources.items():
#         for m_drink, m_info in MENU.items():
#             if m_drink == drink:
#                 for ingredient, measure in m_info.items():
#                     if ingredient == "ingredients":
#                         for k, v in measure.items():
#                             if k == key:
#                                 if value < v:
#                                     print(f"Sorry there is not enough {key}")
#                                     supply = 0
#                                     return supply
#                                 else:
#                                     supply = 1
#     return supply
