import requests
from amedas.amedas_db import AmedasDB
# amedas➡フォルダ名 .db➡db.py
from amedas.amedas_api import Amedas_Api
from dateutil.relativedelta import relativedelta
import datetime
# amedas


class Amedas():
    """
    全体のデータコントロール
    あったらdb.pyからデータを見に行く
    なかったらamedas_api.pyを使用し、アメダスAPIからデータを取得する    
    """

    DEFAULT_BASE_URL = "https://api.cultivationdata.net/"  # インスタンスする前に使える
    DEFAULT_DB_PATH = "amedas.db"

    def __init__(self, url: str = DEFAULT_BASE_URL, db_path=DEFAULT_DB_PATH) -> None:  # return で帰ってくるのはNone
        # url = DEFAULT_BASE_URL でurlに引数として何も渡されない場合は DEFAULT_BASE_URLをいれてくれる
        self.base_url = url  # self = インスタンス インスタンス生成時にurlを持たせるようにする
        self.db_path = db_path  # インスタンス変数
        self.db = AmedasDB(self.db_path)
        self.api = Amedas_Api()

    def index_numbers(self):
        return (self.db.fetch_m_index_nbr())

    def whether_date_range(self, index_select, from_ym: datetime, to_ym: datetime):
        '''
        やりたいこと
        from_ym と to_ym の間の値を月ごとに出力し
        月単位で amedas_dbのwhether_data関数の中に引数で入れて
        dataを取ってくる
        その後、この関数の中で
        取ってきたdataを結合する   
        '''

        # from_ym から to_ym までの各月をイテレート
        current_date = from_ym
        target_rows=[]
        # 開始月から終了月までのデータを取得 
        while current_date <= to_ym:
            year = current_date.year
            month = current_date.month
            # もし配列に要素がなかったら取得しに行く
            target_data=self.db.whether_data(index_select, year, month)
            if target_data:
                target_rows.extend(target_data)
            else:
                fetch_data = []
                # APIからネストの辞書型データを取得
                fetch_data_raw=self.api.fetch_kako_data(index_select,year,month)
                for k, v in fetch_data_raw[list(fetch_data_raw.keys())[0]].items():  # アンパッキング
                    fetch_data.append(
                    {
                        "id": index_select,
                        "ymd": datetime.datetime.strptime(k, "%Y-%m-%d").strftime("%Y-%m-%d"),
                        # 三項演算子
                        "Local_Pressure_(Average)": v["現地気圧（平均）"] if v["現地気圧（平均）"] not in [None, "--"] else "0",
                        "Sea_Level_Pressure_(Average)": v["海面気圧（平均）"] if v["海面気圧（平均）"] not in [None, "--"] else "0",
                        "Total_Precipitation": v["合計降水量"] if v["合計降水量"] not in [None, "--"] else "0",
                        "Maximum_1-Hour_Precipitation": v["最大1時間降水量"] if v["最大1時間降水量"] not in [None, "--"] else "0",
                        "Maximum_10-Minute_Precipitation": v["最大10分間降水量"] if v["最大10分間降水量"] not in [None, "--"] else "0",
                        "Average_Temperature": v["平均気温"] if v["平均気温"] not in [None, "--"] else "0",
                        "Maximum_Temperature": v["最高気温"] if v["最高気温"] not in [None, "--"] else "0",
                        "Minimum_Temperature": v["最低気温"] if v["最低気温"] not in [None, "--"] else "0",
                        "Average_Humidity": v["平均湿度"] if v["平均湿度"] not in [None, "--"] else "0",
                        "Minimum_Humidity": v["最小湿度"] if v["最小湿度"] not in [None, "--"] else "0",
                        "Average_Wind_Speed": v["平均風速"] if v["平均風速"] not in [None, "--"] else "0",
                        "Maximum_Wind_Speed": v["最大風速"] if v["最大風速"] not in [None, "--"] else "0",
                        "Maximum_Wind_Speed_(Direction)": v["最大風速（風向）"] if v["最大風速（風向）"] not in [None, "--"] else "0",
                        "Maximum_Instantaneous_Wind_Speed": v["最大瞬間風速"] if v["最大瞬間風速"] not in [None, "--"] else "0",
                        "Maximum_Instantaneous_Wind_Speed_(Direction)": v["最大瞬間風速（風向）"] if v["最大瞬間風速（風向）"] not in [None, "--"] else "0",
                        "Sunshine_Duration": v["日照時間"] if v["日照時間"] not in [None, "--"] else "0",
                        "Total_Snowfall": v["合計降雪"] if v["合計降雪"] not in [None, "--"] else "0",
                        "Maximum_Snow_Depth": v["最深積雪"] if v["最深積雪"] not in [None, "--"] else "0",
                        "Weather_Summary_(Daytime)": v["天気概況（昼）"] if v["天気概況（昼）"] not in [None, "--"] else "0",
                        "Weather_Summary_(Nighttime)": v["天気概況（夜）"] if v["天気概況（夜）"] not in [None, "--"] else "0"
                    })
                # 取得したデータはDBへ保存
                print(fetch_data)
                self.db.save_whether_log(index_select, fetch_data)
                target_rows.extend(target_data)

            # 1か月後に進める
            current_date += relativedelta(months=1)

        print(target_rows)
        return target_rows

    # from_ym_y = from_ym.year
    # from_ym_m = from_ym.month
    # to_ym_y = to_ym.year
    # to_ym_m = to_ym.month
    # submit_from = {"index_select": index_select,
    #             "year": from_ym_y, "month": from_ym_m}
    # submit_to = {"index_select": index_select,
    #             "year": to_ym_y, "month": to_ym_m}
    # submit_from["year"]
    # submit_from["month"]
    # submit_to["year"]
    # submit_to["month"]

    def whether_data(self, index_nbr: int, year: int, month: int):
        # DBへアクセスして引数で指定された 国際地点番号 と 年月データ がDBにあるか確認する
        target_data = self.db.whether_data(index_nbr, year, month)
        # あった場合はデータ返す
        if target_data:
            return target_data

        # AmedasApiにデータを取りに行く

        fetch_data_raw = self.api.fetch_kako_data(index_nbr, year, month)
        fetch_data = []
        for k, v in fetch_data_raw[list(fetch_data_raw.keys())[0]].items():  # アンパッキング
            '''
            地名=list(fetch_data_raw.keys())[0] で地名抜き出し
            fetch_data_raw[地名]
            '''
            print(k, v["現地気圧（平均）"])
            print(k, v)
            fetch_data.append(
                {
                    "id": index_nbr,
                    "ymd": datetime.datetime.strptime(k, "%Y-%m-%d").strftime("%Y-%m-%d"),
                    # 三項演算子
                    "Local_Pressure_(Average)": v["現地気圧（平均）"] if v["現地気圧（平均）"] not in [None, "--"] else "0",
                    "Sea_Level_Pressure_(Average)": v["海面気圧（平均）"] if v["海面気圧（平均）"] not in [None, "--"] else "0",
                    "Total_Precipitation": v["合計降水量"] if v["合計降水量"] not in [None, "--"] else "0",
                    "Maximum_1-Hour_Precipitation": v["最大1時間降水量"] if v["最大1時間降水量"] not in [None, "--"] else "0",
                    "Maximum_10-Minute_Precipitation": v["最大10分間降水量"] if v["最大10分間降水量"] not in [None, "--"] else "0",
                    "Average_Temperature": v["平均気温"] if v["平均気温"] not in [None, "--"] else "0",
                    "Maximum_Temperature": v["最高気温"] if v["最高気温"] not in [None, "--"] else "0",
                    "Minimum_Temperature": v["最低気温"] if v["最低気温"] not in [None, "--"] else "0",
                    "Average_Humidity": v["平均湿度"] if v["平均湿度"] not in [None, "--"] else "0",
                    "Minimum_Humidity": v["最小湿度"] if v["最小湿度"] not in [None, "--"] else "0",
                    "Average_Wind_Speed": v["平均風速"] if v["平均風速"] not in [None, "--"] else "0",
                    "Maximum_Wind_Speed": v["最大風速"] if v["最大風速"] not in [None, "--"] else "0",
                    "Maximum_Wind_Speed_(Direction)": v["最大風速（風向）"] if v["最大風速（風向）"] not in [None, "--"] else "0",
                    "Maximum_Instantaneous_Wind_Speed": v["最大瞬間風速"] if v["最大瞬間風速"] not in [None, "--"] else "0",
                    "Maximum_Instantaneous_Wind_Speed_(Direction)": v["最大瞬間風速（風向）"] if v["最大瞬間風速（風向）"] not in [None, "--"] else "0",
                    "Sunshine_Duration": v["日照時間"] if v["日照時間"] not in [None, "--"] else "0",
                    "Total_Snowfall": v["合計降雪"] if v["合計降雪"] not in [None, "--"] else "0",
                    "Maximum_Snow_Depth": v["最深積雪"] if v["最深積雪"] not in [None, "--"] else "0",
                    "Weather_Summary_(Daytime)": v["天気概況（昼）"] if v["天気概況（昼）"] not in [None, "--"] else "0",
                    "Weather_Summary_(Nighttime)": v["天気概況（夜）"] if v["天気概況（夜）"] not in [None, "--"] else "0"
                })
        # 取得したデータはDBへ保存
        print(fetch_data)
        self.db.save_whether_log(index_nbr, fetch_data)

        target_data = self.db.whether_data(index_nbr, year, month)
        # あった場合はデータ返す
        if target_data:
            return target_data

        # insert_data=[]
        # for recode in range(len(fetch_data)):
        #    insert_data.append(tuple(fetch_data[recode].values()))

        # # 呼び出し元に返す
        # return(insert_data)

    def weather_db_check(index_nbr, from_ym, to_ym):
        pass


if __name__ == "__main__":  # python 特殊メソッド
    Amedas = Amedas()
    date = Amedas.fetch_kako_data(47636, 2024, 7)
    print(date)
