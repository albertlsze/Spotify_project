'''Marshmallow schema definition OSRS items sqlalchemy model'''
from marshmallow_sqlalchemy import SQLAlchemyAutoSchema, auto_field

from ..models.yeardb import YearDB

class YearSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = YearDB
        load_instance = True
