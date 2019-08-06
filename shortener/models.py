from flask import current_app as app

class Url(app.db.Model):
    id = Column(app.db.Integer, primary_key=True)
    url = Column(app.db.String(), nullable=False)
    alias = Column(app.db.String(app.config['HASH_SIZE']), unique=True, nullable=False)

    def __repr__(self):
        return '<Url %r, %r>' % self.alias, self.url
