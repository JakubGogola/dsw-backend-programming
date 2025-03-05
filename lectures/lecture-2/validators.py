from pydantic import BaseModel, validator, root_validator, EmailStr, field_validator
from datetime import datetime

class Event(BaseModel):
    name: str
    date: datetime

    @validator('date')
    def validate_date(cls, v):
        if v < datetime.now():
            raise ValueError('Date must be in the future!')
        return v

class User(BaseModel):
    name: str
    age: int

    @validator('name')
    def name_must_be_capitalized(cls, v):
        if not v.istitle():
            raise ValueError('Name must be capitalized')
        return v

class BaseUser(BaseModel):
    name: str
    email: EmailStr

class AdvancedUser(BaseUser):
    age: int
    is_active: bool = True

    @validator('age')
    def age_must_be_valid(cls, v):
        if v < 18:
            raise ValueError('Age must be greater than or equal to 18')
        return v

class Purchase(BaseModel):
    product_price: float
    discount: float

    @root_validator
    def check_discount(cls, values):
        product_price = values.get('product_price')
        discount = values.get('discount')

        if discount > product_price:
            raise ValueError('Discount cannot be greater than the product price')

        return values

class User(BaseModel):
    name: str
    age: int
    email: EmailStr

    # Walidacja pola 'age' za pomocą @field_validator
    @field_validator('age')
    def validate_age(cls, v):
        if v < 18:
            raise ValueError('Age must be greater than or equal to 18')
        return v

    # Walidacja pola 'email' za pomocą @field_validator
    @field_validator('email')
    def validate_email(cls, v):
        blocked_domains = ["blocked.com", "spam.com"]
        domain = v.split('@')[-1]
        if domain in blocked_domains:
            raise ValueError(f"Email domain '{domain}' is blocked")
        return v

# Przykład użycia
try:
    user = User(name="John Doe", age=17, email="john@blocked.com")
except ValueError as e:
    print(f"Error: {e}")

# Prawidłowy przypadek
user = User(name="Jane Doe", age=25, email="jane@valid.com")
print(user)
