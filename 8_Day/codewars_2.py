"Link : https://www.codewars.com/kata/576b93db1129fcf2200001e6/python"
# Sum without highest and lowest number

def sum_array(arr):
    if arr is None or len(arr) <= 3:
        return 0
    
    return sum(arr) - max(arr) - min(arr)



# Alternative (Sorting approach) this is Also correct, but slightly slower (sorting)
def sum_array(arr):
    if arr is None or len(arr) <= 1:
        return 0
    
    arr = sorted(arr)
    return sum(arr[1:-1])




def sum_array(arr):
    return sum(sorted(arr)[1:-1]) if arr else 0




def sum_array(arr):
    return sum(arr) - min(arr) - max(arr) if arr and len(arr) > 1 else 0

print(sum_array([1,2,3]))