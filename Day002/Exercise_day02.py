'''
INSTRUCTIONS

I was reading this article by Tim Urban - Your Life in Weeks and relisesd just how little time we actually have.
Create a program using maths and f-String that tell uus how many we have left, if we live until 90 years old.

It will take your current ages as the input and output a message with our time left in this format:
You have x weeks left.

Where x is replace with actual caculated number of weeks the input ages has left until age 90.

Warning your output should match the Example output format exactly, even the position of the commas and full stops.

Example input:
56

Example output:
 You have 1768 weeks left.
'''

age_input = int(input("Enter your age: "))

weeks_left = (90 - age_input) * 52
print(f"You have {weeks_left} weeks left.")
