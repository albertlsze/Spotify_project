'''Resource for REST routes for OSRS Items'''
from flask import abort
from flask.views import MethodView
from lib.connection.postgres import PostgresConnection

from lib.models.song_timescale_db import SongTimeDB
from lib import SQL_cnx, SONG_TIME_SCHEMA, MANY_SONG_TIME_SCHEMA


class MultiTimeTracks(MethodView):
    '''Class for REST methods to interact with multiple time tracks in DB'''

    def get_distinct_items_ids(self, **_):

        with SQL_cnx.session_scope() as sess:
            item_ids = sess.query(SongTimeDB.song_id).distinct()
            dumped_item = MANY_SONG_TIME_SCHEMA.dump(item_ids)

            #if not dumped_item:
            #    return abort(404)

            distinct_ids = []
            for i in dumped_item:
                distinct_ids.append(i['song_id'])
        return set(distinct_ids)