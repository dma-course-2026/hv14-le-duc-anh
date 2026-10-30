import math
n = int(input("Nhập n: "))
m = int(math.sqrt(n))
if m * m == n:
    print(n, "là số chính phương")
else:
    print(n, "không phải là số chính phương")