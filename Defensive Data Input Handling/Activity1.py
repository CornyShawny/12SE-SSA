def validate_age():
    while True:
        age_input = input("Please enter your age: ")
        try:
            age = int(age_input)
            if 0 <= age <= 120:
                return age
            else:
                print("Age must be between 0 and 120.")
        except ValueError:
            print("Please enter a whole number.")

valid_age = validate_age()
print(f"Valid age entered: {valid_age}")
