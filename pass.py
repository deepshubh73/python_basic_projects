check_pass = input("Enter your password: ")


check_pass_len = len(check_pass)

if check_pass_len < 8:
    print("Must be above 8 char")

elif check_pass == check_pass.lower():
    print("Password is weak cuz all are lowercase, use uppar")

elif check_pass != check_pass.title():
    print("First letter must be capital")

elif not any(ch.isdigit() for ch in check_pass):
    print("Must enter at least one digit in your password")


elif "@" not in check_pass:
    print("Must enter @ in your password")

else:
    print("Your password is strong")