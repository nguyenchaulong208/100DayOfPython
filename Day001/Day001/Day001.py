# Day1
print("Day 1 - Python Print Function")
print("The function is declared like this:")
print("print('what to print')")

#Day 1 - String Manipulation and Code Intelligence
    #Tach thanh nhieu dong
print("--------------------")
print("tach thanh nhieu dong")
print("Hello world!\nHello world\nHello world")
    
        #Ket hop chuoi
print("--------------------")
print("Ket hop chuoi: ")
print("Hello" + " " + "Theodore")
print("--------------------")
#Dung comment de debug tung dong
print(" Day 1 - String Manipulation\nString Concatenation is done with the "+" sign.\ne.g. print(\"Hello \" + \"world\")\nNew lines can be created with a backslash and n.")
print("--------------------")
#Input function
print("Input function: ")
print("What is your name?")
print("--------------------")
    #Thay vi dung print de hien thi cau hoi de nhap ten, ta dung input function de hien thi cau hoi va luu gia tri nhap
        #input() function
        #input("A prompt for the user") => khi chay chuong trinh, se hien thi cau "A prompt for the user" va cho nguoi dung nhap gia tri
        #Ex:
input("What is your name?\n")
print("--------------")
    #Ket hop input function voi print function
print("Ket hop input function voi print function:")
print("Hello " + input("What is your name?\n")) 
    # => khi chay chuong trinh, se hien thi cau "What is your name?" va cho nguoi dung nhap gia tri sau do hien thi cau "Hello" + gia tri vua nhap
print("--------------------")
    #len() function => tra ve do dai cua chuoi
print(len(input()))
    # => Hien thi so luong ky tu cua chuoi vua nhap
print("--------------------")
print("--------------------")

                                            #VARIBLES
    #Luu gia tri vua nhap vao bien
name = input("What is your name?\n") # => luu gia tri vua nhap vao bien name de su dung sau nay
print("Gia tri vua nhap la: " + name)
#luu nhieu  gia tri vao 1 bien name
name = "Theodore"
print("Gia tri vua nhap la: " + name)
# => gia tri vua nhap se bi ghi de boi gia tri moi luu vao bien name la "Theodore"
#ex: hien thi so luong ky tu cua chuoi vua nhap => Cach nay se giup code ngan gon hon de nhin hon
name = input("What is your name?\n")
length = len(name)
print(length)
print("**************************")
        #EXERCISE 1
#Day 1 - Exercise 1
#Input function - Output function
print("Day 1 - Exercise 1")
#Instructions
print("Instructions: This program takes two inputs. The first input is stored in a variable called a. the second input is stored in a variable called b.\nWrite a program that swictches the values stored in the variables a and b.")
print("|------------------------|")
#Code
a = input()
b = input()
#Dung bien trung gian de luu gia tri cua bien a va sau do hoan doi gia tri cua bien a va b
c = a
a = b
b = c
print("a: " + a)
print("b: " + b)





