import random

print("Welcome to your Password Generator")

chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!@£$%^&*().,?0123456789'

number = int(input("Amount of passwords to generate: "))

length = int(input("input your password length"))

print("\nhere are your passwords: ")


for pwd in range(number): # This is looping a list of numbers from 0 to whatever number you choose. Each time the loop goes around, it picks one of those numbers from the list.
                        # so if i pick 5 it will loop 5 times
    passwords = " " # We're creating a new variable called passwords and giving it a starting value of an empty space.
    for c in range(length):
        passwords += random.choice(chars) # picks the char and adds it randomly and assign it to a new variable passwords,
                                          #assigns the random to password variable
    print(passwords)