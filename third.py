import random
from datetime import datetime
from collections import Counter

# Restaurant System with All Features
menu = {
    "🍜 Noodles": 20, "🍵 Tea": 30, "🍞 Bread": 10, 
    "🥪 Sandwich": 50, "🍕 Pizza": 80, "🍔 Burger": 60
}

categories = {
    "Food": ["🍜 Noodles", "🍞 Bread", "🥪 Sandwich", "🍕 Pizza", "🍔 Burger"],
    "Drinks": ["🍵 Tea"]
}

print("🏪 Welcome to our Restaurant!")
name = input("Enter your name: ")
table = input("Enter table number: ")
print(f"Hello {name}! Table: {table}")

# Lucky customer check
if random.randint(1, 10) == 7:
    print("🎉 CONGRATULATIONS! You're our lucky customer - 20% discount!")
    lucky_discount = 0.20
else:
    lucky_discount = 0

input("Press Enter to show menu...")

# Display menu by categories
print("\n🍽️ --- MENU ---")
for category, items in categories.items():
    print(f"\n📋 {category}:")
    for item in items:
        print(f"   {item}: Rs {menu[item]}")

# Order system
order_dict = {}
total_price = 0

while True:
    print("\n🛒 Options: order [quantity] [item] | remove [item] | show | done")
    action = input("What would you like to do? ").strip().lower()
    
    if action == "done":
        break
    elif action == "show":
        if order_dict:
            print("\n📝 Current Orders:")
            for item, qty in order_dict.items():
                print(f"   {item} x{qty} = Rs {menu[item] * qty}")
        else:
            print("No orders yet!")
        continue
    elif action.startswith("remove"):
        parts = action.split(" ", 1)
        if len(parts) > 1:
            item_to_remove = parts[1].title()
            # Find matching item with emoji
            found = None
            for menu_item in menu:
                if item_to_remove.lower() in menu_item.lower():
                    found = menu_item
                    break
            
            if found and found in order_dict:
                del order_dict[found]
                print(f"✅ Removed {found}")
            else:
                print("❌ Item not found in your orders!")
        continue
    
    # Parse order command
    parts = action.split()
    if len(parts) >= 2 and parts[0].isdigit():
        quantity = int(parts[0])
        item_name = " ".join(parts[1:]).title()
    elif len(parts) >= 1:
        quantity = 1
        item_name = " ".join(parts).title()
    else:
        print("❌ Invalid format! Use: [quantity] [item name]")
        continue
    
    # Find matching menu item
    found_item = None
    for menu_item in menu:
        if item_name.lower() in menu_item.lower():
            found_item = menu_item
            break
    
    if found_item:
        if found_item in order_dict:
            order_dict[found_item] += quantity
        else:
            order_dict[found_item] = quantity
        
        item_total = menu[found_item] * quantity
        print(f"✅ Added: {found_item} x{quantity} = Rs {item_total}")
        
        # Calculate running total
        total_price = sum(menu[item] * qty for item, qty in order_dict.items())
        print(f"💰 Current total: Rs {total_price}")
        
        # Ask for more
        while True:
            more = input("Add more items? (yes/no): ").lower().strip()
            if more in ["yes", "y", "no", "n"]:
                break
            print("Please answer yes or no only!")
        
        if more in ["no", "n"]:
            break
    else:
        print("❌ Item not available! Check menu.")

if not order_dict:
    print("No orders placed. Thank you for visiting!")
    exit()

# Calculate final bill
subtotal = sum(menu[item] * qty for item, qty in order_dict.items())
discount_amount = subtotal * lucky_discount
after_discount = subtotal - discount_amount

# Volume discount
if after_discount >= 100:
    volume_discount = after_discount * 0.10
    print(f"🎁 Volume discount (10% on orders ₹100+): Rs {volume_discount:.2f}")
else:
    volume_discount = 0

after_all_discounts = after_discount - volume_discount
gst = after_all_discounts * 0.18
final_total = after_all_discounts + gst

# Payment method
print("\n💳 Payment Methods: 1-Cash | 2-Card | 3-UPI")
payment = input("Choose payment method (1/2/3): ")
payment_methods = {"1": "Cash", "2": "Card", "3": "UPI"}
payment_method = payment_methods.get(payment, "Cash")

# Generate receipt
receipt_id = random.randint(1000, 9999)
order_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

# Final receipt
print(f"\n🧾 ===== RECEIPT #{receipt_id} =====")
print(f"🏪 Restaurant Name")
print(f"📅 Date: {order_time}")
print(f"👤 Customer: {name}")
print(f"🪑 Table: {table}")
print(f"💳 Payment: {payment_method}")
print("-" * 35)

print("📋 Orders:")
for item, qty in order_dict.items():
    item_total = menu[item] * qty
    print(f"   {item}")
    print(f"   {qty} x Rs {menu[item]} = Rs {item_total}")

print("-" * 35)
print(f"Subtotal:        Rs {subtotal:.2f}")

if lucky_discount > 0:
    print(f"Lucky Discount:  -Rs {discount_amount:.2f}")

if volume_discount > 0:
    print(f"Volume Discount: -Rs {volume_discount:.2f}")

print(f"After Discounts: Rs {after_all_discounts:.2f}")
print(f"GST (18%):       Rs {gst:.2f}")
print(f"FINAL TOTAL:     Rs {final_total:.2f}")
print("=" * 35)

# Save to file
with open("daily_sales.txt", "a") as f:
    f.write(f"{order_time},{name},{table},{final_total:.2f},{payment_method}\n")

# Rating system
rating = input("\n⭐ Rate your experience (1-5): ")
if rating.isdigit() and 1 <= int(rating) <= 5:
    print(f"Thank you for {rating}⭐ rating!")
else:
    print("Thank you for your feedback!")

print(f"\n🎉 Thank you {name}! Please pay Rs {final_total:.2f}")
print("Have a great day! 😊")

# Show most popular item
try:
    with open("daily_sales.txt", "r") as f:
        print(f"\n📊 Today's most popular items updated!")
except:
    pass
