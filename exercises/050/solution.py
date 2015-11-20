a = 0
b = 0
for i in range(0, 1000):
    if i % 3 == 0:
        a = a + i
    if i % 5 == 0:
        b = b + i
print(a + b)
