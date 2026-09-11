diem_mon_hoc = {
    "Toan": 8.0,
    "Ly": 7.5,
    "Hoa": 9.0,
    "Van": 6.5
}

# Cộng thêm 0.5 điểm cho mỗi môn

diem_cong_diem = {
    mon: round(diem + 0.5, 2)
    for mon, diem in diem_mon_hoc.items()
}

print(diem_cong_diem)
print(" ")
print("Cộng thêm 0.5 điểm mỗi môn và đổi thành chữ hoa!")
print(" ")
# Đổi tên môn thành chữ in hoa
ten_mon_viet_hoa = {
    mon.upper(): diem
    for mon, diem in diem_mon_hoc.items()
}

print(ten_mon_viet_hoa)