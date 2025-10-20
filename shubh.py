import random


name1 = input("Enter your name : ")
age1 = input("Enter your age : ")
name2 = input("Enter your love name : ")
age2 = input("Enter your love age : ")


len = (len(name1) + len(name2))*5
age_diff = abs(int(age1) - int(age2))
if age_diff <=2:
    len = len +20
elif age_diff <=5:
    len = len - 20

rand = random.randint(1,100)
final = rand + age_diff

print(f"{name1} and {name2} love score is {final}%")

