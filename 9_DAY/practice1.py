# Merging Dictionaries
dict1 = {'a': 1, 'b': 2}
dict2 = {'b': 3, 'c': 4}


print(dict1 | dict2)  # Output: {'a': 1, 'b': 3, 'c': 4}
print({**dict1, **dict2})  # Output: {'a': 1, 'b': 3, 'c': 4}



# Method 1: Using the update() method
merged_dict = dict1.copy()  # Create a copy of dict1 to avoid modifying it
merged_dict.update(dict2)  # Update the copy with dict2
print(merged_dict)  # Output: {'a': 1, 'b': 3, 'c': 4}



# Method 2: Using dictionary unpacking (Python 3.5+)
merged_dict = {**dict1, **dict2}  # Unpack both dictionaries into a new one
print(merged_dict)  # Output: {'a': 1, 'b': 3, 'c': 4}



# Method 3: Using a dictionary comprehension
merged_dict = {key: dict2.get(key, dict1.get(key)) for key in set(dict1) | set(dict2)}  # Combine keys and get values from dict2 or dict1
print(merged_dict)  # Output: {'a': 1, 'b': 3, 'c': 4}



# Method 4: Using the ChainMap from the collections module
from collections import ChainMap
merged_dict = dict(ChainMap(dict2, dict1))  # ChainMap gives precedence to dict2
print(merged_dict)  # Output: {'a': 1, 'b': 3, 'c': 4}



# Method 5: Using a loop to merge dictionaries
merged_dict = dict1.copy()  # Create a copy of dict1
for key, value in dict2.items():
    merged_dict[key] = value  # Update the value for each key in dict2
print(merged_dict)  # Output: {'a': 1, 'b': 3, 'c': 4}



# Method 6: Using the dict() constructor with unpacking
merged_dict = dict(dict1, **dict2)  # Unpack dict1 and dict
print(merged_dict)  # Output: {'a': 1, 'b': 3, 'c': 4}




# Method 7: Using the copy() method and a loop
merged_dict = dict1.copy()  # Create a copy of dict1
for key in dict2:
    merged_dict[key] = dict2[key]  # Update the value for each key in dict2
print(merged_dict)  # Output: {'a': 1, 'b': 3, 'c': 4}




print("All methods have successfully merged the dictionaries with dict2 taking precedence over dict1 for duplicate keys.")