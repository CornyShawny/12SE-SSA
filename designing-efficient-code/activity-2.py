import time

sessions = {}

def create_session(user_id):
    # Sets login_time to None - improve this to capture the actual login time (current timestamp)
    sessions[user_id] = {'login_time': time.time(), 'data': {}}

def login_user(user_id):
    sessions[user_id]['login_time'] = time.time()  # This should be replaced with the real current time

def is_session_active(user_id, timeout):
    if user_id in sessions:
        return (time.time() - sessions[user_id]['login_time']) < timeout
    return True

# Task:
# - Update create_session and login_user to correctly store the current login timestamp.
# - Implement a function is_session_active(user_id, timeout) that returns True if the user session is active within the timeout period.