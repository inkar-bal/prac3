scores = [45, 78, 60, 32, 90, 55, 61]
passed = list(filter(lambda x: x >= 60, scores))
print(passed)



numbers = [1, 2, 3, 4, 5, 6, 7, 8]
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
print(even_numbers)


numbers = [1, 2, 3, 4, 5, 6]
# Step 1: keep only even numbers, Step 2: square them
result = list(map(lambda x: x**2, filter(lambda x: x % 2 == 0, numbers)))
print(result)

