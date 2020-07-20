import random
import time
import sqlite3
import winsound
import datetime

conn = sqlite3.connect('C:/Users/K/OneDrive - 경희대학교/바탕 화면/2020/개발/파이썬 기초/resource/records.db', isolation_level=None)
cursor = conn.cursor()
cursor.execute("CREATE TABLE IF NOT EXISTS records(id INTEGER PRIMARY KEY AUTOINCREMENT, cor_cnt INTEGER, record text, regdate text)")

words = []  # 영어 단어 리스트
n = 1  # 게임 시도 횟수
cor_cnt = 0  # 정답 개수

with open('./resource/word.txt', 'r') as f:
    for c in f:
        words.append(c.strip())
# print(words)  # 단어 리스트 확인


input("Ready? Press Enter Key!")

start = time.time()

while n <= 5:
    random.shuffle(words)
    q = random.choice(words)

    print("*Question # {}".format(n))
    print(q)

    x = input()

    if str(q).strip() == str(x).strip():
        print("Pass!")
        winsound.PlaySound('./sound/good.wav', winsound.SND_FILENAME)
        cor_cnt += 1
    else:
        winsound.PlaySound('./sound/bad.wav', winsound.SND_FILENAME)
        print("Wrong!")

    print()

    n += 1

end = time.time()
et = end - start
et = format(et, ".3f")

if cor_cnt >= 3:
    print("합격!")
else:
    print("불합격!")

# 기록 DB 삽입
cursor.execute("INSERT INTO records('cor_cnt', 'record', 'regdate') VALUES (?,?,?)", (cor_cnt, et, datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')))

print("게임 시간 : ", et, "초", "정답 개수 : {}".format(cor_cnt))

if __name__ == '__main__':
    pass




