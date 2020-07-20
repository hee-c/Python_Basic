# 테이블 수정 및 삭제

import sqlite3

# DB파일 조회(없으면 새로 생성)
conn = sqlite3.connect('C:/Users/K/OneDrive - 경희대학교/바탕 화면/2020/개발/파이썬 기초/resource/database.db', isolation_level=None)

# Cusor 연결
c = conn.cursor()

# 데이터 수정1
# c.execute("UPDATE users SET username = ? WHERE id = ?", ('niceman', 2))

# 데이터 수정2
# c.execute("UPDATE users SET username = :name WHERE id = :id", {"name": 'goodman', "id": 5})

# 데이터 수정3
# c.execute("UPDATE users SET username = '%s' WHERE id = '%s'" %('badboy', 3))

# 중간 데이터 확인
for user in c.execute("SELECT * FROM users"):
    print(user)


# Row Delete1
c.execute("DELETE FROM users WHERE id = ?", (2,))

# Row Delete2
c.execute("DELETE FROM users WHERE id = :id", {"id": 5 })

# Row Delete3
c.execute("DELETE FROM users WHERE id = '%s'" % 4)

# 중간 데이터 확인
for user in c.execute("SELECT * FROM users"):
    print(user)

# 테이블 전체 데이터 삭제
print("users db deleted : ", conn.execute("DELETE FROM users").rowcount, " rows")
