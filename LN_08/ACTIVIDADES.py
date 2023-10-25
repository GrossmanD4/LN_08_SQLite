#a
#import sqlite3
#conn = sqlite3.connect ('pedidos.db')
#cursor = conn.cursor()
#cursor.execute("CREATE TABLE PRUEBA( DNI VARCHAR(8))")
#b
#import sqlite3
#conn = sqlite3.connect('pedidos.db')
#print("Base de datos abierta satisfactoriamente");
#c
#import sqlite3
#conn = sqlite3.connect ('pedidos.db')
#cursor = conn.cursor()
#cursor.execute("""CREATE TABLE IF NOT EXISTS users(
#userid INT PRIMARY KEY,
#fname TEXT,
#lname TEXT,
#gender TEXT);
#""")
#conn.commit()
#d
#import sqlite3
#conn = sqlite3.connect ('pedidos.db')
#cursor = conn.cursor()
#cursor.execute("""CREATE TABLE IF NOT EXISTS orders(
#orderid INT PRIMARY KEY,
#date TEXT,
#userid TEXT,
#total TEXT);
#""")
#conn.commit()
#2a
#import sqlite3
#conn = sqlite3.connect('pedidos.db')
#print("Base de datos abierta satisfactoriamente");
#conn.execute("INSERT INTO orders (ORDERID, DATE, USERID, TOTAL) \
#VALUES (1, '02/12/2021', 1, 20000)");
#conn.execute("INSERT INTO orders (ORDERID, DATE, USERID, TOTAL) \
#VALUES (2, '02/10/2021', 2, 210)");
#conn.execute("INSERT INTO orders (ORDERID, DATE, USERID, TOTAL) \
#VALUES (3, '04/12/2019', 3, 415203)");
#conn.execute("INSERT INTO orders (ORDERID, DATE, USERID, TOTAL) \
#VALUES (4, '02/09/2019', 4, 2541360)");
#conn.commit()
#print("Registros creados satisfactoriamente");
#conn.close()
#2b
#import sqlite3
#conn = sqlite3.connect('pedidos.db')
#print("Base de datos abierta satisfactoriamente");
#cursor = conn.execute("SELECT ORDERID, DATE, USERID, TOTAL from orders")
#for row in cursor:
#    print("ORDERID = ", row[0])
#    print("DATE = ", row[1])
#    print("USERID = ", row[2])
#    print("TOTAL = ", row[3], "\n")
#
#print("Operacion realizada satisfactoriamente");
#conn.close()
#2c
#import sqlite3
#conn = sqlite3.connect('pedidos.db')
#print("Base de datos abierta satisfactoriamente");
#conn.execute("UPDATE orders set TOTAL = 25000.00 where ORDERID = 1")
#conn.commit()
#print("Número total de registros actualizados: ", conn.total_changes)
#cursor = conn.execute("SELECT ORDERID, DATE, USERID, TOTAL from orders")
#for row in cursor:
#    print("ORDERID = ", row[0])
#    print("DATE = ", row[1])
#    print("USERID = ", row[2])
#    print("TOTAL = ", row[3], "\n")
#print("Actualización realizada satisfactoriamente");
#conn.close()
#2d
#import sqlite3
#conn = sqlite3.connect('pedidos.db')
#print("Base de datos abierta satisfactoriamente");
#conn.execute("DELETE from orders where ORDERID = 2;")
#conn.commit()
#print("Número total de registros borrados: ", conn.total_changes)
#cursor = conn.execute("SELECT ORDERID, DATE, USERID, TOTAL from orders")
#for row in cursor:
#    print("ORDERID = ", row[0])
#    print("DATE = ", row[1])
#    print("USERID = ", row[2])
#    print("TOTAL = ", row[3], "\n")
#print("Eliminación realizada satisfactoriamente");
#conn.close()
#3a
#import sqlite3
#conn = sqlite3.connect('pedidos.db')
#order = (5, '15/06/2015', 3, 400215)
#cur=conn.cursor()
#cur.execute("INSERT INTO orders VALUES(?, ?, ?, ?);", order)
#conn.commit()
#moreOrders = [(6, '03/10/2021', 3, 2015478), (7, '02/01/2019', 3, 2015698)]
#cur.executemany("INSERT INTO orders VALUES(?, ?, ?, ?);", moreOrders)
#conn.commit()
#3b
#import sqlite3
#conn = sqlite3.connect('pedidos.db')
#print("Base de datos abierta satisfactoriamente");
#cur = conn.cursor()
#cur.execute("SELECT * FROM orders;")
#one_result = cur.fetchone()
#print(one_result)
#print("Consulta realizada satisfactoriamente");
#conn.close()
#3c
#import sqlite3
#conn = sqlite3.connect('pedidos.db')
#print("Base de datos abierta satisfactoriamente");
#cur = conn.cursor()
#cur.execute("SELECT * FROM orders;")
#three_results = cur.fetchmany(3)
#print(three_results)
#print("Consulta realizada satisfactoriamente");
#conn.close()
#3d
#import sqlite3
#conn = sqlite3.connect('pedidos.db')
#print("Base de datos abierta satisfactoriamente");
#cur = conn.cursor()
#cur.execute("SELECT * FROM orders;")
#all_results = cur.fetchall()
#for x in all_results:
#    print(x)
#print("Consulta realizada satisfactoriamente");
#conn.close()
#3e
#import sqlite3
#conn = sqlite3.connect('pedidos.db')
#print("Base de datos abierta satisfactoriamente");
#cur = conn.cursor()
#cur.execute("SELECT *, users.fname, users.lname FROM orders LEFT JOIN users ON "
#            "users.userid = orders.userid;")
#for x in cur.fetchall():
#    print(x)
#print("Consulta realizada satisfactoriamente");
#conn.close()
