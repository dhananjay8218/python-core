# A decorator modifies or extends the behavior of a function.

from functools import wraps

# Basic decorator
def my_decorator(func):
    @wraps(func)
    def wrapper():
        print("Before function")
        func()
        print("After function")
    return wrapper

@my_decorator
def greet():
    print("Hello from function")

greet()
print(greet.__name__)


# Logging decorator
def log_action(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print("Calling:", func.__name__)
        result = func(*args, **kwargs)
        print("Finished:", func.__name__)
        return result
    return wrapper

@log_action
def process_item(name, status="ok"):
    print("Processing:", name, "Status:", status)

process_item("ItemA")


# Access control decorator
def require_admin(func):
    @wraps(func)
    def wrapper(role):
        if role != "admin":
            print("Access denied")
            return None
        return func(role)
    return wrapper

@require_admin
def open_dashboard(role):
    print("Access granted to dashboard")

open_dashboard("user")
open_dashboard("admin")
