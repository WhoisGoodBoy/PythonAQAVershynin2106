from sqlalchemy.orm import declarative_base
from sqlalchemy import VARCHAR, Integer, Column

Base = declarative_base()


class Users(Base):
    __tablename__ = 'tablewithusers'
    id = Column(VARCHAR(8), primary_key=True)
    first_name = Column(VARCHAR(25))
    last_name = Column(VARCHAR(25))
    age = Integer
    email = Column(VARCHAR(25))
