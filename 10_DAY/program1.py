# Link : https://www.codewars.com/kata/54e6533c92449cc251001667/train/python

def unique_in_order(sequence):
    lst = []
    for i in range(len(sequence)):
        if i == 0:
            lst.append(sequence[0])
        else:
            if sequence[i-1] != sequence[i]:
                lst.append(sequence[i])
    return lst




def unique_in_order(sequence):
    result = []
    prev = None
    for item in sequence:
        if item != prev:
            result.append(item)
            prev = item
    return result



def unique_in_order(sequence):
    result = []  
    for item in sequence:
        if not result or result[-1] != item:
            result.append(item)
    return result



from itertools import groupby
def unique_in_order(sequence):
    return [key for key, _ in groupby(sequence)]