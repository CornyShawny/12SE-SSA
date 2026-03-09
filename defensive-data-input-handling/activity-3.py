import re

def sanitize_input(user_input):
    sanitized = re.sub(r'<script.*?>.*?</script>', '', user_input,
                       flags=re.IGNORECASE | re.DOTALL)
    sanitized = sanitized.replace('&', '&amp;').replace('<', '&lt;').replace('>', '&gt;')
    return sanitized

def get_valid_comment():
    while True:
        comment = input("Write your comment: ")
        clean = sanitize_input(comment)

        if len(clean) > 200:
            print("Comment exceeds 200 characters. Make sure it's under 200 characters.")
            continue

        return clean

comment = get_valid_comment()
print(f"User comment: {comment}")