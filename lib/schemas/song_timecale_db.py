'''Marshmallow schema definition OSRS items sqlalchemy model'''
from marshmallow_sqlalchemy import SQLAlchemyAutoSchema, auto_field

from ..models.song_timescale_db import SongTimeDB

class SongTimeSchema(SQLAlchemyAutoSchema):
    '''Song Marshmallow schema class'''
    class Meta:
        model = SongTimeDB
        load_instance = True
        include_fk = True