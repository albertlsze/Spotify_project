'''Marshmallow schema definition OSRS items sqlalchemy model'''
from marshmallow_sqlalchemy import SQLAlchemyAutoSchema, auto_field

from ..models.songdb import SongDB

class SongSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = SongDB
        load_instance = True
