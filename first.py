# topic?
#restaurant customer will order food

items = ["Noodles", "Tea", "Bread", "Sandwich"]
prices = [20,30,10,50]

print("Welcome to our Restaurant")
print("Order the items you want to eat")
print("Menu:")
for item, price in zip(items, prices):
    print(f"{item}: Rs {price}")

order_1 = input("enter item you want to order : ")
if order_1 in items:
    i = items.index(order_1)
    print(f"Your item {order_1} is ready. Price: Rs {prices[i]}")
else:
    print("item is not available")

order_2 = input("enter another item you want to order : ")
if order_2 in items:
    i = items.index(order_2)
    print(f"Your item {order_2} is ready. Price: Rs {prices[i]}")
else:
    print("item is not available")
