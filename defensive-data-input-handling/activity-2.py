import re

def sanitize_input(user_input):
    sanitized = re.sub(r'<script.*?>.*?</script>', '', user_input,
                       flags=re.IGNORECASE | re.DOTALL)
    sanitized = sanitized.replace('&', '&amp;').replace('<', '&lt;').replace('>', '&gt;')
    return sanitized

def get_valid_username():
    pattern = r'^[A-Za-z0-9_]+$'

    while True:
        username = input("Enter your username: ")
        clean = sanitize_input(username)

        if not (3 <= len(clean) <= 15):
            print("Invalid username: length must be between 3 and 15 characters.")
            continue

        if not re.match(pattern, clean):
            print("Invalid username: only letters, numbers, and underscores are allowed.")
            continue

        return clean

username = get_valid_username()
print(f"Welcome, {username}!")