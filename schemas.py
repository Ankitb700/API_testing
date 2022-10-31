from pydantic import BaseModel


class Users(BaseModel):
    id: int
    name: str
    email: str

    class Config:
        orm_mode = True

class jobapplication(BaseModel):
        id: int
        name: str
        under: str
        salary: int
        branch: str
        team_no: int
        project_name: str
        doj: str

class bookstore(BaseModel):
    id: int
    b_name: str
    u_name: str
    a_name: str
    date_p: int


class location(BaseModel):
    __tablename__="loc"
    id :int
    l_name :str
    geo_coordinate: str
    Owner_name: str
    Con_number:int
    email:str


    class Config:
        orm_mode = True
