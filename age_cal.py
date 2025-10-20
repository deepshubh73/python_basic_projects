date_of_birth = int(input("Enter Your birth year : "))
current_year = int(input("enter current year : "))
if date_of_birth < current_year :
    DOB = current_year - date_of_birth
    print(DOB)
else:
    print("enter valid year")


