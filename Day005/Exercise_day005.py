'''
You are going to write a program that calculates the sum of all the even numbers from 1 to X, if X is 100 then the first even number would be 2 the last on is 100
i.e. 2 + 4 +6 +8 + ... + 98 + 100
Important, there should only be 1 print statement in your console ouput.
it should just print the final total and not every step of the calculateion.
also we will be constrain the inputs to only take numbers from 0 to a max of 1000.

Example input1
10
Example output1
30

Example input1
52
Example output1
702
'''
target = int(input('Enter your number: '))
even_sum = 0

for number in range(2, target +1 ,2):
    even_sum += number
print('Result: ', even_sum)