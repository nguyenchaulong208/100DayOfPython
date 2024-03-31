#Functions with inputs
#Đây là 1 hàm k có parameter truyền vào
def greet():
    print('Hello')
    print('How do you do')
    print("Isn't the weather nice today?")

greet()

#Hàm có parameter truyền vào là hàm khi được đươc gọi thì các giá trị của hàm gọi sẽ truyền vào hàm được gọi.
#Ví dụ:

def your_name(name):
    print(f'Your name is: {name}')

input_name = input('Enter your name: ')
your_name(input_name)
#parameter là input_name, dữ liệu nhập vàoinput_name gọi là đối số