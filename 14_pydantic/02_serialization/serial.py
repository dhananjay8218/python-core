# model_dump()      → converts Pydantic model to a Python dict (raw Python types)
# model_dump_json() → converts Pydantic model to a JSON string (encoders applied)

from pydantic import BaseModel, ConfigDict
from typing import List
from datetime import datetime


# Address model
class Address(BaseModel):
    street: str
    city: str
    zip_code: str


# User model with custom JSON serialization
class User(BaseModel):
    id: int
    name: str
    email: str
    is_active: bool = True
    created_at: datetime
    address: Address
    tags: List[str] = []

    model_config = ConfigDict(
        json_encoders={
            datetime: lambda v: v.strftime("%d-%m-%Y %H:%M:%S")
        }
    )


user = User(
    id=1,
    name="Hitesh",
    email="h@hitesh.ai",
    created_at=datetime(2024, 3, 15, 14, 30),
    address=Address(
        street="Something",
        city="Jaipur",
        zip_code="009988"
    ),
    is_active=False,
    tags=["premium", "subscriber"]
)

# 1️⃣ Pydantic model object
print(user)

print("=" * 30)

# 2️⃣ Python dictionary output
python_dict = user.model_dump()
print(python_dict)

print("=" * 30)

# 3️⃣ JSON string output (custom datetime format applied)
json_str = user.model_dump_json()
print(json_str)
