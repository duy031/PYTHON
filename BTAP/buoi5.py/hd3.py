# for với range()
for i in range(1, 6):
    print(i)

# for duyệt List
diem_so = [8.5, 7.0, 9.2, 6.5]

for diem in diem_so:
    print("Diem:", diem)

# for duyệt Tuple
toa_do = (3, 5)

for gia_tri in toa_do:
    print(gia_tri)

# for duyệt Dictionary
diem_mon = {
    "Toan": 8.0,
    "Ly": 7.5
}

for mon, diem in diem_mon.items():
    print(mon, ":", diem)

# for duyệt String
ten = "Python"

for ky_tu in ten:
    print(ky_tu)

# Bài vận dụng – Bảng cửu chương
n = 5

for i in range(1, 11):
    print(f"{n} x {i} = {n * i}")
    