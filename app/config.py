class Config:
    MYSQL_HOST = 'localhost'
    MYSQL_USER = 'root'
    MYSQL_PASSWORD = ''
    MYSQL_DB = 'flaskCrud'


class Config:
    SQLALCHEMY_DATABASE_URI = 'mysql+mysqlconnector://root:''@localhost/flaskCrud'
    SQLALCHEMY_TRACK_MODIFICATIONS = False