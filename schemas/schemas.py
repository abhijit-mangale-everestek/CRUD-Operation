from typing import List, Optional

from pydantic import BaseModel, Field


class UserBase(BaseModel):
    first_name: str = Field(..., max_length=10, title='Enter valid First Name',
                            description='firstname must be greater than 3 and less than 10.')
    last_name: str
    gender: str


class User(UserBase):
    id: int

    class Config:
        orm_mode = True
