#Prime number checker

def prime_checker(number):
    is_prime = True
    for num in range(2, number):
        if number % 2 == 0:
            is_prime = False
    if is_prime:
        print("It's a prime number")

    else:
        print("It's not a prime number")

n = int(input("Enter a number: "))
prime_checker(number=n)