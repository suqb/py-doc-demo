# pip install pymysql
import json

from pymysql import Connection

conn = Connection(
    host='120.77.246.22',
    port=3306,
    user='root',
    password='wmj18476723899',
)

conn.select_db("sharding-jdbc")

cursor = conn.cursor()

cursor.execute("select * from tb_user_0")

result = cursor.fetchall()

print(json.JSONEncoder().encode(result))

conn.close()

