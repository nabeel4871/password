import secrets
import string

def generate_password(length=16):
    # Define the character set: uppercase, lowercase, digits, and punctuation
    characters = string.ascii_letters + string.digits + string.punctuation
    
    # Generate a secure random password
    password = ''.join(secrets.choice(characters) for _ in range(length))
    
    return password

def generate_multiple_passwords(count=5, length=16):
    passwords = [generate_password(length) for _ in range(count)]
    return passwords

# Example usage:
passwords = generate_multiple_passwords(count=5, length=16)  # You can specify the number and length of passwords
for idx, pwd in enumerate(passwords, 1):
    print(f"Password {idx}: {pwd}")