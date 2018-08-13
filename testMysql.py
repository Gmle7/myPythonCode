import pymysql  #导入 pymysql

#打开数据库连接
conn = pymysql.connect(
    host="192.168.10.239",
    user="root",
    passwd="manager",
    db="analysis",
    port=3306)
# 使用cursor()方法获取操作游标
cursor = conn.cursor()
sql = "select * from t_flow_component"
try:
    cursor.execute(sql)  #执行sql语句
    results = cursor.fetchall()  #获取查询的所有记录
    print("id", "name", "password")
    #遍历结果
    for row in results:
        id = row[0]
        name = row[1]
        password = row[2]
        print(id, name, password)
except Exception as e:
    raise e
finally:
    #cursor.close()
    conn.close()  #关闭连接