# Link : https://www.codewars.com/kata/54edbc7200b811e956000556/train/python
# Counting sheep...


def count_sheeps(sheep):
    count = 0
    for i in sheep:
        if i == True:
            count += 1
    return count


def count_sheeps(sheep):
    return sheep.count(True)

def count_sheeps(sheep):
    return sum(sheep)

