mon_hoc_ky1 = {"Toan", "Ly", "Hoa", "Van"}
mon_hoc_ky2 = {"Toan", "Anh", "Tin", "Van"}

# Giao: môn học chung của 2 học kỳ
print(mon_hoc_ky1 & mon_hoc_ky2)

# Hợp: tất cả môn học của cả 2 học kỳ
print(mon_hoc_ky1 | mon_hoc_ky2)

# Hiệu: môn chỉ có ở học kỳ 1
print(mon_hoc_ky1 - mon_hoc_ky2)