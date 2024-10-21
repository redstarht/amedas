import requests
from amedas.amedas_db import AmedasDB
# amedas➡フォルダ名 .db➡db.py
from amedas.amedas_api import Amedas_Api
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

    def whether_data(self, index_nbr: int, year: int, month: int):
        pass
        # DBへアクセスして引数で指定された 国際地点番号 と 年月データ がDBにあるか確認する
        target_data = self.db.whether_data(index_nbr, year, month)
        # あった場合はデータ返す
        if target_data:
            return target_data

        # AmedasApiにデータを取りに行く

        fetch_data_raw = self.api.fetch_kako_data(index_nbr, year, month)
        fetch_data = []
        for k, v in fetch_data_raw.items():  # アンパッキング
            print(k, v["現地気圧（平均）"])
            print(k, v)
            fetch_data.append(
                {
                    "id": index_nbr,
                    "ymd": k,
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
        self.db.save_whether_log(index_nbr, fetch_data)

        # 呼び出し元に返す
        pass

    def weather_db_check(index_nbr, from_ym, to_ym):
        pass


if __name__ == "__main__":  # python 特殊メソッド
    Amedas = Amedas()
    date = Amedas.fetch_kako_data(47636, 2024, 7)
    print(date)
