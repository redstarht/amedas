from flask import Flask, render_template, request, jsonify
import datetime
from amedas import amedas
# from amedas.amedas import amedas

amd = amedas.Amedas(db_path="AAA.db")

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/menu/<line_code>")
def menu(line_code):
    print(line_code)
    if line_code == "xxx":
        msg = "ASDF"
    else:
        msg = "!!!!!"

    return render_template("menu.html", line_code=line_code, msg=msg)


@app.route("/index_nbr")
def index_nbr():
    result = [
        {"index_nbr": 100,
         "station_name": "仮町"},
        {"index_nbr": 200,
         "station_name": "kari"}

        # ここのデータをもとにプルダウン作成
    ]
    return jsonify(result)


@app.route("/city")
def city():
    return "city"


@app.route("/weather_date")
def weather_date():
    """
    #docstring xxxxxxxxxxx この関数はどういう機能を示すのかを記載
    引数が必要な時はそこに　引数で渡すものの説明を各
    例：指定された都市の、指定期間の気象データを返す
    params: asd str 年コード "231201"
    return: json

    #docktest
    この関数が正しく動くかをテストする事
    """

    index_nbr = request.args.get('index_nbr', None)
    from_ym = request.args.get('from', None)
    to_ym = request.args.get("to", None)  # 第1引数の文字列がクエリ文字になる
    # http://127.0.0.1:5000/weather_date?index_nbr=123&from=2024-07%E2%80%99&to=2024-10

    if (index_nbr is None) or (from_ym is None) or (to_ym is None):
        return jsonify(
            {
                "success": False,
                "message": "パラメータの設定が正しくありません",
                "your request": request.url
            })

    print(index_nbr, from_ym, to_ym)

    result = amd.fetch_kako_data(index_nbr=47636, year=2024, month=4)

    print(result)

    result = [
        {"date": "2024-01-01", "temp_ave": 10.0,
            "temp_high": 20.0, "temp_low": 1.0},
        {"date": "2024-01-02", "temp_ave": 10.0,
            "temp_high": 20.0, "temp_low": 1.0},
        {"date": "2024-01-03", "temp_ave": 10.0,
            "temp_high": 20.0, "temp_low": 1.0},
    ]
    return jsonify(result)


@app.route("/amedas_data")
def amedas_data():
    amdno = request.args.get("amdno", None)  # 引数の中から任意のとこだけとってくる
    year = request.args.get("year", None)
    month = request.args.get("month", None)

    # "1個でも空欄だったらNone"

    # 指定された条件でデータをDBから取得し、返す形に加工する
    response_data = [
        {"ymd": "2024-07-01", "temp_average": 20, "temp_high": 23, "temp_low": 15},
        {"ymd": "2024-07-02", "temp_average": 21, "temp_high": 24, "temp_low": 15},
        {"ymd": "2024-07-03", "temp_average": 22, "temp_high": 25, "temp_low": 15},
        {"ymd": "2024-07-04", "temp_average": 23, "temp_high": 26, "temp_low": 15},
    ]

    return jsonify(response_data)

@app.route("/debug_db")
def debug_db():
    from amedas import amedas_api
    api = amedas_api.Amedas_Api()
    index_nbr = 47636
    year = 2024
    month = 2
    data=amd.whether_data(index_nbr,year,month)
    return jsonify(data)


@app.route("/debug")
def debug():
    from amedas import amedas_api
    api = amedas_api.Amedas_Api()
    index_nbr = 47636
    year = 2024
    month = 5
    date = api.fetch_kako_data(index_nbr=index_nbr, year=year, month=month)
    # データ成形　or DB.apiにおくってから成形　どっちでもよい

    d = date[list(date.keys())[0]]

    date_for_db = []

    for k, v in d.items():
        print(k, v)

        datestr = datetime.datetime.strptime(
            k, "%Y-%m-%d").strftime("%Y-%m-%d")

        date_for_db.append(
            (index_nbr, datestr,
            v['合計降水量'],
            v['合計降雪'],
            v['天気概況（夜）'],
            v['天気概況（昼）'],
            v['平均気温'],
            v['平均湿度'],
            v['平均風速'],
            v['日照時間'],
            v['最低気温'],
            v['最大10分間降水量'],
            v['最大1時間降水量'],
            v['最大瞬間風速'],
            v['最大瞬間風速（風向）'],
            v['最大風速'],
            v['最大風速（風向）'],
            v['最小湿度'],
            v['最深積雪'],
            v['最高気温'],
            v['海面気圧（平均）'],
            v['現地気圧（平均）']
             ))
    
    print(date_for_db)
    
    from amedas import amedas_db
    db = amedas_db.AmedasDB("debug.db")
    db.save_whether_log(index_nbr, date)
