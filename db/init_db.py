
import sqlite3
import json

# 创建数据库
conn = sqlite3.connect("db/zodiac.db")
cur = conn.cursor()

# 创建表
cur.execute("""
CREATE TABLE IF NOT EXISTS zodiac (
    name TEXT,
    start_date TEXT,
    end_date TEXT,
    male_personality TEXT,
    female_personality TEXT,
    match TEXT,
    match_reason TEXT
)
""")

# 加载 JSON 数据
with open("data/zodiac_data.json", "r") as f:
    xingzuo_list = json.load(f)

# 插入数据
for x in xingzuo_list:
    cur.execute("INSERT INTO zodiac VALUES (?, ?, ?, ?, ?, ?, ?)", (
        x["name"], x["start_date"], x["end_date"],
        x["male_personality"], x["female_personality"],
        x["match"], x["match_reason"]
    ))

conn.commit()
conn.close()
print("数据库初始化完成")
