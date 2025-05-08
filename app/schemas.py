from pydantic import BaseModel
from datetime import datetime


class PostCreate(BaseModel):
    title: str
    content: str
    category: str
    tags: list[str]

class PostOut(PostCreate):
    id: int
    createdAt: datetime
    updatedAt: datetime

    class Config:
        orm_mode = True

