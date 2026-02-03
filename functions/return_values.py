def add_numbers(a,b):
    result=a+b   # calculate the sum
    return result    # return the value to the caller
# Calling the function
sum_result=add_numbers(3,5)
# The returned value can be stored or reused
print(sum_result)


def greet(name):
    """
    This function prints a greeting message.
    It does not return any value.
    """
    print("Hello,", name)
# Calling the function
greet("Inkar")



def find_max(numbers):
    """
    This function takes a list of numbers
    and returns the maximum value.
    """
    max_value = numbers[0]  # assume first element is the largest
    for num in numbers:
        if num > max_value:
            max_value = num
    return max_value
# Example list
nums = [3, 7, 2, 9, 5]
# Function call
print(find_max(nums))
