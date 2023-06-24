import pymysql
conn = pymysql.connect(host='localhost',user='root',password='onenable1@',db='restaurant_db',charset='utf8')

cur = conn.cursor()
# sql = 'select res_id from restaurant where res_name = "고깃집열"'
# sql = "insert into restaurant(`res_name`, `tel_no`,`address`,`url`,`score`)values('김밥천국3','02-123-4567','남양주시 호평동','www.asdasdasdasfa/asasf/safas',4.2)"

sql = "insert into member(`member_id`, `member_name`,`pw`)values('test123','구민','test1234')"
cur.execute(sql)
conn.commit()
# for row in cur:
#     print(row[0])