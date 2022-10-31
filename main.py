
from fastapi import FastAPI, Depends
import model
import schemas
from schemas import Users
from database import engine, Session

app = FastAPI()

model.Base.metadata.create_all(bind=engine)


# Dependency
def get_db():
    db = Session()
    try:
        yield db
    finally:
        db.close()


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.post('/user')
async def create_user(user: schemas.Users, db: Session = Depends(get_db)):
    newuser = model.User(id=user.id, name=user.name, email=user.email)

    db.add(newuser)
    db.commit()
    db.refresh(newuser)

    return newuser


@app.get('/users/{id}')
async def get_user( db: Session = Depends(get_db)):
    user = db.query(model.User).all()    #filter(model.User.id== id)
    return user


@app.get('/users')
async def get_all_user(db: Session = Depends(get_db)):
    return db.query(model.User).all()

@app.post('/jusers')
async def create_user(jusers:schemas.jobapplication,db: Session = Depends(get_db)):
    jnewuser = model.jobapplication(id = jusers.id,name = jusers.name,under= jusers.under,salary= jusers.salary,branch= jusers.branch,team_no= jusers.team_no,project_name= jusers.project_name,doj= jusers.doj)
    db.add(jnewuser)
    db.commit()
    db.refresh(jnewuser)
    return jnewuser

@app.get('/jdata')
async def get_all_juser(db:Session=Depends(get_db)):
    return db.query(model.jobapplication).all()

#BOOKSTORE
@app.post('/book')
async def create_book(book:schemas.bookstore,db: Session = Depends(get_db)):
    Book = model.bookstore(id = book.id,b_name=book.b_name,u_name=book.u_name,a_name=book.a_name,date_p=book.date_p)
    db.add(Book)
    db.commit()
    db.refresh(Book)
    return Book

@app.get('/book_d')
async def get_all_book(db:Session=Depends(get_db)):
    return db.query(model.bookstore).all()

@app.get("/book/{id}")
async def get_book( db: Session = Depends(get_db)):
    book = db.query(model.bookstore).filter(model.bookstore.id == id).first()
    return book


#location
@app.post('/location')
async def create_location(loc:schemas.location,db: Session = Depends(get_db)):
    loc = model.location(id = loc.id, l_name=loc.l_name, geo_coordinate=loc.geo_coordinate, Owner_name=loc.Owner_name ,Con_number=loc.Con_number, email=loc.email)
    db.add(loc)
    db.commit()
    db.refresh(loc)
    return loc

@app.get('/location_all')
async def get_all_location(db:Session=Depends(get_db)):
    return db.query(model.location).all()

@app.get("/location/{id}")
async def get_location( db: Session = Depends(get_db)):
    loca = db.query(model.location).filter(model.location.id == id).first()
    return loca
