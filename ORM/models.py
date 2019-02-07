from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

#테이블 만들기
class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    # 비어있을 수 없다 false의 의미
    email = db.Column(db.String(120), unique=True, nullable=False)
    
    def __repr__(self):
        return f"<User '{self.username}'>"
        
        
