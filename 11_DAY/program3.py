# Link : https://www.codewars.com/kata/5324945e2ece5e1f32000370/train/python

def sum_strings(x, y):
    x = x.lstrip('0') or '0'
    y = y.lstrip('0') or '0'
    
    i, j = len(x) - 1, len(y) - 1
    carry = 0
    result = []

    while i >= 0 or j >= 0 or carry:
        digit_x = ord(x[i]) - ord('0') if i >= 0 else 0
        digit_y = ord(y[j]) - ord('0') if j >= 0 else 0

        total = digit_x + digit_y + carry
        result.append(str(total % 10))
        carry = total // 10

        i -= 1
        j -= 1

    return ''.join(result[::-1])
