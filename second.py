# Restaurant ordering system
menu = {"Noodles": 20, "Tea": 30, "Bread": 10, "Sandwich": 50}

print("Welcome to our Restaurant!")
name = input("Enter your name: ")
print(f"Hello {name}!")

input("Press Enter to show menu...")
print("\n--- MENU ---")
for item, price in menu.items():
    print(f"{item}: Rs {price}")

total_price = 0
order_list = []

while True:
    order = input("\nWhat would you like to order? ").strip().title()
    
    if order in menu:
        order_list.append(order)
        total_price += menu[order]
        print(f"Order added: {order} - Rs {menu[order]}")
        print(f"Total so far: Rs {total_price}")
        
        while True:
            more = input("Do you want to add more items? (yes/no): ").lower().strip()
            if more in ["yes", "y", "no", "n"]:
                break
            print("Please answer yes or no only!")
        
        if more in ["no", "n"]:
            break
    else:
        print("Item not available! Please choose from menu.")

print(f"\n--- FINAL BILL ---")
print(f"Customer: {name}")
print("Orders:")
for item in order_list:
    print(f"- {item}: Rs {menu[item]}")
print(f"\nTotal Amount: Rs {total_price}")
print("Please pay the amount. Thank you!")
