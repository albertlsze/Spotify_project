from flask import Flask, render_template,url_for, request, redirect
from flask_sqlalchemy import SQLAlchemy
from config.database_config import sql_config


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = f"mysql://{sql_config['username']}:{sql_config['password']}@{sql_config['host']}/{sql_config['database']}"
db = SQLAlchemy(app)

@app.route('/')
def index():
    return render_template('index.html')

if __name__ == "__main__":
    app.run(debug=True)