M = int(input("Nhập M: "))
N = int(input("Nhập N: "))
tong = 0
for i in range(M, N + 1):
    if i % 6 == 0:
        tong = tong + i
print("Kết quả:", tong)