from pydantic import BaseModel


# Nested model representing an address
class Address(BaseModel):
    street: str
    city: str
    postal_code: str


# User model containing a nested Address model
class User(BaseModel):
    id: int
    name: str
    address: Address


# Create Address instance directly
address = Address(
    street="123 Something",
    city="Jaipur",
    postal_code="100001"
)

# Create User using Address object
user_obj = User(
    id=1,
    name="Hitesh",
    address=address
)

print(user_obj)


# Create User using nested dictionary (automatic parsing)
user_data = {
    "id": 2,
    "name": "Hitesh",
    "address": {
        "street": "321 Something",
        "city": "Paris",
        "postal_code": "20002"
    }
}

user_dict = User(**user_data)
print(user_dict)
