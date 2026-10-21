from sqlalchemy import create_engine
from sqlalchemy import Column, Integer, String, ForeignKey, Date
from sqlalchemy.orm import DeclarativeBase, Session, relationship

engine = create_engine("postgresql://admin:12345@217.71.129.139:6075/furniture")

class Base(DeclarativeBase): pass
class User(Base):
    __tablename__="users"
    id = Column(Integer, primary_key=True, index=True)
    name=Column(String,nullable=False)
    surname=Column(String,nullable=False)
    patr=Column(String)
    login=Column(String,nullable=False )
    password=Column(String,nullable=False)
    role_id=Column(Integer,ForeignKey("roles.id"),nullable=False)
    role=relationship("Role", lazy="joined")

class Role(Base):
    __tablename__="roles"
    id = Column(Integer, primary_key=True, index=True)
    title=Column(String,nullable=False)

class Address(Base):
    __tablename__="address"
    id = Column(Integer, primary_key=True, index=True)
    index=Column(Integer,nullable=False)
    city=Column(String,nullable=False)
    street=Column(String,nullable=False)
    number=Column(Integer,nullable=True)

class Status(Base):
    __tablename__="status"
    id = Column(Integer, primary_key=True, index=True)
    title=Column(String,nullable=False)

class Category(Base):
    __tablename__="category"
    id = Column(Integer, primary_key=True, index=True)
    title=Column(String,nullable=False)

class Manufactures(Base):
    __tablename__="manufactures"
    id = Column(Integer, primary_key=True, index=True)
    title=Column(String,nullable=False)

class Suppliers(Base):
    __tablename__="suppliers"
    id = Column(Integer, primary_key=True, index=True)
    title=Column(String,nullable=False)

class Zakaz(Base):
    __tablename__="zakaz"
    id = Column(Integer, primary_key=True, index=True)
    date_z=Column(Date,nullable=False )
    data_d=Column(Date,nullable=False )
    address_id=Column(Integer,ForeignKey("address.id"),nullable=False )
    user_id=Column(Integer,ForeignKey("users.id"),nullable=False )
    code=Column(Integer,nullable=False )
    status_id=Column(Integer,ForeignKey("status.id"),nullable=False )

class Tovar(Base):
    __tablename__="tovar"
    id = Column(Integer, primary_key=True, index=True)
    articul=Column(String, unique=True, nullable=False)
    name=Column(String,nullable=False)
    ed_izm=Column(String,nullable=False)
    price=Column(Integer,nullable=False )
    sale=Column(Integer,nullable=False )
    count=Column(Integer,nullable=False )
    description=Column(String,nullable=False)
    photo=Column(String)
    supplier_id=Column(Integer,ForeignKey("suppliers.id"),nullable=False )
    manufactures_id=Column(Integer,ForeignKey("manufactures.id"),nullable=False )
    category_id=Column(Integer,ForeignKey("category.id"),nullable=False )
    supplier = relationship("Suppliers", lazy="joined")
    manufacture = relationship("Manufactures", lazy="joined")
    category = relationship("Category", lazy="joined")

class Order_tovar(Base):
    __tablename__="order_tovar"
    zakaz_id = Column(Integer,ForeignKey("zakaz.id"),primary_key=True,nullable=False )
    tovar_id = Column(Integer,ForeignKey("tovar.id"),primary_key=True,nullable=False )
    count=Column(Integer,nullable=False )


def create():
    Base.metadata.create_all(bind=engine)
    print("Созданыь бд и таблицы")


