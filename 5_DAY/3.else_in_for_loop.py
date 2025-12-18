# else in for loop
for i in range(5):
    print(i)
else:
    print("else part") # this will execute always

for i in range(5):
    print(i)
    if i==3:
        break
else:
    print("else part") # this will not executed