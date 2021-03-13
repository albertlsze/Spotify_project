from flask import Flask, render_template,url_for, request, redirect, abort
from flask_sqlalchemy import SQLAlchemy
from config.database_config import sql_config
from lib.resources.songdb import AllSongItems
from lib.models.songdb import SongDB
from lib import SQL_cnx, SONG_SCHEMA, MANY_SONG_SCHEMA
from lib.utils.Frontend.bokeh_hist import bokeh_hist
from bokeh.embed import components
import pandas as pd
from bokeh.io import show


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = f"mysql://{sql_config['username']}:{sql_config['password']}@{sql_config['host']}/{sql_config['database']}"
db = SQLAlchemy(app)


class song_query(db.Model, SongDB):
    def __repr__(self):
        return f'database: {self.name}'

@app.route('/', methods = ['GET'])
def index():
    order_by = song_query.song_name
    with SQL_cnx.session_scope() as sess:
        multi_songs = sess.query(SongDB.song_id, SongDB.song_name, SongDB.artists_id, SongDB.release_date).order_by(
            order_by).limit(150).all()
        dumped_item = MANY_SONG_SCHEMA.dump(multi_songs)

        if not dumped_item:
            return abort(404)
    chart_script, chart_div = song_feature_chart()
    return render_template('index.html',song_titles = multi_songs,div_song_feature_chart=chart_div,script_song_feature_chart=chart_script)

def song_feature_chart():
    # Bokeh graph
    song_data = 'D:\\Documents\\Github\\albertlsze\\Spotify_project\\scripts\\Prepopulated_data\\song_data.csv'
    song_data = pd.read_csv(song_data)
    column = ["acousticness", "danceability", "duration_ms", "energy", "instrumentalness", "key", "liveness",
              "loudness", "popularity", "speechiness", "tempo", "valence"]

    graph = bokeh_hist("Song Features")
    #chart = graph.add_tabs(song_data, column)
    chart = graph.hist_hover(song_data, 'popularity', bins = 30, show_plot = False)
    return components(chart)

if __name__ == "__main__":
    app.run(debug=True)