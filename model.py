from database import Base
from sqlalchemy import Column, String, Integer


class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, autoincrement=True, primary_key=True)
    name = Column(String(150))
    email = Column(String(255))


# jobapplication
class jobapplication(Base):
    __tablename__ = "jusers"
    id= Column(Integer, autoincrement=True, primary_key=True)
    name=Column(String(150))
    under= Column(String(150))
    salary= Column(Integer)
    branch= Column(String(150))
    team_no= Column(Integer)
    project_name= Column(String(150))
    doj= Column(String(150))

class bookstore(Base):
    __tablename__ = "book"
    id= Column(Integer, autoincrement=True, primary_key=True)
    b_name=Column(String(150))
    u_name=Column(String(150))
    a_name=Column(String(150))
    date_p=Column(Integer)

class location(Base):
    __tablename__="loc"
    id=Column(Integer,autoincrement=True,primary_key=True)
    l_name = Column(String(150))
    geo_coordinate= Column(String(150))
    Owner_name=Column(String(150))
    Con_number=Column(Integer)
    email=Column(String(150))
