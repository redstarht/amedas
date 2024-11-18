import sqlite3
import datetime


def dict_factory(cursor, row):
    d = {}
    for idx, col in enumerate(cursor.description):
        d[col[0]] = row[idx]
    return d

# インスタンス化した瞬間にDBにアクセスする
# DBの初期化、DBファイルがあれば使用 / なければ作成して使用(CREATE TABLE)
# DBへのデータ抽出・データ書き込み
# SELECTでないデータを書き込み
#






class AmedasDB():
    """
    DBからデータの出し入れのみ実施
    """

    def __init__(self, db_file) -> None:
        self.db_file = db_file
        self.create_db()

    def create_db(self):
        sql_create_db = '''
        CREATE TABLE IF NOT EXISTS t_weather_log (
            index_nbr INT NOT NULL,
            ymd TEXT NOT NULL,
            Local_Pressure_Average REAL NOT NULL,
            Sea_Level_Pressure_Average REAL NOT NULL,
            Total_Precipitation REAL NOT NULL,
            Maximum_1_Hour_Precipitation REAL NOT NULL,
            Maximum_10_Minute_Precipitation REAL NOT NULL,
            Average_Temperature REAL NOT NULL,
            Maximum_Temperature REAL NOT NULL,
            Minimum_Temperature REAL NOT NULL,
            Average_Humidity REAL NOT NULL,
            Minimum_Humidity REAL NOT NULL,
            Average_Wind_Speed REAL NOT NULL,
            Maximum_Wind_Speed REAL NOT NULL,
            Maximum_Wind_Speed_Direction TEXT NOT NULL,
            Maximum_Instantaneous_Wind_Speed REAL NOT NULL,
            Maximum_Instantaneous_Wind_Speed_Direction TEXT NOT NULL,
            Sunshine_Duration REAL NOT NULL,
            Total_Snowfall TEXT NOT NULL,
            Maximum_Snow_Depth TEXT NOT NULL,
            Weather_Summary_Daytime TEXT NOT NULL,
            Weather_Summary_Nighttime TEXT NOT NULL,
            CONSTRAINT index_nbr_pk primary key(index_nbr,ymd)
            ) 
        '''

        with sqlite3.connect(self.db_file) as conn:  # .dbファイルが無い場合は勝手に作ってくれる
            cur = conn.cursor()
            cur.execute(sql_create_db)
            conn.commit()

    def fetch_m_index_nbr(self):
        sql_m_index_nbr='''
        SELECT index_nbr, station_name
        FROM m_index_nbr
        '''
        with sqlite3.connect(self.db_file) as conn:  # .dbファイルが無い場合は勝手に作ってくれる
                try:
                    conn.row_factory = dict_factory
                    conn.text_factory = lambda x: x.decode("utf-8", errors="ignore")
                    cur = conn.cursor()
                    cur.execute(sql_m_index_nbr)
                    rows = cur.fetchall()

                except Exception as e:
                    print(e)
                    rows = []

        return rows
        

    def whether_data(self, index_nbr, year, month) -> list:  # ->アノテーション(型宣言/型注釈)
        from_ymd = datetime.date(year, month, 1)
        if month == 12:
            year += 1
            month = 1
        else:
            month += 1

        to_ymd = datetime.date(year, month, 1)

        # dateの範囲でデータを取得してくる
        # sql文を動的に作成
        sql = '''
        SELECT 
        index_nbr,
        ymd,
        Local_Pressure_Average,
        Sea_Level_Pressure_Average,
        Total_Precipitation,
        Maximum_1_Hour_Precipitation,
        Maximum_10_Minute_Precipitation,
        Average_Temperature,
        Maximum_Temperature,
        Minimum_Temperature,
        Average_Humidity,
        Minimum_Humidity,
        Average_Wind_Speed,
        Maximum_Wind_Speed,
        Maximum_Wind_Speed_Direction,
        Maximum_Instantaneous_Wind_Speed,
        Maximum_Instantaneous_Wind_Speed_Direction,
        Sunshine_Duration,
        Total_Snowfall,
        Maximum_Snow_Depth,
        Weather_Summary_Daytime,
        Weather_Summary_Nighttime
        FROM t_weather_log
        WHERE index_nbr=? and ymd >= ? and ymd < ?
        '''

        with sqlite3.connect(self.db_file) as conn:  # .dbファイルが無い場合は勝手に作ってくれる
            try:
                conn.row_factory = dict_factory
                cur = conn.cursor()
                cur.execute(sql,
                (index_nbr, 
                 from_ymd.strftime("%Y-%m-%d"),
                 to_ymd.strftime("%Y-%m-%d")))
                rows = cur.fetchall()

            except Exception as e:
                print(e)
                rows = []

        return rows

    # dattはdict型でもありリスト型でもあるけど・・・
    def save_whether_log(self, index_nbr: int, fetch_data: list):
        sql = '''
        INSERT INTO t_weather_log (
            index_nbr,
            ymd,
            Local_Pressure_Average,
            Sea_Level_Pressure_Average,
            Total_Precipitation,
            Maximum_1_Hour_Precipitation,
            Maximum_10_Minute_Precipitation,
            Average_Temperature,
            Maximum_Temperature,
            Minimum_Temperature,
            Average_Humidity,
            Minimum_Humidity,
            Average_Wind_Speed,
            Maximum_Wind_Speed,
            Maximum_Wind_Speed_Direction,
            Maximum_Instantaneous_Wind_Speed,
            Maximum_Instantaneous_Wind_Speed_Direction,
            Sunshine_Duration,
            Total_Snowfall,
            Maximum_Snow_Depth,
            Weather_Summary_Daytime,
            Weather_Summary_Nighttime
        )
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        ON CONFLICT (index_nbr, ymd)
        DO NOTHING
        '''
        # タプルのリスト に　変換
        insert_data = []
        print("-----------")
        print(fetch_data)
        for recode in range(len(fetch_data)):
            insert_data.append(tuple(fetch_data[recode].values()))

        with sqlite3.connect(self.db_file) as conn:
            try:  # try エラーが起きたら exceptのところにいくという処理
                cur = conn.cursor()
                cur.executemany(sql, insert_data)
                conn.commit()
            except Exception as e:
                print(e)
                conn.rollback()


#         sql = '''
#     insert into
#     t_weather_log (
#         id,
#         ymd,
#         total_precipitation,
#         total_snow,
#         weather_condition_night,
#         weather_condition_day,
#         average_temperature,
#         average_humidity,
#         average_wind_speed,
#         sunshine_hours,
#         min_temperature,
#         max_10min_precipitation,
#         max_1hour_precipitation,
#         max_gust_speed,
#         max_gust_direction,
#         max_wind_speed,
#         max_wind_direction,
#         min_humidity,
#         max_snow_depth,
#         max_temperature,
#         average_sea_pressure,
#         average_local_pressure,
#     )
# values (
#     ?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?
#     )
#     on conflict(id,ymd)
#     do NOTHING
# '''


# params = []


# params = [
#     (1,
#      "2024-09-07",
#         '1.5',
#         '--',
#         '薄曇時々晴',
#         '曇時々晴',
#         '9.1',
#         '72',
#         '4.6',
#         '5.9',
#         '4.2',
#      '0.5',
#      '1.5',
#      '14.1',
#      '北北西',
#      '9.2',
#      '北西',
#      '37',
#      '--',
#      '15.6',
#      '1018.7',
#      '1011.8')
# ]
