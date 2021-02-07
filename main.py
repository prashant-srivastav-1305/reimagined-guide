import product_list as pl

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

items_bought = {}
all_items = {}
supermarket_dict = pl.supermarket_dict
price = pl.price
amount = {}

for keys in supermarket_dict:
    all_items[supermarket_dict[keys]] = keys

while True:
    choice = int(input("WHICH ITEM DO YOU WANT TO BUY? "))

    if choice == 0:
        break

    qty = int(input("QUANTITY: "))

    if choice in list(all_items.keys()):
        items_bought[all_items[choice]] = price[all_items[choice]]
        amount[all_items[choice]] = qty * price[all_items[choice]]

    else:
        print("INVALID CHOICE")

print(items_bought)
print(amount)
# still in dev
# to be continued....
