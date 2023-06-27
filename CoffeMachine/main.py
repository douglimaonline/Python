from data import MENU, resources, price

money = 0  # $
is_machine_on = True
coffee_choice = ''


def report():
    print(f'Water = {resources["water"]}ml\nMilk = {resources["milk"]}ml\nCoffee ='
          f' {resources["coffee"]}g\nMoney = ${money}')


def cost():
    coffee_cost = MENU[coffee_choice]["cost"]
    print(f'Cost: ${coffee_cost}')
    print(f'Please inset coins.')
    total_payment = 0
    for coin in price["coins"]:
        get_coin = input(f'How many {coin}? ')
        if get_coin.isdigit():
            total_payment += round((int(get_coin) * price["coins"][coin]), 2)
    if total_payment >= coffee_cost:
        global money
        money += coffee_cost
        for ingredient in MENU[coffee_choice]["ingredients"]:
            resources[ingredient] -= MENU[coffee_choice]["ingredients"][ingredient]

        if (total_payment - coffee_cost) != 0.00:
            print(f"Here is ${round(total_payment - coffee_cost, 2)} in change.")
        print("Enjoy.☕")
    else:
        print("Sorry, insufficient founds.")


def menu():
    global coffee_choice
    global is_machine_on
    coffee_choice = input(' What would you like? (espresso/latte/cappuccino): ').lower()
    if coffee_choice == 'espresso' or coffee_choice == 'latte' or coffee_choice == 'cappuccino':
        return coffee_choice
    elif coffee_choice == 'report':
        report()
        menu()
    elif coffee_choice == 'off':
        is_machine_on = False
        print('Machine turn off')
    else:
        print('Invalid choice')
        menu()


def check_resources():
    for ingredient in MENU[coffee_choice]["ingredients"]:
        if MENU[coffee_choice]["ingredients"][ingredient] > resources[ingredient]:
            print(f'Sorry, there is no {ingredient} enough.')
            machine_function()
    return coffee_choice


# Machine Start
def machine_function():
    while is_machine_on and coffee_choice != 'off':
        if coffee_choice != 'off':
            menu()
            check_resources()
            cost()
        else:
            break


machine_function()
