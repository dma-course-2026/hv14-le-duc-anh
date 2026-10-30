a, b = map(int, input("Nhập a và b: ").split())
if a==0 and b==0:
    print("Không kiểm tra được")
elif a==0:
    print("0 không là ước của", b)
    print(f"{b} không là ước của 0")
elif b==0:
    print("0 là ước của", a)
    print(f"{a} không là ước của 0")
elif a % b == 0:
    print(f"{b} là ước của {a}")
    print(f"{a} không là ước của {b}")
elif b % a == 0:
    print(f"{a} là ước của {b}")
    print(f"{b} không là ước của {a}")
else:
    print(f"{a} không là ước của {b}")
    print(f"{b} không là ước của {a}")