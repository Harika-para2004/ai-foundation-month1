def calculate_bmi(weight, height):
    """Calculate Body Mass Index (BMI) given weight in kg and height in meters."""
    bmi = weight / (height ** 2)
    return round(bmi ,2)


print(calculate_bmi(70, 1.75))
