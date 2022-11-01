#coding: utf-8

## mysqlから各地方の天気の情報を抽出しグラフ化

import numpy as np
import mysql.connector
from matplotlib import pyplot as plt
import seaborn as sns
import json

sns.set()

class db_connect:
    def __init__(self):
        self.conf = json.load(open("/workplace/auth/mysql_info.json", "r"))
        self.connect = mysql.connector.connect(user=self.conf["mysql"]["user"], password=self.conf["mysql"]["password"], host=self.conf["mysql"]["host"], database=self.conf["mysql"]["db"])
    
    def __call__(self):
        return print(self.connect.is_connected())
    
    def select(self, tl_name, col_name=np.array([], dtype="str")):
        col_set = ""
        if len(col_name)>0:
            for i in range(len(col_name)):
                if i == len(col_name)-1:
                    col_set += col_name[i]
                else:
                    col_set += f"{col_name[i]},"
            query = f"select {col_set} from {tl_name}"
        else:
            query = f"select * from {tl_name}"
        
        cursor = self.connect.cursor()
        cursor.execute(query)
        return cursor.fetchall()
    
    def close(self):
        self.connect.close()


def main():
    mysql = db_connect()
    res = mysql.select("State", ["id", "name"])
    print(res)
    mysql.close()

if __name__ == "__main__":
    main()