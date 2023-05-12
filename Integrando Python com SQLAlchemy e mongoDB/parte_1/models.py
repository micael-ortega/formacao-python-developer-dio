from sqlalchemy.orm import declarative_base
from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine


url = 'sqlite:///:memory'
engine = create_engine(url)
Base = declarative_base()


class User(Base):
    __tablename__ = 'user'

    id = Column(Integer, primary_key=True)
    name = Column(String(20), nullable=False)
    surname = Column(String(64), nullable=False)
    cpf = Column(String(11), nullable=False, unique=True)

    user_account = relationship('UserAccount', back_populates='user')


class UserAccount(Base):
    __tablename__ = 'user_account'
    id = Column(Integer, primary_key=True)
    account_number = Column(Integer, unique=True, nullable=False)
    account_type = Column(String(32), nullable=False)
    user_id = Column(Integer, ForeignKey('user.id'))
    agency_id = Column(Integer, ForeignKey('agency.id'))

    user = relationship('User', backref='user_accounts')
    agency = relationship('Agency', back_populates='agency_account')


class Agency(Base):
    __tablename__ = 'agency'
    id = Column(Integer, primary_key=True)
    agency_number = Column(Integer, nullable=False, unique=True)
    agency_city = Column(String(32), nullable=False)
    agency_state = Column(String(3), nullable=False)
    agency_country = Column(String(4), nullable=False)

    agency_account = relationship('UserAccount', back_populates='agency')


Base.metadata.create_all(bind=engine)


