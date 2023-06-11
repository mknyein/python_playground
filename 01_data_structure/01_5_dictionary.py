# Dictionary assignment
student = {
    "name": "John Doe",
    "age": 20,
    "grade": "A"
}

# Accessing values by keys
name = student["name"]
age = student.get("age")

# Modifying dictionary values
student["grade"] = "B"

# Dictionary methods
keys = student.keys()
values = student.values()
items = student.items()

print(student)  # Output: {'name': 'John Doe', 'age': 20, 'grade': 'B'}
print(name)     # Output: John Doe
print(age)      # Output: 20
print(keys)     # Output: dict_keys(['name', 'age', 'grade'])
print(values)   # Output: dict_values(['John Doe', 20, 'B'])
print(items)    # Output: dict_items([('name', 'John Doe'), ('age', 20), ('grade', 'B')])
