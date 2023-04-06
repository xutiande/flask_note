# 模型文件
from exts import db
from datetime import datetime

# 用户
class UserModel(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)  # 主键，自增
    username = db.Column(db.String(255), nullable=False)
    password = db.Column(db.String(255), nullable=False)
    email = db.Column(db.String(255), nullable=False, unique=True)  # 唯一的（不能出现相同的）


#内容
class ArticlesModels(db.Model):
    __tablename__ = 'articles'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)  # 主键，自增
    title = db.Column(db.String(255), nullable=False)
    content = db.Column(db.Text, nullable=False)
    author = db.Column(db.String(255), nullable=False)
    create_date = db.Column(db.DateTime, default=datetime.now)  # 用户当前时间
