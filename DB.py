import sqlite3
import datetime

now = datetime.datetime.now()
print('now : ', now)

nowDatetime = now.strftime('%Y-%m-%d %H:%M:%S')
print('nowDatetime : ', nowDatetime)

conn = sqlite3.connect('C:/Users/K/OneDrive - 경희대학교/바탕 화면/2020/개발/파이썬 기초/resource/database.db', isolation_level=None)

c = conn.cursor()
print(type(c))

c.execute("CREATE TABLE IF NOT EXISTS users(id INTEGER PRIMARY KEY, username text, email text, phone text, website text, regdate text)")

# 데이터 삽입
# c.execute("INSERT INTO users VALUES(1, 'Kim', 'Kim@naver.com', '010-0000-0000', 'Kim.com', ?)", (nowDatetime,))
# c.execute("INSERT INTO users(id, username, email, phone, website, regdate) VALUES (?,?,?,?,?,?)", (2,'Park','Park@daum.net','010-1111-1111','Park.com',nowDatetime))


# Many 삽입(튜플, 리스트)
userList = (
    (3, 'Lee', 'Lee@naver.com', '010-2222-2222', 'Lee.com', nowDatetime),
    (4, 'Cho', 'Cho@naver.com', '010-3333-3333', 'Cho.com', nowDatetime),
    (5, 'Yoo', 'Yoo@naver.com', '010-4444-4444', 'Yoo.com', nowDatetime)
)

#c.executemany("INSERT INTO users(id, username, email, phone, website, regdate) VALUES (?,?,?,?,?,?)", userList)

# 테이블 삭제
#conn.execute("DELETE FROM users")
#print("users db deleted : ", conn.execute("DELETE FROM users").rowcount)

# conn.close()

