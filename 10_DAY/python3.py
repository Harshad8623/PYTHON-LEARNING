# Link : https://www.codewars.com/kata/55c45be3b2079eccff00010f/train/python

def order(sentence):
    if sentence == '':
        return ''
    
    dc = {}
    words = sentence.split()

    for word in words:
        for ch in word:
            if ch.isdigit():
                dc[int(ch)] = word
    
    result = [dc[key] for key in sorted(dc)]
    return ' '.join(result)



def order(sentence):
    return ' '.join(sorted(sentence.split(), key=lambda w: sorted(w)))