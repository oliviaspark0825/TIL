-- create
INSERT INTO users(username, email)
VALUES('suhyun', 'ddd@gmail.com');

user=User(username='suhyun'.
        email = 'ddd@gmail.com')
 



-- read
SELECT * FROM users;
users = User.query.all()

SELECT * FROM users WHERE username='suhyun'
users = User.query.filter_by(username='suhyun').all()

SELECT * FROM users WHERE username='suhyun' LIMIT 1;
users = User.query.filter_by(username='suhyun').first()


miss = User.query.filter_by(username='ssafy').first()
-- 하나만 찍어서 조회했을 때 값이 없으면 nonetype 나타남

-- Get One by id
-- primary key 만 GET 으로 가져올 수 있음
SELECT * FROM users WHERE id=1;
users = User.query.get(1)

-- LIKE
users = User.query.filter(User.email.like('%exam%')).all()
-- LIMIT, OFFSET // 두개 뛰고 하나 -> 3번째꺼
users = User.query.limit(1).offset(2).all()

--UPDATE
user = User.query.get(1)
user.username = 'ssafy'
db.session.commit()
user.username

-- DELETE
user = User.query.get(1)
db.session.delete(user)
db.session.commit()