N = int(input("Nhập năm: "))
if N == 0:
    print("Năm không hợp lệ")
else:
    if N % 4 == 0 and N % 100 != 0 or N % 400 == 0:
        print(f"Số ngày của năm {N} là 366")
    else:
        print(f"Số ngày của năm {N} là 365")