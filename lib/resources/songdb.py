'''Resource for REST routes for OSRS Items'''
from flask import abort
from flask.views import MethodView
from marshmallow import fields
from sqlalchemy import or_
from sqlalchemy.orm.exc import NoResultFound
from pprint import pprint

from lib import SQL_cnx, SONG_SCHEMA, MANY_SONG_SCHEMA
from lib.models.songdb import SongDB

class AllSongItems(MethodView):
    '''Class for REST methods to interact with multiple OSRS Item in DB'''

    def get(self, order_by = SongDB.song_name, **_):
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
        with SQL_cnx.session_scope() as sess:
            multi_songs = sess.query(SongDB.song_id,SongDB.song_name,SongDB.artists_id,SongDB.release_date).order_by(order_by).all()
            dumped_item = MANY_SONG_SCHEMA.dump(multi_songs)

            if not dumped_item:
                return abort(404)

        return dumped_item


    def get_distinct_item_ids(self, **_):
        with SQL_cnx.session_scope() as sess:
            item_ids = sess.query(SongDB.song_id).distinct()
            dumped_item = MANY_SONG_SCHEMA.dump(item_ids)

            if not dumped_item:
                return abort(404)

            distinct_ids = []
            for i in dumped_item:
                distinct_ids.append(i['song_id'])
        return distinct_ids


if __name__ == '__main__':
    all_songs = AllSongItems()
    distinct_ids = all_songs.get_distinct_item_ids()
    pprint(type(distinct_ids))
    pprint(len(distinct_ids))
    pprint(len(set(distinct_ids)))

    #pprint(all_songs.get())
