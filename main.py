import menu

money = 0
cm_working = True
coffee_type = "test"


def stop_cm():
    global cm_working
    if coffee_type == "off":
        cm_working = False


def resources_report():
    if coffee_type == "report":
        print(f"Water: {menu.resources["water"]}")
        print(f"Milk: {menu.resources["milk"]}")
        print(f"Coffee: {menu.resources["coffee"]}")
        print(f"Money: ${money}")
        cm_choice()


def espresso():
    if coffee_type == "espresso":
        if menu.resources["water"] < menu.MENU["espresso"]["ingredients"]["water"]:
            print("Sorry, there is not enough water.")
            cm_choice()
            if menu.resources["coffee"] < menu.MENU["espresso"]["ingredients"]["coffee"]:
                print("Sorry, there is not enough coffee.")
                cm_choice()
        else:
            menu.resources["water"] -= menu.MENU["espresso"]["ingredients"]["water"]
            menu.resources["coffee"] -= menu.MENU["espresso"]["ingredients"]["coffee"]


def latte():
    if coffee_type == "latte":
        if menu.resources["water"] < menu.MENU["latte"]["ingredients"]["water"]:
            print("Sorry, there is not enough water.")
            cm_choice()
            if menu.resources["milk"] < menu.MENU["latte"]["ingredients"]["milk"]:
                print("Sorry, there is not enough milk.")
                cm_choice()
                if menu.resources["coffee"] < menu.MENU["latte"]["ingredients"]["coffee"]:
                    print("Sorry, there is not enough coffee.")
                    cm_choice()
        else:
            menu.resources["water"] -= menu.MENU["latte"]["ingredients"]["water"]
            menu.resources["milk"] -= menu.MENU["latte"]["ingredients"]["milk"]
            menu.resources["coffee"] -= menu.MENU["latte"]["ingredients"]["coffee"]


def cappuccino():
    if coffee_type == "cappuccino":
        if menu.resources["water"] < menu.MENU["cappuccino"]["ingredients"]["water"]:
            print("Sorry, there is not enough water.")
            cm_choice()
            if menu.resources["milk"] < menu.MENU["cappuccino"]["ingredients"]["milk"]:
                print("Sorry, there is not enough milk.")
                cm_choice()
                if menu.resources["coffee"] < menu.MENU["cappuccino"]["ingredients"]["coffee"]:
                    print("Sorry, there is not enough coffee.")
                    cm_choice()
        else:
            menu.resources["water"] -= menu.MENU["cappuccino"]["ingredients"]["water"]
            menu.resources["milk"] -= menu.MENU["latte"]["ingredients"]["milk"]
            menu.resources["coffee"] -= menu.MENU["cappuccino"]["ingredients"]["coffee"]


def pay():
    global money
    print("Please insert coins.")
    quarters = int(input("How many quarters?: "))
    dimes = int(input("How many dimes?: "))
    nickles = int(input("How many nickles?: "))
    pennies = int(input("How many pennies?: "))

    total_coins = quarters * 0.25 + dimes * 0.1 + nickles * 0.05 + pennies * 0.01

    if total_coins < menu.MENU[coffee_type]["cost"]:
        print("Sorry, that's not enough money. Money refunded.")
        if coffee_type == "espresso":
            menu.resources["water"] += menu.MENU["espresso"]["ingredients"]["water"]
            menu.resources["coffee"] += menu.MENU["espresso"]["ingredients"]["coffee"]
        else:
            menu.resources["water"] += menu.MENU["cappuccino"]["ingredients"]["water"]
            menu.resources["milk"] += menu.MENU["latte"]["ingredients"]["milk"]
            menu.resources["coffee"] += menu.MENU["cappuccino"]["ingredients"]["coffee"]
        cm_choice()
    elif total_coins > menu.MENU[coffee_type]["cost"]:
        total_coins -= menu.MENU[coffee_type]["cost"]
        money += menu.MENU[coffee_type]["cost"]
        print(f"Here is ${round(total_coins, 2)} in change")
        print(f"Here is your {coffee_type}☕. Enjoy!")
    else:
        money += total_coins
        print(f"Here is your {coffee_type}☕. Enjoy!")


def cm_choice():
    global coffee_type
    while cm_working:
        coffee_type = input("What would you like? (espresso ($1.5) / latte ($2.5) / cappuccino ($3)")

        stop_cm()
        if cm_working:
            resources_report()
            espresso()
            latte()
            cappuccino()
            pay()


cm_choice()

