import os
basedir = os.path.abspath(os.path.dirname(__file__))


class Config:
    # Secret key for session management and CRSF protection
    SECRET_KEY = os.environ.get('SECRET')

    # Database configuration, we are using SQLite for simplicity
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'db.sqlite')
    SQLACLCHEMY_TRACK_MODIFICATIONS = False

    # Other configurations will be included here as needed.
