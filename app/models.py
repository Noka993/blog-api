from sqlalchemy import Column, Integer, String
from sqlalchemy.sql.sqltypes import TIMESTAMP
from sqlalchemy.sql.expression import text
from sqlalchemy.dialects.postgresql import ARRAY

from .database import Base


class Post(Base):
    __tablename__ = "posts"

    id = Column(Integer, primary_key=True, nullable=False, unique=True)
    title = Column(String, nullable=False)
    content = Column(String, nullable=False)
    category = Column(String, nullable=False)
    tags = Column(ARRAY(String))
    createdAt = Column(
        TIMESTAMP(timezone=True), nullable=False, server_default=text("now()")
    )
    updatedAt = Column(
        TIMESTAMP(timezone=True), nullable=False, server_default=text("now()")
    )
