
#cookie
SECRET_KEY='dasdafoafo;fasfsa'


#数据库配置
HOSTNAME = '127.0.0.1'
USERNAME = 'root'
PASSWORD = '123456'
DATABASE = ''          #数据库名
PORT = '3306'
DB_URI = 'mysql+pymysql://{}:{}@{}:{}/{}?charset=utf8'.format(USERNAME, PASSWORD, HOSTNAME, PORT, DATABASE)
SQLALCHEMY_DATABASE_URI = DB_URI

