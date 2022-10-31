from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import  declarative_base
from sqlalchemy.orm import  sessionmaker

# sql_address= 'mysql+pymysql://root:ankit700@localhost:3306/mydb'
# sql_address= 'mysql+pymysql://root:ankit700@localhost:3306/japplication'
# sql_address= 'mysql+pymysql://root:ankit700@localhost:3306/bookstore'
sql_address= 'mysql+pymysql://root:ankit700@localhost:3306/location'



engine = create_engine(sql_address)

Session = sessionmaker(bind=engine)


Base = declarative_base()
