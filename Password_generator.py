import random
import string

def generate_password(length, chars):
    password = ""
    for i in range(length):
        password += random.choice(chars)
    return password

length = int(input("Введите длину пароля: "))
use_lowercase = input("Включать ли строчные буквы? (y/n): ")
use_uppercase = input("Включать ли заглавные буквы? (y/n): ")
use_digits = input("Включать ли цифры? (y/n): ")
use_symbols = input("Включать ли символы? (y/n): ")

chars = ""
if use_lowercase.lower() == "y":
    chars += string.ascii_lowercase
if use_uppercase.lower() == "y":
    chars += string.ascii_uppercase
if use_digits.lower() == "y":
    chars += string.digits
if use_symbols.lower() == "y":
    chars += string.punctuation

password = generate_password(length, chars)
print("Сгенерированный пароль: " + password)
