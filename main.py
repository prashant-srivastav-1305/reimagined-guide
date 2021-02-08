"""The main program file"""

# importing the local documents for ref
import product_list as pl
import employee_info as info

# importing pandas for dataframes
import pandas as pd
# importing winsound to generate warnings
import winsound
# importing date time (self-explanatory)
import datetime as dt
# importing tabulate module for a better way to represent the data frame
from tabulate import tabulate


"""The program asks the user to enter a username and a password. If both of them are correct only then access is allowed.
The username and password are extracted from the employee_info.py file"""

a = input("ENTER THE USERNAME: ")
if a in list(info.employee_dict.keys()):
    b = input("ENTER THE PASSWORD: ")
    if b == info.employee_dict[a]:
        # printing the supermarket name 
        info.supermarket_name(name="ABC SUPERMARKET")
        # printing the items category wise
        pl.Fruits.print_category()
        pl.Fruits.print_items()
        pl.Vegetables.print_category()
        pl.Vegetables.print_items()
        pl.Dairy.print_category()
        pl.Dairy.print_items()
        pl.Groceries.print_category()
        pl.Groceries.print_items()
        pl.PersonalCare.print_category()
        pl.PersonalCare.print_items()
        pl.HomeNeeds.print_category()
        pl.HomeNeeds.print_items()
        pl.Stationery.print_category()
        pl.Stationery.print_items()

        # empty dictionary to store items bought
        items_bought = {}
        all_items = {}
        supermarket_dict = pl.supermarket_dict
        price = pl.price
        amount = {}
        quantity = {}

        for keys in supermarket_dict:
            all_items[supermarket_dict[keys]] = keys

        # endless loop to ask the user which item to add into the bill
        while True:
            choice = int(input("WHICH ITEM DO YOU WANT TO BUY? "))

            if choice == 0:
                break

            qty = int(input("QUANTITY: "))

            if choice in list(all_items.keys()):
                items_bought[all_items[choice]] = price[all_items[choice]]
                amount[all_items[choice]] = qty * price[all_items[choice]]
                quantity[all_items[choice]] = qty

            else:
                print("INVALID CHOICE")
        
        # empty dictionary which will later store the taxes on items
        taxes = {}
        for keys in amount:
            tax = 0.18 * amount[keys]
            taxes[keys] = tax
    
        # creating the DataFrame of the table
        table = {
            "ITEM NAME": list(items_bought.keys()),
            "PRICE": list(items_bought.values()),
            "QUANTITY": list(quantity.values()),
            "TOTAL": list(amount.values()),
            "TAX": list(taxes.values())
        }

        df = pd.DataFrame(data=table)
        print()
        print(f"EMPLOYEE NAME: {info.employee_names[a]}")
        print(f"EMPLOYEE ID: {info.employee_ids[a]}")
        print(f"DATE AND TIME: {dt.datetime.now().strftime('%m/%d/%Y %H:%M:%S')}")
        print()
        print(tabulate(df, headers='keys', tablefmt='psql'))
        print()
        payment = sum(list(amount.values())) + 0.18*sum(list(amount.values()))
        print(f"TOTAL AMOUNT: {payment} INCL. OF ALL TAXES")
        print()
        print("THANKS FOR SHOPPING WITH US!!")
        input("VISIT AGAIN :)")
        input()

    # warning generated if password is incorrect
    else:
        winsound.MessageBeep(type=1)
        print("ACCESS DENIED.")
        input()
    
# warning generated if username is incorrect             
else:
    winsound.MessageBeep(type=1)
    print("WRONG USERNAME.")
    input()
