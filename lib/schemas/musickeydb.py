'''Marshmallow schema definition OSRS items sqlalchemy model'''
from marshmallow_sqlalchemy import SQLAlchemyAutoSchema, auto_field

from ..models.musickeydb import MusicKeyDB

class MusicKeySchema(SQLAlchemyAutoSchema):
    '''Music Marshmallow schema class'''
    class Meta:
        model = MusicKeyDB
        load_instance = True
