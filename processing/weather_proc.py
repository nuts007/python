#coding: utf-8

## 環境省からのオープンデータを用いたcsvファイルの加工

import pandas as pd
import numpy as np
import os
import csv
from datetime import datetime

class Main:
    def __init__(self):
        self.weather = pd.read_csv("/workplace/processing/weather.csv", encoding="shift_jis")

    def println(self):
        return print(self.weather)
    
    def types(self):
        return print(type(self.weather))

    def files(self):
        return self.weather
    
    def dataframes(self):
        return print(np.shape(self.weather))

if __name__ == "__main__":
    main = Main()

# main.println()
# main.types()

# encode0: 手動整形部分
## weather.csvのダウンロード日時の行および、空白行はあらかじめ削除
# encode1: ラベル名の整形
base_file = main.files()
df = base_file.rename(columns={"Unnamed: 0": "label"})
for labels in df.columns:
    new_label = labels.replace(".", "_")
    df = df.rename(columns={labels:new_label})

# encode2: データベースへの保存用に整形
state = []
temps = {}
flag = None
for city in df.columns.values:
    if city[0:2] != flag and city != "label":
        flag = city[0:2]
        state.append(flag)
        temps[city] = {}

recodes = np.array([], dtype="str")
for i in np.arange(start=2, stop=len(df.label), step=1):
    recodes = np.append(recodes, df.label[i])

## 格納イメージ type: dict --> {"state_name": {"recode_date_1": [m_avg_1, d_max_1, d_min_1, r_max_1, r_min_1], "recode_date_2"[...], ...}}
for city in state:
    for mt in recodes:
        temps[city][mt] = []
        name = list(map(lambda x: city if x == 0 else city + f"_{x}", range(5)))
        for nm in name:
            temps[city][mt].append(df[df["label"].isin([mt])][nm].values[0])

# encode3: そのままDBへインポートできるcsvファイルの作成
## state table: id(auto), state_name, create_at
## temprature table: state(foreign), recode_date, avg, dmax, dmin, rmax, rmin

## 実装フロー：空csvファイルの作成 > 必要情報の書き込み > 日付+labelでエクスポート
timestamp = datetime.strftime(datetime.now(), "%Y%m%d%H%M%S")
create_at = datetime.strftime(datetime.now(), "%Y/%m/%d")
export_state_path = f"/workplace/processing/export/{timestamp}_state.csv"
export_temp_path = f"/workplace/processing/export/{timestamp}_temp.csv"
if os.path.isfile(export_state_path):
    exit()
else:
    with open(export_state_path, "w") as f:
        f.write("")
        header = ["NAME", "CREATE_AT"]
        writer = csv.writer(f)
        writer.writerow(header)
        for city in state:
            writer.writerow([city, create_at])
        f.close()

if os.path.isfile(export_temp_path):
    exit()
else:
    with open(export_temp_path, "w") as f:
        f.write("")
        header = ["STATE", "RECODE", "AVG", "DMAX", "DMIN", "RMAX", "RMIN"]
        writer = csv.writer(f)
        writer.writerow(header)
        for city in state:
            for mt in recodes:
                save_arr = temps[city][mt]
                save_arr.insert(0, mt)
                save_arr.insert(0, city)
                if(len(save_arr) == 7):
                    writer.writerow(save_arr)
                else:
                    writer.writerow(["ERROR"])
        f.close()

        

        
    
    
