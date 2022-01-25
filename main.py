import random  # we are importing random module

print("password generator")  # displaying program name to user

chars = '1234567890abcdefghijklmnopqrstuvwxyz!@#$%^&*'  # we are creating a string with random characters

number = int(input("how many password you would like to generate?:"))  # asking user for password amount


length = int(input('length?:'))  # asking user for how long they want their password to be

print("here is your password :")

for pwd in range(number):  # looping thru number input

    passwords = None  # declaring the empty password variable
    for c in range(length):  # looping thru length input (nested)
        passwords += random.choice(chars)  # adding random character from char variable for each iteration in length

    print(passwords)  # we are printing final password
    