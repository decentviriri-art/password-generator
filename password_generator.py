import random
import string

print("==========================")
print("PASSWORD GENERATE")
print("==========================")

length=int(input("Enter the length of password:"))
if length < 8:
    print("Password must at least 8 characters")
else:
    Characters = (
        string.ascii_uppercase +
        string.ascii_lowercase +
        string.digits +
        string.punctuation
        )
    password =""
    while len(password) < length:
        password_choice=random.choice(Characters)
        password=password + password_choice
    print("\n Password GENERATOR")
    print(password)
