'''Marshmallow schema definition OSRS items sqlalchemy model'''
from marshmallow_sqlalchemy import SQLAlchemyAutoSchema, auto_field

from ..models.genredb import GenreDB

class GenreSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = GenreDB
        load_instance = True
