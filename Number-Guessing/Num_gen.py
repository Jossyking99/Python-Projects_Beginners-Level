# Importing random module 
import random

#Great the user and ask for their name
name = input("please enter your name: ")
print(f"Hello Dev {name}👨‍💻 welcome to the password generator.")

# Asking user for the length of the password to be generated
pass_len = int(input("Enter the length of the password: "))

# Characters and symbols to generate password
pass_data = "qwertyuiopasdfgjklzxcvbnm1234567890[];',./!@#$%^&*()_+:<>?"

# Using random.sample() to collect random data from pass_data as a list & using .join() to join the list elements to form a string
password = "".join(random.sample(pass_data, pass_len))

print(password)