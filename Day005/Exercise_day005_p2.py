
for number in range(1,101):
    if (number % 3 != 0 and number % 5 != 0):
        print(number)
    if(number % 3 == 0 and number % 5 == 0):
        print('Fizz Buzz')
    if number % 3 == 0:
        print('Fizz')
    if number % 5 == 0:
        print('Buzz')
print('------')

    
#Đáp án
print('Code mẫu')
target = 100
for number in range(1,target + 1):
    if(number % 3 == 0 and number % 5 == 0):
        print('FizzBuzz')
    if number % 3 == 0:
        print('Fizz')
    if number % 5 == 0:
        print('Buzz')
    else:
        print(number)
    