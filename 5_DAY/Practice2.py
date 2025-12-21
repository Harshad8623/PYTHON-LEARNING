# Star Patterns

for i in range(8):
    print("*")


for i in range(8):
    print(i*"*")


for i in range(8):
    print(" "*(8-i),end='')
    print('*'*i)


for i in range(8):
    print(" "*i,"*"*i)