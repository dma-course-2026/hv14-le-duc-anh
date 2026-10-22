M, N = map(int, input("Nhập M và N: ").split())
tong = 0
for i in range(M, N+1):
    if i % 3 == 0 or i % 5 == 0:
        tong += i
print(f"Tổng các số chia hết cho 3 hoặc 5 từ {M} đến {N} = {tong}")