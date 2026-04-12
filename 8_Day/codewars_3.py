"Link : https://www.codewars.com/kata/55b42574ff091733d900002f/train/python"
# Friend or Foe?

def friend(x):
    y = []
    for i in range(0, len(x)):
        if len(x[i]) == 4:
            y.append(x[i])
    return y





def friend(x):
    result = []
    for name in x:
        if len(name) == 4:
            result.append(name)
    return result





def friend(x):
    return [name for name in x if len(name) == 4]