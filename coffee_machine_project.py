Menu = {
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 150
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 200,
    },
    "espresso": {
        "ingredients": {
            "water": 300,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 300,
    }
}
profit = 0
resources = {
    "water": 500,
    "milk": 200,
    "coffee": 100
}
def check_resources(order_ingredients):
    for item in order_ingredients:
        if order_ingredients[item] > resources[item]:
            print(f"Sorry, there is not enough {item}.")
            return False
    return True
def process_coins():
    total = 0
    coins_five = int(input("How many ₹5 coins?: "))
    coins_ten = int(input("How many ₹10 coins?: "))
    coins_twenty = int(input("How many ₹20 coins?: "))
    total = coins_five * 5 + coins_ten * 10 + coins_twenty * 20
    return total
def is_payment_successful(money_received, coffee_cost):
    if money_received >= coffee_cost:
        global profit
        profit += coffee_cost
        change = money_received - coffee_cost
        print(f"Here is ₹{change} in change.")
        return True
    else:
        print("Sorry, that's not enough money. Money refunded.")
        return False
def make_coffee(coffee_name, coffee_ingredients):
    for item in coffee_ingredients:
        resources[item] -= coffee_ingredients[item]
    print(f"Here is your {coffee_name} ☕... Enjoy!")
is_on = True
while is_on:
    choice = input("What would you like to have? (latte/espresso/cappuccino): ").lower()
    if choice == "off":
        is_on = False
    elif choice == "report":
        print(f"Water: {resources['water']}ml")
        print(f"Milk: {resources['milk']}ml")
        print(f"Coffee: {resources['coffee']}ml")
        print(f"Money: ₹{profit}")
    elif choice in Menu:
        coffee_type = Menu[choice]
        if check_resources(coffee_type['ingredients']):
            payment = process_coins()
            if is_payment_successful(payment, coffee_type['cost']):
                make_coffee(choice, coffee_type['ingredients'])
    else:
        print("Invalid choice. Please select latte, espresso, or cappuccino.")
