n = int(input("Nhập n: "))
tong = 0
for i in range(1, n):
    if n % i == 0:
        tong = tong + i
if tong == n:
    print(n, "là số hoàn hảo")
else:
    print(n, "không phải là số hoàn hảo")