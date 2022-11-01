#coding:utf-8

## mysql-connecor-pythonを利用した接続
## 接続情報は別ファイルから取り込みファイル内への直書きは禁止をテスト

import mysql.connector as mc
import json
import os
import datetime

def main():
    path = "/workplace/auth/mysql_info.json"
    
    if os.path.isfile(path) == False:
        print("mysql info file not found")
    else:
        with open(path) as f:
            conf = json.load(f)
            connect = mc.connect(user=conf["mysql"]["user"], password=conf["mysql"]["password"], host=conf["mysql"]["host"], database=conf["mysql"]["db"])
            cursor = connect.cursor()
            now = datetime.datetime.now()
            format_now = now.strftime("%y-%m-%d")
            cursor.execute("select * from char_test")
            for row in cursor.fetchall():
                print(row)
            # connect.commit()

            f.close()

if __name__ == "__main__":
    main()
