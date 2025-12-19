from typing import Optional, List, Union
from pydantic import BaseModel


# -------------------- BASIC NESTED MODELS --------------------

class Address(BaseModel):
    street: str
    city: str
    postal_code: str


class Company(BaseModel):
    name: str
    address: Optional[Address] = None


class Employee(BaseModel):
    name: str
    company: Optional[Company] = None


# -------------------- UNION (POLYMORPHIC) MODELS --------------------

class TextContent(BaseModel):
    type: str = "text"
    content: str


class ImageContent(BaseModel):
    type: str = "image"
    url: str
    alt_text: str


class Article(BaseModel):
    title: str
    # A section can be either text or image
    sections: List[Union[TextContent, ImageContent]]


# -------------------- DEEP NESTED HIERARCHY --------------------

class Country(BaseModel):
    name: str
    code: str


class State(BaseModel):
    name: str
    country: Country


class City(BaseModel):
    name: str
    state: State


class Location(BaseModel):
    street: str
    city: City
    postal_code: str


class Organization(BaseModel):
    name: str
    head_quarter: Location
    # Use default_factory to avoid shared mutable defaults
    branches: List[Location] = []
