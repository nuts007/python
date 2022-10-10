#coding: utf-8

## MYSQLの接続テスト

import MySQLdb

def main():
    # MYSQLへ接続
    connection = MySQLdb.connect(
        host='172.17.0.3',
        user='pydev',
        passwd='pydev_pass',
        db='pydev_sandbox'
    )
    cursor = connection.cursor()

    # print(help(cursor))
    # cursor.execute("insert into test values(2, 'python query')")

    query = "select * from test"
    result = cursor.execute(query)
    print(result)

    # MYSQLをコミット
    connection.commit()

    # MYSQLからの切断
    connection.close()


if __name__ == "__main__":
    main()