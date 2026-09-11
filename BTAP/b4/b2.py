diem_mon_hoc = {
    "Toán": 8.0,
    "Lý": 7.5,
    "Hóa": 9.0,
    "Văn": 6.5
}
print ("Môn học:")
# Duyệt qua các khóa
for mon in diem_mon_hoc.keys():
    print(mon)

print("Điểm các môn:")
# Duyệt qua các giá trị
for diem in diem_mon_hoc.values():
    print(diem)

# Duyệt qua cả khóa và giá trị
for mon, diem in diem_mon_hoc.items():
    print(f"{mon}: {diem}")

# Tính tổng điểm
tong_diem = 0

for diem in diem_mon_hoc.values():
    tong_diem = tong_diem + diem

# Tính điểm trung bình
print("Diem trung binh:", round(tong_diem / len(diem_mon_hoc), 2))