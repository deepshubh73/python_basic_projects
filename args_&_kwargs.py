

def add_no(*args):
    print(args)
    total = sum(args)
    print(total)

add_no(1,2,3,4,5,6,7,8,9,)


def add_no(*args):
    print(args)
    return sum(args)

print(add_no(1,2,3,4,5,6,7,8,9))



# Print वाला - सिर्फ दिखाता है
def calculate_print(a, b):
    print(a + b)       # 15 दिखेगा

x = calculate_print(10, 5)  # 15 दिखेगा
print(x)                    # None (क्योंकि कुछ return नहीं हुआ)

# Return वाला - value देता है
def calculate_return(a, b):
    return a + b       # 15 return करता है

y = calculate_return(10, 5)  # कुछ नहीं दिखेगा
print(y)                     # 15 दिखेगा
print(y * 2)                 # 30 दिखेगा (क्योंकि y में value है)
