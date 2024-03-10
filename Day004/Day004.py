#RANDOM MODULE
#Random Module Python sử dụng là Mersenne Twister
    #Mersenne Twister là một trình tạo số giả ngẫu nhiên đa năng (PRNG) được phát triển vào năm 1997 bởi Makoto Matsumoto [ja] (本) và Takuji Nishimura (西 德 ).
    #Tên của nó bắt nguồn từ thực tế là độ dài thời gian của nó được chọn là một Mersenne nguyên.
#Để sử dụng được module thì phải import random
import random
#Random với số nguyên
randomNumber = random.randint(1, 100)
print(randomNumber)
#Random với số thập phân
    #Dùng .random(), random() chỉ trả về kết quả từ 0,000 - 0.9999
    #mở rộng hơn để random() số thập phân với phạm vi lớn hơn thì ta dùng phép * giữ giá trị random() và 1 số nguyên hoặc giá trị của randint(x,y)
random_float = random.random()
print(random_float * randomNumber)
print(random_float * 5)
#Định nghĩa 1 module và sử dụng biến đó từ 1 file .py khác bên trong project.
#Để sử dụng module đó thì ta import file .py có chứa module vào file .py hiện tại
#Ví dụ sử dụng biến Pi từ file my_module.py
import my_module
print(my_module.pi)

#DANH SÁCH trong Python
#Danh sách trong python là 1 cấu trúc dữ liệu, là 1 cách tổ chức dữ liệu và lưu trữ dữ liệu bằng python
#Python không quan tâm kiểu dữ liệu bên trong danh sách
    #Ví dụ về danh sách
fruits = ["item1", "item2",1, 2, 0.002,54.78, True, False]
print(fruits)
#in kết quả theo chỉ muc
print(fruits[3])
print(fruits[2])