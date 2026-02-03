students = [
    ("Aruzhan", 19),
    ("Dias", 22),
    ("Amina", 18),
    ("Nursultan", 21)
]
# Sort by age (index 1)
sorted_students = sorted(students, key=lambda x: x[1])
print(sorted_students)


numbers = [5, 2, 9, 1, 7]
# Sort descending using lambda
sorted_numbers = sorted(numbers, key=lambda x: x, reverse=True)
print(sorted_numbers)



numbers = [1, -2, 3, -4, 5, -6]
# Step 1: keep only positives
# Step 2: square them
# Step 3: sort descending
result = sorted(
    map(lambda x: x**2, filter(lambda x: x > 0, numbers)),
    reverse=True
)
print(result)
