# Traditional way
numbers = []
for i in range(5):
    numbers.append(i * 2)
print(numbers)  # [0, 2, 4, 6, 8]

# List comprehension
numbers = [i * 2 for i in range(5)]
print(numbers)  # [0, 2, 4, 6, 8]



# Even numbers only
evens = [i for i in range(10) if i % 2 == 0]
print(evens)  # [0, 2, 4, 6, 8]



# Traditional way
squares = {}
for i in range(5):
    squares[i] = i ** 2
print(squares)  # {0: 0, 1: 1, 2: 4, 3: 9, 4: 16}

# Dictionary comprehension
squares = {i: i ** 2 for i in range(5)}
print(squares)  # {0: 0, 1: 1, 2: 4, 3: 9, 4: 16}



# Only odd numbers
odd_squares = {i: i ** 2 for i in range(10) if i % 2 == 1}
print(odd_squares)  # {1: 1, 3: 9, 5: 25, 7: 49, 9: 81}



names = ['alice', 'bob', 'charlie']
# Name lengths
name_lengths = {name: len(name) for name in names}
print(name_lengths)  # {'alice': 5, 'bob': 3, 'charlie': 7}
