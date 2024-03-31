'''
1.
- Để định nghĩa 1 hàm ta dùng từ khóa def và tên hàm. để phân biệt tên hàm với biến ta dùng () và kết thúc hàm bằng dấu :
ví dụ:
def my_function():
    Do this
    Then do this
    Finally do this

    
- Để gọi hàm vừa định nghĩa ta dùng câu lệnh sau:
my_function()
- Mục đích định nghĩa ra hàm là có thể tái sử dụng, code trông gọn gàng hơn, áp dụng các tính chất kế thừa, đa hình,....
*Trên đây là 1 hàm đơn giản không có parameter truyền vào
'''
#Ví dụ 1:
# def my_function():
#     print('Đây là hàm tự định nghĩa có tên my_function')

# #Gọi hàm my_function
# my_function()

#While
'''
Vòng lặp while là vòng lặp chỉ dừng lại khi đúng với điều kiện sai, khác với vòng lặp for
while something_is_true:

    Do this
    Then do this
    Then do this
'''
#Ví dụ

number = 0
while number < 50:
    number = number + 1
    print(number)