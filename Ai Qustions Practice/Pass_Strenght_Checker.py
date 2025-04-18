# Password Strength Checker
# CODE BY LUCKY

password = input("Enter Password: ")
length = len(password)

if password.isspace() or password == "":
    print("Password cannot be empty or just spaces!")
elif password.isdigit():
    print("Only digits not allowed! Weak Password ❌")
elif length <= 8:
    print(password, "is Weak ❌ (Too short)")
else:
    print(password, "is a Good Password ✅")
