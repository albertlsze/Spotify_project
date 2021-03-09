'''Resource for REST routes for OSRS Items'''
from flask import abort
from flask.views import MethodView
from marshmallow import fields
from sqlalchemy import or_
from sqlalchemy.orm.exc import NoResultFound

from .. import SQL_cnx, SONG_SCHEMA, MANY_SONG_SCHEMA
from ..models.songdb import SongDB

class AllSongItems(MethodView):
    '''Class for REST methods to interact with multiple OSRS Item in DB'''

    def get(self, **_):
        '''Get all songs currently in the database.

        :param _: None
        :return: responses:
                    200:
                        description: Return items in the database.
                        content:
                            application/json:
                                schema: GetManyResponseSchema
                    400:
                        description: API exception occurred during request.
                    500:
                        description: unexpected exception occurred during request.
        '''
        with SQL_cnx.session() as sess:
            multi_songs = sess.query(SongDB.song_id,SongDB.song_name).all()
            dumped_item = MANY_SONG_SCHEMA.dump(multi_songs)

            if not dumped_item:
                return abort(404)

        return {'data': dumped_item}
