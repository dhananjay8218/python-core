# Custom exceptions let you define application-specific error types.

# Example 1: Using built-in exceptions
def process_item(name):
    allowed = ["typeA", "typeB", "typeC"]
    if name not in allowed:
        raise ValueError("Unsupported item type")
    print("Processing:", name)

try:
    process_item("unknown")
except ValueError as e:
    print("Error:", e)


# Example 2: Custom exception class
class MissingResourceError(Exception):
    """Raised when a required resource is missing."""
    pass

def create_product(material, quantity):
    if material is None or quantity <= 0:
        raise MissingResourceError("Missing material or invalid quantity")
    print("Product created")

try:
    create_product(None, 10)
except MissingResourceError as e:
    print("Custom Error:", e)


# Example 3: Another custom exception with additional conditions
class ValidationError(Exception):
    """Raised when validation fails."""
    pass

def register_user(name, age):
    if not name:
        raise ValidationError("Name cannot be empty")
    if age < 18:
        raise ValidationError("User must be 18+")
    print("User registered:", name)

try:
    register_user("", 20)
except ValidationError as e:
    print("Validation Error:", e)

try:
    register_user("Alex", 16)
except ValidationError as e:
    print("Validation Error:", e)


# Example 4: Combining multiple custom exceptions
class AccessDeniedError(Exception):
    """Raised when user does not have required permissions."""
    pass

def open_panel(role):
    if role != "admin":
        raise AccessDeniedError("Admin privileges required")
    print("Panel opened")

try:
    open_panel("guest")
except AccessDeniedError as e:
    print("Access Error:", e)


# Example 5: Using custom exceptions inside workflows
def system_check(config):
    if "version" not in config:
        raise MissingResourceError("System version missing")
    if config.get("mode") not in ["auto", "manual"]:
        raise ValidationError("Mode must be 'auto' or 'manual'")
    print("System check passed")

try:
    system_check({"mode": "invalid"})
except (MissingResourceError, ValidationError) as e:
    print("System Error:", e)
