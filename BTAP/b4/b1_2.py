sinh_vien = {
    "ho_ten": "Do Van Duy",
    "nam_sinh": 2006,
    "diem_tb": 8.5
}

# Thêm khóa mới
sinh_vien["lop"] = "DH14C1"

# Sửa giá trị của khóa đã có
sinh_vien["diem_tb"] = 9.0

# In Dictionary sau khi thêm và sửa
print(sinh_vien)

# Xóa theo khóa và lấy ra giá trị vừa xóa
diem_cu = sinh_vien.pop("diem_tb")

print(sinh_vien)
print("Diem da xoa:", diem_cu)

# Cập nhật / thêm nhiều khóa
sinh_vien.update({
    "nam_sinh": 2003,
    "email": "a@example.com"
})

# In kết quả cuối cùng
print(sinh_vien)