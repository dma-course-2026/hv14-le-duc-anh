M, N = map(int, input("Nhập M và N: ").split())
if M % 2 == N % 2 or M % 2 == 0 and N % 2 == 0:
    print("ĐÚNG")
else:
    print("SAI")
