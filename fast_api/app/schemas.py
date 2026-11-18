from enum import Enum
from pydantic import BaseModel, Field
from typing import Optional

class issues_status(str, Enum):
    open = "open"
    in_progress = "in_progress"
    closed = "closed"

class issues_priority(str, Enum):
    low = "low"
    medium = "medium"
    high = "high"

class issues_create(BaseModel):
    title: str = Field(min_length=3, max_length=100)
    description: str = Field(min_length=5, max_length=2000)
    priority: issues_priority = issues_priority.medium

class issues_update(BaseModel):
    title: Optional[str] = Field(default=None, max_length=100)
    description: Optional[str] = Field(
        default=None, min_length=5, max_length=2000)
    priority: Optional[issues_priority] = None
    status: Optional[issues_status] = None

class issues_out(BaseModel):
    id: str
    title: str
    description: str
    priority: issues_priority
    status: issues_status