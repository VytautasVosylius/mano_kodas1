from sqlalchemy import create_engine, Column, Integer, String, DateTime
from sqlalchemy.orm import DeclarativeBase, sessionmaker
 
engine = create_engine("mysql://root:Test123+@localhost:3306/test")
 
class Base(DeclarativeBase):
    pass
 
class Device(Base):
    __tablename__ = "device"
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(50), nullable=False)
    created_at = Column(DateTime)
 
class Shop(Base):
    __tablename__ = "shop"
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(50), nullable=False)
 
 
Base.metadata.create_all(engine)
 
Session = sessionmaker(bind = engine)
with Session() as session:
    new_shop = Shop(name = "TopoCentras")
    session.add(new_shop)
    session.commit()