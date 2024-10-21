import csv
import sqlite3



# CSVファイルのパス
station_file_path = r'amedas\station.csv'

# SQLiteデータベースに接続
with sqlite3.connect('amedas.db') as conn:
    cursor = conn.cursor()

    # CSVファイルを開いてデータをインポート
    with open(station_file_path, 'r', encoding='utf-8') as station:
        # CSVファイルのエンコーディングが UTF-8 以外である場合、
        # その正しいエンコーディングを調べる必要があります。
        # 例えば、CSVファイルが日本語を含んでいる場合、
        # エンコーディングが Shift-JIS であることがよくあります。
        reader = csv.reader(station)
        
        # ヘッダーをスキップ（必要に応じて）
        header=next(reader)

        index_nbr_idx=header.index("IndexNbr")
        country_area_idx=header.index("CountryArea")
        station_name_idx=header.index("StationName")

        # データをテーブルに挿入
        for row in reader:
            index_nbr = row[index_nbr_idx]
            country_area = row[country_area_idx]
            station_name = row[station_name_idx]
            cursor.execute('''INSERT OR REPLACE INTO m_index_numbers (IndexNbr, CountryArea, StationName)
            VALUES (?, ?, ?)''', (index_nbr, country_area, station_name))
            
    #         VALUES (?, ?, ?) は、データのプレースホルダです。SQLiteにデータを安全に挿入するために、
    # 直接データをSQL文に埋め込むのではなく、? を使ってパラメータを渡します。
    # この手法は SQLインジェクション のリスクを防ぐために使われます。
    # 各 ? は対応するデータの値（この場合、row の要素）で置き換えられます。
    # つまり、CSVの各行のデータが順番に ? の場所に挿入される形になります。



conn.commit()
conn.close()