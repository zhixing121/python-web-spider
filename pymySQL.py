import pymysql

# conn = pymysql.connect(host="127.0.0.1", user='root', passwd='12346', db='mysql')
conn = pymysql.connect("localhost", 'root', '123456', 'mysql')
cur = conn.cursor()
cur.execute("USE scraping")

cur.execute("SELECT * FROM pages")
print(cur.fetchone())

cur.close()
conn.close()