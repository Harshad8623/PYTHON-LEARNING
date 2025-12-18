# enumerate is useful for obtaining an indexed list:
# (0, seq[0]), (1, seq[1]), (2, seq[2]), ...
# enumerate() = index + value (from ONE sequence)

for i,j in enumerate('Harshad'):
    print(i,j)

i = range(2, 10, 2)
print(i)