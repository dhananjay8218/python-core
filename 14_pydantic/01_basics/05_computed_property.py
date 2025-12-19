from pydantic import BaseModel, Field, computed_field


# Model with a derived (computed) field
class Product(BaseModel):
    price: float
    quantity: int

    # Computed field is calculated dynamically, not stored
    @computed_field
    @property
    def total_price(self) -> float:
        return self.price * self.quantity


# Booking model with validation and computed total
class Booking(BaseModel):
    user_id: int
    room_id: int
    # Nights must be at least 1
    nights: int = Field(..., ge=1)
    rate_per_night: float

    # Total amount derived from nights and rate
    @computed_field
    @property
    def total_amount(self) -> float:
        return self.nights * self.rate_per_night


# Example usage
booking = Booking(
    user_id=123,
    room_id=456,
    nights=3,
    rate_per_night=100.0
)

# Access computed field like a normal attribute
print(booking.total_amount)

# Computed field is included in serialized output
print(booking.model_dump())
