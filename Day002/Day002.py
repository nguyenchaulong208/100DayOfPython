#Data type
'''
Cac kieu du lieu trong python
1. Number
    1.1 int
    1.2 float
2. String
    ex:
    "Hello" or 'Hello'
3. Boolean
'''

#Ex:
#string
print("Ví dụ kiểu dữ liệu string:")
print("Hello"[0]) # => in ra ký tự chỉ mục [0] là H => đây cũng là cách truy cập vào các ký tự trong chuỗi thông qua các chỉ mục
print("Hello"[4]) # => in ra ký tự chỉ mục [4] là o
print("123"+"345") # => in ra chuỗi 123345 => cộng chuỗi/ nối chuỗi/ nối các ký tự trong chuỗi

#integer
#để khai báo số nguyên, ta chỉ cần gán giá trị cho biến
#Phân cách các chữ số bằng dấu phẩy (,) trong python không được hỗ trợ => ta có thể sử dụng dấu gạch dưới (_) để phân cách các chữ số trong số nguyên để dễ đọc hơn khi code 
#=> python sẽ tự động bỏ qua dấu gạch dưới khi chạy chương trình 
#Ex:
print("Ví dụ kiểu dữ liệu interger:")
num = 123_456_789 # => in ra 123456789
print(num)
number = 123 #Không cân khai báo kiểu dữ liệu cho biến number là int hay gì cả => python tự hiểu là biến number là kiểu int
print(number) #=> in ra 123

#float
#để khai báo số thực, ta chỉ cần gán giá trị cho biến
#Ex:
print("Ví dụ kiểu dữ liệu float:")
float = 3.14159
print(float) #=> in ra 3.14159

#boolean
#để khai báo biến boolean, ta chỉ cần gán giá trị cho biến
#Ex:
print("Ví dụ kiểu dữ liệu Bool:")
bool = True
print(bool) #=> in ra True
bool = False
print(bool) #=> in ra False
print("-----------------")
#-----------------------------

                            # F String
#f-string là chuyển các kiểu dữ liệu khác về dạng string và in ra màn hình
#ex
print("Ví dụ về f-string")

score = 0
height = 10
print(f"score là: {score}, height là: {height}")