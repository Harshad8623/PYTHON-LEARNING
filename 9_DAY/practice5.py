# Link : https://www.codewars.com/kata/55908aad6620c066bc00002a/train/python
# Exes and Ohs

def xo(s):
    n = s.lower()
    n1 = n.count('x')
    n2 = n.count('o')
    if n1 == n2 :
        return True
    return False

def xo(s):
    s = s.lower()
    return s.count('x') == s.count('o')