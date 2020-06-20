# 代码清单13-1 将数据导入数据库（importdata.py）
import sqlite3


def convert(value):
    if value.startswith('~'):
        return value.strip('~')
    if not value:
        value = '0'
        return float(value)


conn = sqlite3.connect('food.db')
curs = conn.cursor(

curs.execute(''' 
CREATE TABLE food (

id TEXT PRIMARY KEY, 
desc TEXT, 
water FLOAT, 
kcal FLOAT, 
protein FLOAT, 
fat FLOAT, 
ash FLOAT, 
carbs FLOAT, 
fiber FLOAT, 
sugar FLOAT
) 
''')
query = 'INSERT INTO food VALUES (?,?,?,?,?,?,?,?,?,?)'
field_count = 10
for line in open('FOOD_DES.txt'):
    fields = line.split('^')
    vals = [convert(f) for f in fields[:field_count]]
    curs.execute(query, vals)

conn.commit()
conn.close()