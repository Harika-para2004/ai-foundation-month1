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

"""3. Reverse a given string."""
def reverse_string(s):
    res = ''
    for i in range(len(s)-1, -1, -1):
        res += s[i]
    """
    Alternatively, using slicing: 1
    return s[::-1]
    2
    return ''.join(reversed(s))
    3
    reversed_str = ''
    for char in s :
        reversed_str = char + reversed_str 
    return reversed_str
    4
    char_list = list(s)
    char_list.reverse()
    return ''.join(char_list)
    option 1 is the most concise and efficient.
    why ? Slicing is optimized in Python and provides a clear and readable way to reverse a string in a single operation.
    how ? It directly accesses the string's characters in reverse order without the need for additional data structures or loops.

    """

input_str = input("Enter a string: ")
print(reverse_string(input_str))

"""4. Count vowels"""
def countVowels(s):
    vowels = 'aeiouAEIOU'

    count = 0
    for char in s:
        if char in vowels:
            count += 1
    return count
print(countVowels(input("Enter a string: ")))

"""5. Find the largest number in a list."""
def find_max_inlist (list):
    max = list[0]
    for num in list : 
        if num > max :
            max = num
    return max
numbers = [3, 5, 7, 2, 8, -1, 4]
print("Maximum number is: ",find_max_inlist(numbers))

"""6.Simple Calulator function"""
def calculator(a, b, operator):
    if operator == '+':
        res = a+b
    elif operator == '-':
        res = a-b
    elif operator == '*':
        res = a*b
    elif operator == '/':
        res = a/b
    else:
        return "Invalid operator"
        
    return res
print(calculator(10, 5, '+'))
print(calculator(10, 5, '-'))
print(calculator(10, 5, '*'))
print(calculator(10, 5, '/'))
