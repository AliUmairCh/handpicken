from flask import Flask
from flask_bootstrap import Bootstrap
from flask import render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
bootstrap = Bootstrap(app)

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:Salam316%21@localhost/postgres'
db = SQLAlchemy(app)

class songs_list(db.Model):
    track_id = db.Column(db.VARCHAR(60), primary_key=True)
    artist = db.Column(db.VARCHAR(60))
    album = db.Column(db.VARCHAR(60))
    title = db.Column(db.VARCHAR(60))
    lang = db.Column(db.VARCHAR(15))
    genre = db.Column(db.VARCHAR(30))
    
@app.route('/')
def index():
    songs = songs_list.query.all()  # Query the database to get all songs
    return render_template('index.html', songs=songs)

@app.route('/song')
def about():
    songs = songs_list.query.all()
    return render_template('song.html', songs=songs)


if __name__ == '__main__':
    app.run(debug=True)