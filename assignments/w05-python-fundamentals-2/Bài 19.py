a, b = map(float, input("Nhập a và b: ").split())
if a > 0:
    x = -b/a
    print(f"Nghiệm của bất phương trình là: x >= {x}")
elif a < 0:
    x = -b/a
    print(f"Nghiệm của bất phương trình là: x <= {x}")
else:
    if b > 0:
        print("Bất phương trình vô nghiệm")
    else:
        print("Bất phương trình có vô số nghiệm")