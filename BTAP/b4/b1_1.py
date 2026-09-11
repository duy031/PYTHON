sinh_vien = {
    "ho ten": "Do Van Duy",
    "nam sinh": 2006,
    "diem tb": 8.5
}
#Truy suất theo khóa 
print (sinh_vien["ho_ten"])
#Truy suất an toàn bằng get()
print (sinh_vien.get("diem_tb"))
#get() với giá trị mặc định nếu không có khóa 
print (sinh_vien.get("lop", "chua co"))
#thứ truy suất khóa không tồn tại 
#print(sinh-vien["lop"])   #sẽ bị lỗi keyError