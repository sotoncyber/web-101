import sqlite3
import flask
import challenge

IntegrityError = sqlite3.IntegrityError

# USAGE
# >>> from tracker.db import init_db
# >>> init_db()
def init_db():
    with challenge.app.app_context():
        db = get_db()
        with challenge.app.open_resource('../schema.sql', mode='r') as f:
            db.cursor().executescript(f.read())
        db.commit()

def get_db():
    db = getattr(flask.g, '_database', None)
    if db is None:
        db = flask.g._database = sqlite3.connect(challenge.app.config['SQLITE_URI'])
    db.row_factory = sqlite3.Row
    return db

def query_db(query, args=(), one=False):
    cur = get_db().execute(query, args)
    rv = cur.fetchall()
    cur.close()
    get_db().commit()
    return (rv[0] if rv else None) if one else rv

@challenge.app.teardown_appcontext
def close_connection(exception):
    db = getattr(flask.g, '_database', None)
    if db is not None:
        db.close()
