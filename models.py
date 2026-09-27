from pydantic import BaseModel, Field


class EmployeeInfo(BaseModel):
    name: str = Field(default="Not Available")
    company: str = Field(default="Not Available")
    role: str = Field(default="Not Available")
    location: str = Field(default="Not Available")
    joining_date: str = Field(default="Not Available")