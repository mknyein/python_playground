# List assignment
numbers = [1, "two", 3, 4, 5]

# Accessing elements by index
first_number = numbers[0]
last_number = numbers[-1]

# List slicing
subset = numbers[1:4]

# Modifying list elements
numbers[2] = 10

# List methods
numbers.append(6)
numbers.remove(4)

print(numbers)       # Output: [1, "two", 10, 5, 6]
print(first_number)  # Output: 1
print(last_number)   # Output: 5
print(subset)        # Output: ["two", 3, 4]
