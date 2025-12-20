# def calculate_bmi(weight, height):
#     """1. Calculate Body Mass Index (BMI) given weight in kg and height in meters."""
#     bmi = weight / (height ** 2)
    
#     bmi = round(bmi, 2)

#     if bmi < 18.5:
#         status = "Underweight"
#     elif bmi < 24.9:
#         status = "Normal weight"
#     else:
#         status = "Overweight"
    
#     return bmi, status
# # Example usage
# weight = float(input("Enter weight in kg: "))
# height = float(input("Enter height in meters: "))

# print(calculate_bmi( weight, height))


""" 2.Check if a number is prime."""
def is_prime(num):
    if num <= 1 :
        return False
    for i in range (2, int(num** 0.5) +1):
        if num % i == 0:
            return False
    return True

print(is_prime(int(input("Enter a number: "))))