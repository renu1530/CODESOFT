
import random

letters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
numbers = "0123456789"
symbols = "!@#$%^&*()"

all = letters + numbers + symbols

length = int(input("Enter the length of password : "))

password = ""

for i in range(length):
  password += random.choice(all)

print(password)

