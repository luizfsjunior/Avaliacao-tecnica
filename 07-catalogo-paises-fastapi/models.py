from sqlalchemy import Column, Integer, String, ForeignKey, UniqueConstraint
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base()

class Country(Base):
    __tablename__ = "countries"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, nullable=False)
    population = Column(Integer, nullable=False)
    continent = Column(String, nullable=False)
    votes_like = Column(Integer, default=0)
    votes_dislike = Column(Integer, default=0)

class Vote(Base):
    __tablename__ = "votes"
    id = Column(Integer, primary_key=True, index=True)
    country_id = Column(Integer, ForeignKey("countries.id"), nullable=False)
    vote = Column(String, nullable=False)  # 'like' ou 'dislike'
    country = relationship("Country")
    __table_args__ = (UniqueConstraint('country_id', 'id', name='_country_vote_uc'),)
