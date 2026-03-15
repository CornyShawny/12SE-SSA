import re

def validate_username(username):
    return re.fullmatch(r'^[A-Za-z][A-Za-z0-9_.]{4,19}$', username) is not None

# Change the function so usernames:
# - start with a letter,
# - contain only letters, numbers, underscores or dots,
# - are 5-20 characters long.
print(validate_username('user_1'))   # True or False?