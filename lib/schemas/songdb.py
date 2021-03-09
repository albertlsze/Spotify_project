'''Marshmallow schema definition OSRS items sqlalchemy model'''
from marshmallow_sqlalchemy import SQLAlchemyAutoSchema, auto_field

from ..models.songdb import SongDB

class SongSchema(SQLAlchemyAutoSchema):
    '''Song Marshmallow schema class'''
    class Meta:
        model = SongDB
        load_instance = True
