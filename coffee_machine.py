menu = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 35,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 25,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 30,
    }
}
profit = 0
resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}
def is_resource_sufficient(order_ingredients):
    for item in order_ingredients:
        if order_ingredients[item] >= resources[item]:
            print(f"Sorry, Not Enough Ingredients for {item}")
            return False
    return True

def process_coins():
    print("Please insert Coins: ")
    total = int(input("How many 1rs notes: "))*1
    total += int(input("How many 2rs notes: ")) * 2
    total += int(input("How many 5rs notes: ")) * 5
    total += int(input("How many 10rs notes: ")) * 10
    total += int(input("How many 20rs notes: ")) * 20
    return total

def is_transaction_successful(money_recieved, drink_cost):
    if money_recieved >= drink_cost:
        change = round(money_recieved - drink_cost, 2)
        print(f"Here is your change: {change}")
        global profit
        profit += drink_cost
        return True
    else:
        print("Sorry, not enough money")
        return False

def make_coffee(drink_name, order_ingredients):
    for item in order_ingredients:
        resources[item] -= order_ingredients[item]
    print(f"Here is your drink: {drink_name}")
print("*** COFFEE MACHINE ***")
itr = True
while itr:
    ch = input("What would you like? (espresso/latte/cappuccino/report/exit): ").lower()
    if ch =='exit':
        itr = False
    elif ch =='report':
        print(f"Water: {resources['water']}ml")
        print(f"Milk: {resources['milk']}ml")
        print(f"Coffee: {resources['coffee']}g")
        print(f"Money: {profit}rs")
    else:
        drink = menu[ch]
        if is_resource_sufficient(drink["ingredients"]):
            payment = process_coins()
            if is_transaction_successful(payment, drink["cost"]):
                make_coffee(ch, drink["ingredients"])