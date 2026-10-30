N = int(input("Nhập N: "))
dem = 0
for i in range(1, N + 1):
    so = int(input("Nhập số: "))
    if so > 10 and so < 20:
        dem = dem + 1
print("Số các số >10 và <20 là:", dem)