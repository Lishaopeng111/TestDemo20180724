import pymysql.cursors

host = '127.0.0.1'
port = 3306
user = 'root'
password = '073434'
db = 'python'

connect = pymysql.Connect(host=host, port=port, user=user, password=password, database=db, charset='utf8')
cursor = connect.cursor()

# 增
sql = 'INSERT INTO trade(name,account,saving) VALUES("李少拉","15191292433","100100")'
cursor.execute(sql)
connect.commit()
print(cursor.rowcount)

# 删
sql = 'DELETE FROM trade WHERE NAME="李少鹏1"'
cursor.execute(sql)
connect.commit()
print(cursor.rowcount)

# 改
sql = 'UPDATE trade SET NAME="李少拉" WHERE NAME ="李少鹏"'
cursor.execute(sql)
connect.commit()
print(cursor.rowcount)

# 查
sql = 'SELECT * FROM trade '
cursor.execute(sql)
connect.commit()
print(cursor.rowcount)
