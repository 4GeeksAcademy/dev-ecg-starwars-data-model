from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import ForeignKey, String, Enum, Text, Integer
from sqlalchemy.orm import Mapped, mapped_column, relationship
from typing import List

db = SQLAlchemy()

class User(db.Model):
    __tablename__ = "user"
    id: Mapped[int] = mapped_column(primary_key=True)
    username: Mapped[str] = mapped_column(String(50), unique=True, nullable=False)
    email: Mapped[str] = mapped_column(String(150), unique=True, nullable=False)
    password: Mapped[str] = mapped_column(String(50), nullable=False)

    favorite_planets: Mapped[List["FavoritePlanet"]] = relationship(back_populates="user")
    favorite_characters: Mapped[List["FavoriteCharacter"]] = relationship(back_populates="user")

    def serialize(self):
        return {
            "id": self.id,
            "user_name": self.username,
            "email": self.email, 
        }
    
class Planet(db.Model):
    __tablename__ = "planet"
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(120), unique=True, nullable=False)
    climate: Mapped[str] = mapped_column(String(120), nullable=True)
    terrain: Mapped[str] = mapped_column(String(120), nullable=False)
    population: Mapped[int] = mapped_column(Integer, nullable=True)
    
    favorited_by_users: Mapped[List["FavoritePlanet"]] = relationship(back_populates="planet")

    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            "climate": self.climate,
            "terrain": self.terrain,
            "population": self.population, 
        }
    
class Character(db.Model):
    __tablename__ = "character"
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(120), unique=True, nullable=False)
    gender: Mapped[str] = mapped_column(String(50), nullable=False)
    birth_year: Mapped[str] = mapped_column(String(50), nullable=True)
    height: Mapped[int] = mapped_column(Integer, nullable=True)
    
    favorited_by_users: Mapped[List["FavoriteCharacter"]] = relationship(back_populates="character")

    def serialize(self):
        return {
            "id": self.id, 
            "name": self.name,
            "gender": self.gender,
            "birth_year": self.birth_year,
            "height": self.height,
        }
    
class FavoritePlanet(db.Model):
    __tablename__ = "favorite_planet"
    user_id: Mapped[int] = mapped_column(ForeignKey("user.id"), primary_key=True)
    planet_id: Mapped[int] = mapped_column(ForeignKey("planet.id"), primary_key=True)
    
    user: Mapped["User"] = relationship(back_populates="favorite_planets")
    planet: Mapped["Planet"] = relationship(back_populates="favorited_by_users")

    def serialize(self):
        return {
            "user_id": self.user_id,
            "planet_id": self.planet_id,
        }
    
class FavoriteCharacter(db.Model):
    __tablename__ = "favorite_character"
    user_id: Mapped[int] = mapped_column(ForeignKey("user.id"), primary_key=True)
    character_id: Mapped[int] = mapped_column(ForeignKey("character.id"), primary_key=True)

    user: Mapped["User"] = relationship(back_populates="favorite_characters")
    character: Mapped["Character"] = relationship(back_populates="favorited_by_users")

    def serialize(self):
        return {
            "user_id": self.user_id, 
            "character_id": self.character_id,
        }


