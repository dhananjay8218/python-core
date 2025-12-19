from typing import Optional
from pydantic import BaseModel, Field


# Employee data model with field-level validation
class Employee(BaseModel):
    id: int
    name: str = Field(
        ...,
        min_length=3,
        max_length=50,
        description="Employee full name",
        examples=["John Doe"]
    )
    # Optional field with default value
    department: Optional[str] = Field(
        default="General",
        description="Department name"
    )
    # Salary must be >= 10,000
    salary: float = Field(
        ...,
        ge=10_000,
        description="Monthly salary amount"
    )


# User data model with regex and range validation
class User(BaseModel):
    # Email format validation
    email: str = Field(
        ...,
        regex=r"^[\w\.-]+@[\w\.-]+\.\w+$",
        description="Valid email address"
    )
    # Indian mobile number validation (10 digits)
    phone: str = Field(
        ...,
        regex=r"^[6-9]\d{9}$",
        description="10-digit mobile number"
    )
    # Age must be within realistic range
    age: int = Field(
        ...,
        ge=0,
        le=150,
        description="Age in years"
    )
    # Discount percentage between 0 and 100
    discount: float = Field(
        ...,
        ge=0,
        le=100,
        description="Discount percentage"
    )
