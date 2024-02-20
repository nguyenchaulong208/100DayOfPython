#CONDITIONAL

#if/else
#if: điều kiện kiểm tra,nếu điều kiện đúng thì sẽ thực hiện câu lệnh
#else: nếu điều kiện sai thì sẽ thực hiện câu lệnh bên dưới
#Cấu trúc if/else
'''
if condition:
    do this
else:
    do this

CÁC TOÁN TỬ:
> Greater than
< Less than
>= Greater than or equal to
<= Less than or equal to
== Equal to
!= Not equal to
'''
print("Ví dụ về if/else")
input_conditional = int(input("Nhập vào chiều cao của bạn: "))

if input_conditional >= 120:
    print("Mua vé thành công")
else:
    print("Mua vé tàu thất bại, bạn không đủ chiều cao quy định.")
print("-------------------")

#elif: nếu điều kiện if sai thì sẽ xét đến điều kiện elif.
print('ví dụ elif')
input_conditional2 = int(input("Nhập vào chiều cao của bạn: "))

if input_conditional2 >= 120:
    print("Xác nhận mua vé.")
    age = int(input("Nhập vào số tuổi của bạn: "))
    if age < 12:
        print("Vui lòng thanh toán $5.")
    elif age <= 18:
        print("Vui lòng thanh toán $7.")
    else:
        print("Vui lòng thanh toán $12")
else:
    print("Mua vé tàu thất bại, bạn không đủ chiều cao quy định.")

#Multiple if: khi có nhiều mệnh đề if, nếu các mệnh đề if đó điều đúng thì cả 3 câu lệnh trong mệnh đề if đó đều thực hiện.
print("---------")
print("ví dụ multiple if")
input_conditional3 = int(input("Nhập vào chiều cao của bạn: "))

if input_conditional3 >= 120:
    print("Xác nhận mua vé.")
    age1 = int(input("Nhập vào số tuổi của bạn: "))
    if age1 < 12:
        print("Giá vé là $5.")
    elif age1 <= 18:
        print("Giá vé là $7.")
    else:
        print("Giá vé là $12")
    option = input("Bạn có muốn chụp ảnh không? Y or N.")
    if option == "Y":
        print("Bạn phải thanh toán thêm $3")
    
    print("Hoàn tất thanh toán")
else:

    print("Mua vé tàu thất bại, bạn không đủ chiều cao quy định.")

#Logical