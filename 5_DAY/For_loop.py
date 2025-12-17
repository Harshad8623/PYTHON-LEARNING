# FOR LOOP EXAMPLES

name = "Harshad"
for i in name:
    print(i)
print()

for i in range(5):
    print(i)
print()

for i in range(0,5):
    print(i)
print()

for i in range(1,10,2):
    print(i)
print()

for i in range(5,0,-1):
    print(i)
print()


# list
seq = [11,22,33,46,59]
for var in seq:
    print(var)
print()


# String
for i in "PYTHON":
    print(i)
print()


# Tuple
for i in (10,20,30,40,90):
    print(i)


# Set
for i in {2,4,6,8,10}:
    print(i)


# Dictonary
dic = {"FIRST NAME":'HARSHAD',"MIDDLE NAME":'MADHAV',"SIR NAME":'DHUPPE'}
for i in dic:
    print(i)  # print keys

for i in dic.values():
    print(i)  # print values

for i in dic.items():
    print(i)