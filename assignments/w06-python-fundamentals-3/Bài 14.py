import math
a, b, c = map(float, input("Nhập 3 cạnh tam giác: ").split())
if a + b < c or a + c < b or b + c < a:
    print("Không phải là tam giác")
elif a <= 0 or b <= 0 or c <= 0:
    print("Không phải là tam giác")
else:
    chuvi = a + b + c
    print(f"Chu vi tam giác là: {chuvi}")
    p = (a + b + c) / 2
    s = math.sqrt(p * (p - a) * (p - b) * (p - c))
    print(f"Diện tích tam giác là: {s}")