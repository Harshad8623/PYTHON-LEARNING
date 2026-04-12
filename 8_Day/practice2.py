# combining two dictionaries
dict1 = {'a': 1, 'b': 2}
dict2 = {'c': 3, 'd': 4}
print(dict1 | dict2)  # Output: {'a': 1, 'b': 2, 'c': 3, 'd': 4}


# Merging dictionaries using the update() method
dict1.update(dict2)
print(dict1)  # Output: {'a': 1, 'b': 2, 'c': 3, 'd': 4}


# Using the unpacking operator to merge dictionaries
dict3 = {**dict1, **dict2}
print(dict3)  # Output: {'a': 1, 'b': 2, 'c': 3, 'd': 4}