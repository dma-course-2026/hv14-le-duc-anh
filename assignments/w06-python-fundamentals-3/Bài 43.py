n = int(input("Nhập n: "))
souoc = 0
for i in range(1, n + 1):
    if n % i == 0:
        souoc = souoc + 1
print(n, "có", souoc, "ước")