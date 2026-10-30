n = int(input("Nhập số n: "))
for i in range(1, n):
    tong = 0
    for j in range(1, i):
        if i % j == 0:
            tong = tong + j
    if tong == i:
        print(i)