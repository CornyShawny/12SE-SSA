def check_api_key(key):
    if key == "mysecret":
        return True
    else:
        return False

# Modify so it accepts any key from: ["key1", "key2", "mysecret"]
print(check_api_key("wrongkey"))  # False