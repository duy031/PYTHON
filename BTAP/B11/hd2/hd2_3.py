import pandas as pd

df = pd.read_csv("diem_sinh_vien.csv")

print("=== BÀI TẬP 2.3 – TÍNH ĐTB TỪNG SINH VIÊN & LỌC ĐẠT/KHÔNG ĐẠT ===")

# Tính điểm trung bình từng sinh viên (làm tròn 2 chữ số)
diem_tb_sv = df.groupby("ho_ten")["diem"].mean().round(2)
print("\nĐiểm trung bình của từng sinh viên:")
print(diem_tb_sv)

# Lọc danh sách đạt và không đạt
sinh_vien_dat = diem_tb_sv[diem_tb_sv >= 5.0]
sinh_vien_khong_dat = diem_tb_sv[diem_tb_sv < 5.0]

print("\n--- Danh sách sinh viên đạt (ĐTB >= 5.0) ---")
print(sinh_vien_dat)

print("\n--- Danh sách sinh viên không đạt (ĐTB < 5.0) ---")
if not sinh_vien_khong_dat.empty:
    print(sinh_vien_khong_dat)
else:
    print("Không có sinh viên nào không đạt.")