#1
def get_even_numbers(numbers):
    even_numbers = []
    for num in numbers:
        if num % 2 ==0:
            even_numbers.append(num)
    return even_numbers

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(get_even_numbers(numbers))

#2
def get_unique_values(numbers):
    unique_values = set()
    for num in numbers:
        unique_values.add(num)
    return list(unique_values)
numbers = [1, 2, 2, 3, 4, 4, 5]
print(get_unique_values(numbers))

#3 Count frequency (DICT)
def count_frequency(items):
    count_frequency = {}
    freq = 0
    for item in items:
        count_frequency[item] = count_frequency.get(item,0) + 1
    return count_frequency

items = ['apple', 'banana', 'apple', 'orange', 'banana', 'apple' ]
print(count_frequency(items))

#4 Find max WITHOUT using max()
def find_largest_number(numbers):
    largest = numbers[0]
    for num in numbers :
         if num > largest:
             largest = num
    return largest

numbers = [3, 5, 7, 2, 8, -1, 4]
print("The largest number is:", find_largest_number(numbers))

#5 Find second largest
def find_second_largest(numbers):
    first_largest = numbers[0]
    second_largest = numbers[0]
    for num in numbers:
        if num > first_largest:
            first_largest = num
        elif num > second_largest and num != first_largest:
            second_largest = num
    
    return second_largest
numbers = [3, 5, 6, 2, 8, -1, 4, 7]
print("The second largest number is:", find_second_largest(numbers))

#6 Find intersection of 2 lists
def find_intersection(list1,list2):
    set1 = set(list1)
    set2 = set(list2)
    intersection = set1.intersection(set2)
    return list(intersection)
list1 = [1, 2, 3, 4, 5]
list2 = [4, 5, 6, 7, 8]
print("Intersection using sets:", find_intersection(list1, list2))

#7 Remove duplicates from a list
def remove_duplicates(list):
    list2  = []
    for item in list:
        if item not in list2:
            list2.append(item)
    return list2
input_list = [1, 2, 2, 6, 4, 4, 5, 3, 3]
print("Unique values:", remove_duplicates(input_list))

#8 Invert dictionary
def invert_dict(dict):
    inverted_dict = {}
    for key in dict:
        inverted_dict[dict[key]] = key
    return inverted_dict
input_dict = {'a': 1, 'b': 2, 'c': 3}
print("Inverted dictionary:", invert_dict(input_dict))

#9  group by first letter
def group_by_first_letter(words):
    res = {}
    for word in words:
        first_letter = word[0]
        if first_letter not in res:
            res[first_letter] = []
        res[first_letter].append(word)
    return res
input_words = ['apple', 'banana', 'avocado', 'blueberry', 'cherry']
print("Grouped by first letter:", group_by_first_letter(input_words))

#10 Word lenght mapping
def word_length_mapping(words):
    res = {}
    for word in words:
        res[word] = len(word)
    return res
input_words = ['apple', 'banana', 'cherry']
print("Word length mapping:", word_length_mapping(input_words))
   



    





