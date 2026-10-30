a, b, c = map(float, input("Nhập 3 cạnh tam giác: ").split())
if a + b < c or a + c < b or b + c < a:
    print("Không phải là tam giác")
elif a <= 0 or b <= 0 or c <= 0:
    print("Không phải là tam giác")
elif a**2 + b**2 == c**2 or b**2 + c**2 == a**2 or a**2 + c**2 == b**2:
    print("Đây là tam giác vuông")
else:
    print("Đây không phải là tam giác vuông")