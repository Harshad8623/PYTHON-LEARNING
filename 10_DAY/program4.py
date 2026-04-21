# link : https://www.codewars.com/kata/52597aa56021e91c93000cb0/train/python


def move_zeros(lst):
    non_zero = [x for x in lst if x != 0]
    zeros = [0] * (len(lst) - len(non_zero))
    return non_zero + zeros


def move_zeros(lst):
    return [x for x in lst if x != 0] + [0] * lst.count(0)


def move_zeros(lst):
    pos = 0  # position to place next non-zero
    
    for i in range(len(lst)):
        if lst[i] != 0:
            lst[pos] = lst[i]
            pos += 1
    
    # fill remaining with zeros
    for i in range(pos, len(lst)):
        lst[i] = 0
    
    return lst



def move_zeros(array):
    for i in array:
        if i == 0:
            array.remove(i) # Remove the element from the array
            array.append(i) # Append the element to the end
    return array