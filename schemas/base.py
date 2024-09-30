from pydantic import BaseModel, validator
from email_validator import validate_email as validate_e





class UserBase(BaseModel):
    email: str

@validator("email")
def validate_email(cls, v):
    try:
        validate_e(v)
        return v
    except Exception as e:
        raise ValueError("Email not valid")


class BaseComplaint(BaseModel):
    title: str
    description: str
    photo_url: str
    amount: float
