# marks= {
#     "shrinath": 100,
#     "Abhijeet": 99,
#     "Rohan": 99
#
# }
# print (marks["Rohan"])

# dictionary method
marks= {
    "Shrinath": 100,
    "Abhijeet": 99,
    "Rohan": 99

}
# print (marks.items())
# print(marks.keys())
# print(marks.values())
# print(marks.update({"Shrinath":100,"Tanmay":56}))
# print(marks)
print(marks.get("tanmay"))

my_dict = {'a': 1, 'b': 2}
my_dict.clear()
print(my_dict)  # Output: {}

my_dict = {'a': 1, 'b': 2}
copy_dict = my_dict.copy()
print(copy_dict)  # Output: {'a': 1, 'b': 2}

my_dict = {'a': 1, 'b': 2}
print(my_dict.get('a'))  # Output: 1
print(my_dict.get('c', 'Not Found'))  # Output: Not Found

my_dict = {'a': 1, 'b': 2}
value = my_dict.pop('a')
print(value)  # Output: 1
print(my_dict)  # Output: {'b': 2}

my_dict = {'a': 1, 'b': 2}
print(my_dict.setdefault('a', 10))  # Output: 1
print(my_dict.setdefault('c', 3))   # Output: 3
print(my_dict)  # Output: {'a': 1, 'b': 2, 'c': 3}

my_dict = {'a': 1, 'b': 2}
my_dict.update({'b': 3, 'c': 4})
print(my_dict)  # Output: {'a': 1, 'b': 3, 'c': 4}

my_dict = {'a': 1, 'b': 2}
print(my_dict.values())  # Output: dict_values([1, 2])

