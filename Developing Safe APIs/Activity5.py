def validate_age(age):
    try:
        age_num = int(age)
        if 0 <= age_num <= 120:
            return True
    except ValueError:
        pass
    return False

# Modify so it returns:
# - "Age must be a number" if input is not an int
# - "Age must be between 0 and 120" if out of range
# - "Valid" if age is OK
print(validate_age('abc'))   # False
print(validate_age('25'))    # True