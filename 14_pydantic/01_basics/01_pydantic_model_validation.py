#  Data validation using Pydantic
# Pydantic validates input data at runtime using Python type hints.
# If data is invalid or missing, it raises a ValidationError.

from pydantic import BaseModel, ValidationError


# Example 1: Basic model with strict validation
class User(BaseModel):
    id: int
    name: str
    is_active: bool


# Invalid input (id should be int)
user_data = {
    "id": 100,     # invalid value (101a)
    "name": "John Doe",
    "is_active": True
}

user = User(**user_data)

print(user)


# Example 2: Model with default values
class Product(BaseModel):
    id: int
    name: str
    price: float
    in_stock: bool = True  # default value


# Valid object (all fields provided)
product_one = Product(
    id=1,
    name="Laptop",
    price=999.99,
    in_stock=True
)
print(product_one)


# Valid object (default value used)
product_two = Product(
    id=2,
    name="Mouse",
    price=24.33
)
print(product_two)


# Invalid object (missing required fields)
try:
    product_three = Product(name="Keyboard")
    print(product_three)
except ValidationError as e:
    print("Product validation error:")
    print(e)
