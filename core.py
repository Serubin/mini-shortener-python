from flask import Flask
from config import BaseConfig

app = Flask(__name__)

app.config.from_object(BaseConfig)

from routes import shortener_blueprint, redirect_blueprint
app.register_blueprint(shortener_blueprint)
app.register_blueprint(redirect_blueprint)

if __name__ == '__main__':
    app.run()
