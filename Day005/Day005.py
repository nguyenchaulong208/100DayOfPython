#LOOP
fruits = ['Apple','Peach', 'Pear']

for fruit in fruits:
    print(fruit)
    print(f"{fruit} Pie")

print(fruits)
print('---------')

#LOOP RANGE()

#range(start,stop)
#sẽ duyệt từ start đến stop -1
#Start mặc định bắt đầu từ 0
for number in range(1,10):
    print(number)

print('---------')
#for với bước lặp có khoảng cách:
for number_1 in range(1,10,3):
    print(number_1)