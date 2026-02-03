def student_info(name, age, grades):
    """
    Displays student information and
    returns the average grade.
    Parameters:
    name (str): student's name
    age (int): student's age
    grades (list): list of grades
    """
    print("Name:", name)
    print("Age:", age)
    average=sum(grades)/len(grades)
    return average
# Function call with different data types
avg_grade=student_info("Aruzhan", 19, [90, 85, 88])
print("Average grade:", avg_grade)
