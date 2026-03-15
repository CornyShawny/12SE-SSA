def check_api_key(key):
    if key in ["mysecret", "key1", "key2"]:
        return True
    else:
        return False

# Modify so it accepts any key from: ["key1", "key2", "mysecret"]
print(check_api_key("wrongkey"))  # False