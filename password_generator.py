import string
import random

def generate_password(length, use_upper, use_numbers, use_special):
    if use_upper:
        chars = string.ascii_letters
    else:
        chars = string.ascii_lowercase

    if use_numbers:
        chars += string.digits

    if use_special:
        chars += string.punctuation

    return ''.join(random.choice(chars) for _ in range(length))

def password_generator():
    while True:
        mode = input("Do you want to use default mode (8 characters with mixed letters, numbers, and special characters) or manual mode? (default/manual): ").lower()
        if mode == "default":
            print(f"Generated password: {generate_password(8, True, True, True)}")
            break
        elif mode == "manual":
            length = int(input("Enter the desired password length: "))
            if input(f"Use uppercase letters? (y/n): ").lower() == "y":
                use_upper = True
            else:
                use_upper = False
            if input(f"Use numbers? (y/n): ").lower() == "y":
                use_numbers = True 
            else:
                use_numbers = False 
            if input(f"Use special characters? (y/n): ").lower() == "y":
                use_special = True
            else:
                use_special = False
            print(f"Generated password: {generate_password(length, use_upper, use_numbers, use_special)}")
            break
        else:
            print("Invalid option, please try again.")

if __name__ == "__main__":
    password_generator()