# SQLite

import sqlite3

db_path="amedas.db"

#""" で囲むと改行して記述できる
sql_create_1="""
    CREATE TABLE IF NOT EXISTS m_amdno (
    amdno INT NOT NULL ,
    city_name TEXT NOT NULL,
    CONSTRAINT m_amdno_pk primary key(amdno)
) 
"""

m_index_numbers="""
    CREATE TABLE IF NOT EXISTS m_index_numbers(
    indexNbr INT NOT NULL,
    CountryArea TEXT NOT NULL,
    StationName TEXT NOT NULL,
    CONSTRAINT m_index_numbers_pk primary key(indexNbr)
    ) 
"""
t_weather_log=f"""
CREATE TABLE IF NO EXISTS {station_name}(
indexNbr INT NOT NULL,
date TEXT NOT NULL,
temp_average REAL NOT NULL,
temp_high REAL NOT NULL,
temp_low REAL NOT NULL
)

"""


with sqlite3.connect(db_path) as conn:
    try: #try エラーが起きたら exceptのところにいくという処理
        cur = conn.cursor()
        cur.execute(sql_create_1)
        cur.execute(m_index_numbers)
        cur.execute(t_weather_log)
        conn.commit()
    except:
        conn.rollback() #rollback() によって、実行中のトランザクションがキャンセルされ、データベースは変更前の状態に戻ります。
