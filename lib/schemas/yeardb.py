'''Marshmallow schema definition OSRS items sqlalchemy model'''
from marshmallow_sqlalchemy import SQLAlchemyAutoSchema, auto_field

from ..models.yeardb import YearDB

class YearSchema(SQLAlchemyAutoSchema):
    '''Year Marshmallow schema class'''
    class Meta:
        model = YearDB
        load_instance = True
