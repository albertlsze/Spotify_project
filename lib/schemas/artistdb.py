'''Marshmallow schema definition OSRS items sqlalchemy model'''
from marshmallow_sqlalchemy import SQLAlchemyAutoSchema, auto_field

from ..models.artistdb import ArtistDB

class ArtistSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = ArtistDB
        load_instance = True
