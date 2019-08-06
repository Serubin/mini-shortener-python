from core import db

class Url(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    url = db.Column(db.String(), nullable=False)
    alias = db.Column(db.String(5), unique=True, nullable=False) # TODO this shold be sized by config

    def __repr__(self):
        return '<Url %r, %r>' % self.alias, self.url
