# --- BAI 1 ---
n = int(input("Nhập vào số nguyên n: "))
print("Số gấp đôi của n là", 2 * n)
# --- BAI 2 ---
import math
a = float(input("Nhập vào số thực a: "))
b = float(input("Nhập vào số thực b: "))
r = float(input("Nhập vào số thực r: "))
diện_tích_hình_chữ_nhật = a * b
diện_tích_hình_tròn = math.pi * r**2
diện_tích_còn_lại = diện_tích_hình_chữ_nhật - diện_tích_hình_tròn
print("Diện tích còn lại là", diện_tích_còn_lại)
# --- BAI 3 ---
c = input("Nhập vào ký tự c: ")
if c == 'C':
    print("c bằng C")
else:
    print("C bằng c")
# --- BAI 4 ---
c = input("Nhập vào ký tự c: ")
if c.isalpha():
    print("c là ký tự chữ cái")
else:
    print("c không phải ký tự chữ cái")
# --- BAI 5 ---