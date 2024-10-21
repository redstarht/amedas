##　変数名

recode["index_nbr"],
 recode["ymd"],
 recode["Local_Pressure_(Average)"],
 recode["Sea_Level_Pressure_(Average)"],
 recode["Total_Precipitation"],
 recode["Maximum_1-Hour_Precipitation"]
 recode["Maximum_10-Minute_Precipitation"]
 recode["Average_Temperature"]
 recode["Maximum_Temperature"]
 recode["Minimum_Temperature"]
 recode["Average_Wind_Speed"]
 recode["Maximum_Wind_Speed"]
 recode["Maximum_Wind_Speed_(Direction)"]
 recode["Maximum_Instantaneous_Wind_Speed_(Direction)"]
 recode["Sunshine_Duration"]
 recode["Total_Snowfall"]
 recode["Maximum_Snow_Depth"]
 recode["Weather_Summary_(Daytime)"]
 recode["Weather_Summary_(Nighttime)"]


recode["index_nbr"],
 recode["ymd"],
 recode["Local_Pressure_(Average)"],
 recode["Sea_Level_Pressure_(Average)"],
 recode["Total_Precipitation"],
 recode["Maximum_1-Hour_Precipitation"]
 recode["Maximum_10-Minute_Precipitation"]
 recode["Average_Temperature"]
 recode["Maximum_Temperature"]
 recode["Minimum_Temperature"]
 recode["Average_Humidity"]
 recode["Minimum_Humidity"]
 recode["Average_Wind_Speed"]
 recode["Maximum_Wind_Speed"]
 recode["Maximum_Wind_Speed_(Direction)"]
 recode["Maximum_Instantaneous_Wind_Speed"]
 recode["Maximum_Instantaneous_Wind_Speed_(Direction)"]
 recode["Sunshine_Duration"]
 recode["Total_Snowfall"]
 recode["Maximum_Snow_Depth"]
 recode["Weather_Summary_(Daytime)"]
 recode["Weather_Summary_(Nighttime)"]








            index_nbr INT NOT NULL,
            ymd TEXT NOT NULL,
            Local_Pressure_(Average) REAL NOT NULL,
            Sea_Level_Pressure_(Average) REAL NOT NULL,
            Total_Precipitation REAL NOT NULL,
            Maximum_1-Hour_Precipitation REAL NOT NULL,
            Maximum_10-Minute_Precipitation REAL NOT NULL,
            Average_Temperature REAL NOT NULL,
            Maximum_Temperature REAL NOT NULL,
            Minimum_Temperature REAL NOT NULL,
            Average_Humidity REAL NOT NULL,
            Minimum_Humidity REAL NOT NULL,
            Average_Wind_Speed REAL NOT NULL,
            Maximum_Wind_Speed REAL NOT NULL,
            Maximum_Wind_Speed_(Direction) TEXT NOT NULL,
            Maximum_Instantaneous_Wind_Speed REAL NOT NULL,
            Maximum_Instantaneous_Wind_Speed_(Direction) TEXT NOT NULL,
            Sunshine_Duration REAL NOT NULL,
            Total_Snowfall TEXT NOT NULL,
            Maximum_Snow_Depth TEXT NOT NULL,
            Weather_Summary_(Daytime) TEXT NOT NULL,
            Weather_Summary_(Nighttime) TEXT NOT NULL,




    "index_nbr":number,
    "ymd":k,
    "Local_Pressure_(Average)": v["現地気圧（平均）"],
    "Sea_Level_Pressure_(Average)": v["海面気圧（平均）"],
    "Total_Precipitation": v["合計降水量"],
    "Maximum_1-Hour_Precipitation": v["最大1時間降水量"],
    "Maximum_10-Minute_Precipitation": v["最大10分間降水量"],
    "Average_Temperature": v["平均気温"],
    "Maximum_Temperature": v["最高気温"],
    "Minimum_Temperature": v["最低気温"],
    "Average_Humidity": v["平均湿度"],
    "Minimum_Humidity": v["最小湿度"],
    "Average_Wind_Speed": v["平均風速"],
    "Maximum_Wind_Speed": v["最大風速"],
    "Maximum_Wind_Speed_(Direction)": v["最大風速（風向）"],
    "Maximum_Instantaneous_Wind_Speed": v["最大瞬間風速"],
    "Maximum_Instantaneous_Wind_Speed_(Direction)": v["最大瞬間風速（風向）"],
    "Sunshine_Duration": v["日照時間"],
    "Total_Snowfall": v["合計降雪"],
    "Maximum_Snow_Depth": v["最深積雪"],
    "Weather_Summary_(Daytime)": v["天気概況（昼）"],
    "Weather_Summary_(Nighttime)": v["天気概況（夜）"]


            
            
            
            
            
            
            "id":index_nbr,
            "ymd":k,
            "Local_Pressure_(Average)": v["現地気圧（平均）"] if v["現地気圧（平均）"] not in [None, "--"] else "0",
            "Sea_Level_Pressure_(Average)": v["海面気圧（平均）"] if v["海面気圧（平均）"]  not in [None, "--"] else "0",
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
            "Weather_Summary_(Nighttime)": v["天気概況（夜）"] if v["天気概況（夜）"]  not in [None, "--"] else "0"









average_local_pressure
average_sea_pressure
total_precipitation
max_1hour_precipitation
max_10min_precipitation
average_temperature
max_temperature
min_temperature
average_humidity
min_humidity
average_wind_speed
max_wind_speed
max_wind_direction
max_gust_speed
max_gust_direction
sunshine_hours
total_snow
max_snow_depth
weather_condition_day
weather_condition_night 


[(47636, '2024-2-1', '1011.8', '1018.7', '1.5', '1.5', '0.5', '9.1', '15.6', '4.2', '72', '37', '4.6', '9.2', '北西', '14.1', '北北西', '5.9', '--', '--', '曇時々晴', '薄曇時々晴'), (47636, '2024-2-2', '1017.0', '1024.0', '--', '--', '--', '4.3', '9.2', '1.5', '51', '40', '4.5', '7.8', '西北西', '12.0', '北西', '6.0', '--', '--', '晴時々曇', '晴一時薄曇'), (47636, '2024-2-3', '1019.2', '1026.3', '0.0', '0.0', '0.0', '6.2', '11.7', '0.5', '50', '30', '2.7', '5.6', '北', '8.1', '北北西', '7.0', '--', '--', '晴時々曇', '雨時々曇'), (47636, '2024-2-4', '1016.5', '1023.4', '0.0', '0.0', '0.0', '8.2', '14.2', '5.4', '60', '42', '3.4', '6.0', '北西', '9.9', '北西', '7.6', '--', '--', '晴一時雨', '曇時々晴'), (47636, '2024-2-5', '1009.3', '1016.3', '24.0', '8.0', '3.0', '5.0', '6.1', '3.7', '81', '51', '3.4', '5.6', '北東', '9.6', '北西', '0.0', '--', '--', '雨一時曇', '晴時々曇一時雨'), (47636, '2024-2-6', '1010.6', '1017.5', '--', '--', '--', '6.0', '10.9', '2.4', '69', '42', '3.9', '8.6', '西北西', '13.2', '西北西', '7.6', '--', '--', '晴一時曇', '晴'), (47636, '2024-2-7', '1010.5', '1017.5', '--', '--', '--', '5.6', '12.0', '0.9', '70', '44', '3.0', '6.8', '西北西', '11.1', '北西', '9.9', '--', '--', '晴', '快晴'), (47636, '2024-2-8', '1010.6', '1017.6', '--', '--', '--', '5.3', '11.1', '0.4', '58', '33', '3.7', '7.5', '西北西', '11.8', '北西', '9.2', '--', '--', '晴時々薄曇', '薄曇'), (47636, '2024-2-9', '1011.0', '1018.0', '--', '--', '--', '6.4', '12.0', '2.2', '52', '33', '3.0', '5.8', '北', '8.3', '北北西', '6.1', '--', '--', '晴時々薄曇', '快晴'), (47636, '2024-2-10', '1011.5', '1018.5', '--', '--', '--', '5.8', '13.1', '0.6', '67', '42', '3.2', '8.9', '西北西', '12.9', '西北西', '9.0', '--', '--', '晴時々薄曇', '晴'), (47636, '2024-2-11', '1012.7', '1019.7', '0.0', '0.0', '0.0', '6.1', '12.2', '2.3', '65', '32', '3.0', '6.1', '北北西', '9.6', '北北西', '6.9', '--', '--', '晴時々曇', '曇時々晴'), (47636, '2024-2-12', '1019.6', '1026.6', '0.0', '0.0', '0.0', '6.7', '12.5', '2.2', '67', '34', '3.2', '6.6', '西北西', '10.3', '西北西', '9.5', '--', '--', '晴', '快晴'), (47636, '2024-2-13', '1024.2', '1031.3', '--', '--', '--', '7.5', '14.9', '0.7', '62', '37', '1.5', '3.4', '南南西', '5.0', '南西', '10.3', '--', '--', '快晴', '快晴'), (47636, '2024-2-14', '1020.1', '1027.0', '--', '--', '--', '10.9', '19.2', '3.7', '62', '35', '1.8', '3.7', '南西', '6.3', '北', '7.8', '--', '--', '晴後薄曇', '晴後時々曇'), (47636, '2024-2-15', '1010.7', '1017.5', '4.0', '1.0', '1.0', '10.8', '14.3', '7.5', '82', '61', '1.3', '4.7', '北北西', '8.5', '北北西', '0.0', '--', '--', '曇後時々雨', '曇時々雨'), (47636, '2024-2-16', '1010.5', '1017.4', '--', '0.0', '--', '9.2', '13.4', '6.3', '52', '33', '5.6', '9.2', '北西', '15.4', '北西', '8.9', '--', '--', '晴時々曇', '曇時々晴'), (47636, '2024-2-17', '1016.3', '1023.2', '0.5', '0.5', '0.5', '10.1', '15.6', '6.1', '62', '42', '2.0', '4.2', '北北西', '6.1', '北北西', '1.0', '--', '--', '曇一時雨', '曇時々雨'), (47636, '2024-2-18', '1020.3', '1027.2', '0.5', '0.5', '0.5', '12.3', '15.7', '10.2', '85', '67', '1.6', '3.5', '南東', '7.1', '東南東', '0.0', '--', '--', '曇時々雨', '雨時々曇'), (47636, '2024-2-19', '1013.9', '1020.7', '47.0', '6.5', '1.5', '14.9', '16.3', '12.5', '97', '90', '4.2', '7.2', '南南東', '12.7', '南南東', '0.0', '--', '--', '大雨一時曇', '雨時々曇一時霧'), (47636, '2024-2-20', '1011.5', '1018.2', '2.0', '1.5', '0.5', '16.3', '21.6', '12.4', '82', '58', '2.8', '6.4', '西北西', '9.7', '北西', '7.6', '--', '--', '薄曇一時霧', '曇時々晴'), (47636, '2024-2-21', '1010.1', '1016.9', '15.0', '4.5', '2.5', '12.1', '13.1', '10.9', '91', '77', '2.0', '4.9', '北西', '8.5', '北西', '0.0', '--', '--', '雨一時曇', '雨時々曇'), (47636, '2024-2-22', '1010.6', '1017.5', '7.5', '2.5', '1.0', '9.1', '12.0', '5.5', '79', '65', '3.6', '5.8', '北西', '9.3', '北西', '0.6', '--', '--', '曇時々雨', '雨時々曇'), (47636, '2024-2-23', '1014.4', '1021.4', '12.5', '3.0', '1.0', '5.8', '8.6', '4.3', '79', '53', '3.6', '7.3', '北北西', '12.3', '北北西', '0.3', '--', '--', '雨時々曇', '晴一時薄曇'), (47636, '2024-2-24', '1017.9', '1024.9', '--', '--', '--', '6.8', '12.6', '1.8', '55', '33', '2.3', '4.6', '北北西', '7.0', '西南西', '9.7', '--', '--', '晴後時々薄曇', '曇時々雨一時晴'), (47636, '2024-2-25', '1011.4', '1018.4', '6.0', '1.0', '0.5', '6.4', '7.4', '5.1', '91', '65', '2.7', '5.2', '北', '7.4', '北', '0.0', '--', '--', '雨', '晴時々曇一時雨'), (47636, '2024-2-26', '1009.6', '1016.5', '--', '--', '--', '7.9', '13.5', '4.6', '56', '33', '6.2', '10.0', '北北西', '17.4', '北北西', '10.4', '--', '--', '晴', '晴'), (47636, '2024-2-27', '1014.3', '1021.3', '--', '--', '--', '6.2', '11.9', '3.2', '47', '32', '6.3', '10.4', '北西', '16.9', '北西', '8.0 )', '--', '--', '晴', '晴一時薄曇'), (47636, '2024-2-28', '1018.6', '1025.6', '--', '--', '--', '7.6', '14.4', '2.3', '47', '29', '4.5', '7.7', '西北西', '11.0', '西北西', '10.9', '--', '--', '快晴', '晴時々曇'), (47636, '2024-2-29', '1014.4', '1021.4', '18.0', '5.5', '1.5', '6.6', '10.8', '2.9', '70', '39', '2.2', '4.3', '北北西', '7.0', '北北西', '0.1', '--', '--', '曇後時々雨', '雨後一時曇')]