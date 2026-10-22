a, b = map(int, input("Nhập hai số nguyên: ").split())
phep_toan = input("Nhập phép toán (+, -, *, /): ")
if phep_toan == "+":
    ket_qua = a + b
elif phep_toan == "-":
    ket_qua = a - b
elif phep_toan == "*":
    ket_qua = a * b
elif phep_toan == "/":
    if b == 0:
        ket_qua = "Lỗi: Chia cho zero"
    else:
        ket_qua = a / b
print(f"Kết quả của {a} {phep_toan} {b} là: {ket_qua}")