import re

def validate_username(username):
    return re.fullmatch(r'\w{3,15}', username) is not None

# Change the function so usernames:
# - start with a letter,
# - contain only letters, numbers, underscores or dots,
# - are 5-20 characters long.
print(validate_username('user_1'))   # True or False?