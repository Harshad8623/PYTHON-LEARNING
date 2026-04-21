# Link : https://www.codewars.com/kata/545cedaa9943f7fe7b000048/train/python

def is_pangram(st):
    st1 = st.lower()
    srt = "abcdefghijklmnopqrstuvwxyz"
    
    for i in srt:
        if i not in st1:
            return False
    return True

def is_pangram(st):
    st = st.lower()
    return all(c in st for c in "abcdefghijklmnopqrstuvwxyz")

def is_pangram(st):
    st = st.lower()
    return set("abcdefghijklmnopqrstuvwxyz").issubset(set(st))



