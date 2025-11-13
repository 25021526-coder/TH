# W2A4
a1 = float(input("Nhap vao so diem a1: "))
b1 = float(input("Nhap vao so diem b1: "))
c1 = float(input("Nhap vao so diem c1: "))
a2 = float(input("Nhap vao so diem a2: "))
b2 = float(input("Nhap vao so diem b2: "))
a3 = float(input("Nhap vao so diem a3: "))
TB = ((a1 + b1 + c1) + (a2 + b2) * 2 + a3 * 3) / 10
print("Diem trung binh cua hoc sinh la:", TB)
print (round(TB,1))
# W2A6
chu_thuong = input("Nhap vao mot ki tu chu cai thuong: ")
print("Ma Unicode cua ky tu '{}' la: {}".format(chu_thuong, ord(chu_thuong)))
chu_hoa = chr(ord(chu_thuong) - 32)
print("Ky tu chu cai in hoa tuong ung la: {}".format(chu_hoa))
