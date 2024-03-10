import random
#Project Create a Password Generator
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h' ,'i' ,'k' , 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z','A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I' ,'J', 'K', 'L', 'M', 'N', 'O','P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['~','!', '@', '#', '$', '%', '^', '&', '(', ')', '-', '*', '_', '+', '=']

print('Welcome to the Password Generator!')
input_letters = int(input('How many letter would you like in your password?\n'))
input_numbers = int(input('How many number would you like in your password?\n'))
input_symbol = int(input('How many symbol would you like in your password?\n'))

#Easy level
#random letters
password = ""

for char in range(input_letters + 1):
    random_char = random.choice(letters) #choice sẽ lấy ngẫu nhiên 1 phần tử từ mảng có sẵn, cụ thể ở đây là lấy 1 phần tử ngẫu nhiên ở mảng letters
    #nối chuỗi
    password = password + random_char
#random symbol
for char in range(input_numbers + 1):
    random_number = random.choice(numbers) #choice sẽ lấy ngẫu nhiên 1 phần tử từ mảng có sẵn, cụ thể ở đây là lấy 1 phần tử ngẫu nhiên ở mảng letters
    #nối chuỗi
    password = password + random_number
#random number
for char in range(input_symbol + 1):
    random_symbols = random.choice(symbols) #choice sẽ lấy ngẫu nhiên 1 phần tử từ mảng có sẵn, cụ thể ở đây là lấy 1 phần tử ngẫu nhiên ở mảng letters
    #nối chuỗi
    password = password + random_symbols
print('Your password is: ', password)

#Hard level
password_hardlv = ''
password_list = []
for char in range(input_letters + 1):
    password_list.append(random.choice(letters)) #choice sẽ lấy ngẫu nhiên 1 phần tử từ mảng có sẵn, cụ thể ở đây là lấy 1 phần tử ngẫu nhiên ở mảng letters    
#random symbol
for char in range(input_numbers + 1):
    password_list.append(random.choice(numbers)) #choice sẽ lấy ngẫu nhiên 1 phần tử từ mảng có sẵn, cụ thể ở đây là lấy 1 phần tử ngẫu nhiên ở mảng letters
#random number
for char in range(input_symbol + 1):
    password_list.append(random.choice(symbols)) #choice sẽ lấy ngẫu nhiên 1 phần tử từ mảng có sẵn, cụ thể ở đây là lấy 1 phần tử ngẫu nhiên ở mảng letters
resutl = random.shuffle(password_list)
for pw in password_list:
    password_hardlv = password_hardlv + pw
print('Your password is: ',password_hardlv)