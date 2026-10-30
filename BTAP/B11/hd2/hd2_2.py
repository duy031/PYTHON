import pandas as pd

# Đọc file dữ liệu điểm sinh viên
df = pd.read_csv("diem_sinh_vien.csv")

print("=== BÀI TẬP 2.2 – THỐNG KÊ THEO MÔN HỌC ===")

# 1. Tính điểm trung bình theo từng môn học
diem_trung_binh_mon = df.groupby("mon_hoc")["diem"].mean()
print("\nĐiểm trung bình theo từng môn học:")
print(diem_trung_binh_mon)

# 2. Thống kê chung cho toàn bộ bảng điểm
print("\nĐiểm trung bình toàn bộ (tất cả các môn):", round(df["diem"].mean(), 2))
print("Điểm cao nhất toàn bộ:", df["diem"].max())
print("Điểm thấp nhất toàn bộ:", df["diem"].min())