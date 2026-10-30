a = int(input("Nhập cơ số a: "))
n = int(input("Nhập số mũ n: "))

res = 1
for i in range(n):
    res *= a

print(f"{a} lũy thừa {n} = {res}")