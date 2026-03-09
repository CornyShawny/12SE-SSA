def get_username(data):
    try:
        return data['username']
    except Exception:
        return "Error: Invalid data"

# Modify so it catches only KeyError and returns "Error: Missing username";
# other exceptions should return "Error: Invalid data".
print(get_username({}))          # What prints?
print(get_username({'username': 'Sam'}))