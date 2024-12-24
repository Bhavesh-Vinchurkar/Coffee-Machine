def total_value():
    print("Please insert the coins")
    quarters=float(input("How many quarters : "))
    dimes=float(input("How many dimes : "))
    nickels=float(input("How many nickels : "))
    pennies=float(input("How many pennies : "))
    return 0.25*quarters+0.10*dimes+0.05*nickels+0.01*pennies


def resource_checker(coffee_type):
    if available_resources['Water']<res_for_each[coffee_type]['Water']:
        print("Sorry there isn't enough water")
        return
    elif available_resources['Milk']<res_for_each[coffee_type]['Milk']:
        print("Sorry there isn't enough milk")
        return
    elif available_resources['Coffee']<res_for_each[coffee_type]['Coffee']:
        print("Sorry there isn't enough coffee")
        return
    else:
        return total_value()


def resource_updater(coffee_type):
    available_resources['Coffee']-=res_for_each[coffee_type]['Coffee']
    available_resources['Water']-=res_for_each[coffee_type]['Water']
    available_resources['Milk']-=res_for_each[coffee_type]['Milk']
    available_resources['Money']+=res_for_each[coffee_type]['Money']


def processing(coffee_type,coffee_value):
    if coffee_value>=res_for_each[coffee_type]['Money']:
        if coffee_value>res_for_each[coffee_type]['Money']:
            change=coffee_value-res_for_each[coffee_type]['Money']
            print(f"Here's your ${round(change,2)} dollars in change")
            resource_updater(coffee_type)
        else:
            resource_updater(coffee_type)
        print(f"Here's your {coffee_type}. Enjoy!")
    else:
        print("Sorry that's not enough money. Money refunded." )


available_resources={'Water':1000,'Milk':1000,'Coffee':500,'Money':100}
res_for_each={
    'espresso':{'Water':50,'Milk':0,'Coffee':18,'Money':3.21},
    'latte':{'Water':200,'Milk':150,'Coffee':24,'Money':3.76},
    'cappuccino':{'Water':250,'Milk':100,'Coffee':24,'Money':3.70}
}
on_or_off=True
while on_or_off:
    coffee_order=input("What would you like? (espresso/latte/cappuccino) : ").lower()

    if coffee_order=='espresso':
        complete_resources=resource_checker('espresso')
        if type(complete_resources)==float:
            processing(coffee_order,complete_resources)
            print("\n*10")
    elif coffee_order=='latte':
        complete_resources=resource_checker('latte')
        if type(complete_resources)==float:
            processing(coffee_order,complete_resources)
            print("\n"*5)
    elif coffee_order=='cappuccino':
        complete_resources=resource_checker('cappuccino')
        if type(complete_resources)==float:
            processing(coffee_order,complete_resources)
            print("\n"*5)
    elif coffee_order=='report':
        for key in available_resources:
            print(f"{key} : {available_resources[key]}")
        print("\n"*5)
    elif coffee_order=='off':
        on_or_off=False
    else:
        print("The following product is unavailable")
        print("\n"*5)