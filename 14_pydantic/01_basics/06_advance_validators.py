from pydantic import BaseModel, field_validator, model_validator
from datetime import datetime


# Validate and normalize person names
class Person(BaseModel):
    first_name: str
    last_name: str

    # Ensure names start with a capital letter
    @field_validator("first_name", "last_name")
    @classmethod
    def validate_name_capitalization(cls, value: str) -> str:
        if not value.istitle():
            raise ValueError("Names must be capitalized")
        return value


# Normalize user email input
class User(BaseModel):
    email: str

    # Convert email to lowercase and remove extra spaces
    @field_validator("email")
    @classmethod
    def normalize_email(cls, value: str) -> str:
        return value.strip().lower()


# Parse price input before validation
class Product(BaseModel):
    price: str  # stored as float internally

    # Convert "$4.44" → 4.44
    @field_validator("price", mode="before")
    @classmethod
    def parse_price(cls, value):
        if isinstance(value, str):
            return float(value.replace("$", ""))
        return value


# Validate a date range
class DateRange(BaseModel):
    start_date: datetime
    end_date: datetime

    # Ensure end_date comes after start_date
    @model_validator(mode="after")
    def validate_date_order(self):
        if self.start_date >= self.end_date:
            raise ValueError("end_date must be after start_date")
        return self
