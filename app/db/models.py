from sqlalchemy import Column, Integer, BigInteger
from app.db.base import Base

class Users(Base):
    '''
    Класс представления пользователя
    на основе базового
    и указание связанной таблицы
    '''
    __tablename__ = "users"
    user_id = Column(BigInteger, primary_key=True, unique=True, autoincrement=False)
