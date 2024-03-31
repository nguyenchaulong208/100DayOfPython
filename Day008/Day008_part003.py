#Function với nhiều parameter
#Khi truyền vào các đối số cần chú ý đến vị trí của hàm gọi tương đương với vị trí của hàm được gọi, nếu k đúng vị trí thì kết quả xử lý sẽ sai

def greet_with(name, location):
    print(f'Hello {name}')
    print(f'What is it like in {location}')
greet_with("Jack Bauer", "Nowhere")
print('----')
#Ví dụ về sắp xếp đối số không tương ứng nhau
def greet_with(name, location):
    print(f'Hello {name}')
    print(f'What is it like in {location}')
greet_with("Nowhere", "Jack Bauer")
print('----')
#Lúc này name bị đảo ngược lại thành Nowhere và location thành Jack Bauer, trong 1 số trường hợp nuế 2 đối số khác kiểu dữ liệu sẽ báo lỗi
#Dùng các từ khóa đối số để tránh nhầm lẫn khi truyền các đối số
#ví dụ
def greet_with(name, location):
    print(f'Hello {name}')
    print(f'What is it like in {location}')

name = "Jack Bauer"
location = "Nowhere"
greet_with(name, location)
print('----')