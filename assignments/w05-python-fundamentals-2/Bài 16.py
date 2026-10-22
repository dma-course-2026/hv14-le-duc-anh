a, b, c = map(float, input("Nhập 3 cạnh tam giác: ").split())
if a + b < c or a + c < b or b + c < a:
    print("Không phải là tam giác")
elif a <= 0 or b <= 0 or c <= 0:
    print("Không phải là tam giác")
elif a == b or b == c or a == c:
    print("Đây là tam giác cân")
else:
    print("Đây không phải là tam giác cân")