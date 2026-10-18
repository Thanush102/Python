is_logged_in = True

def require_login(func):
    def wrapper():
        if is_logged_in:
            func()
        else:
            print("Access Denied! Please log in.")
    return wrapper
@require_login
def dashboard():
    print("Welcome to your dashboard!")
# User is logged in
dashboard()

# User is not logged in
is_logged_in = False
dashboard()

'''
Output:
Welcome to your dashboard!
Access Denied! Please log in.
'''
