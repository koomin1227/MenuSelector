import pymysql
conn = pymysql.connect(host='localhost',user='root',password='onenable1@',db='restaurant_db',charset='utf8')
sql = "insert into member(`member_id`, `member_name`,`pw`)values('test123','구민','test1234')"

user_id =''
user_name = ''

def select(sql):
    cur = conn.cursor()
    cur.execute(sql)
    datas = cur.fetchall()
    return datas

def login():
    global user_id
    global user_name
    id = input('id: ')
    pw = input('pw: ')
    cur = conn.cursor()
    sql = "select * from member where member_id = '" + id + "'"
    cur.execute(sql)
    datas = cur.fetchall()
    if len(datas) == 0:
        print("id나 비밀번호가 틀립니다\n\n")
        return False
    else:
        if datas[0][2] == pw:
            print(datas[0][1],"님 환영합니다.\n\n")
            user_id = datas[0][0]
            user_name = datas[0][1]
            return True
        else:
            print("id나 비밀번호가 틀립니다\n\n")

            return False

def make_account():# 계정등록후 로그인까지
    id = input('id: ')
    pw = input('pw: ')
    name = input('이름: ')
    cur = conn.cursor()
    sql = "select * from member where member_id = '" + id + "'"
    cur.execute(sql)
    datas = cur.fetchall()
    if len(datas) > 0:
        print('아이디가 중복 됩니다!! 다시 입력하세요. \n\n')
        return False
    sql = "insert into member(`member_id`, `member_name`,`pw`)values(%s,%s,%s)"
    val = (id,name,pw)
    cur.execute(sql,val)
    conn.commit()
    print('가입되었습니다. 로그인을 해주세요.')
    return True

def view_restaurant():
    while True:
        print('검색하고 싶은 식당을 입력하세요.')
        location = input('입력: ')
        sql = 'select * from rstaurant where'



while True:
    print('안녕하세요. 사용하시려면 로그인을 하세요. 없으시다면 회원가입을 해주세요')
    print('1)로그인 2)회원가입')
    n = int(input('입력 : '))
    if n == 1:
        if login():
            break
    elif n == 2:
        make_account()

while True:
    print('메뉴를 선택해주세요.')
    print('1)식당조희 2)내가 쓴 글 조회 3)로그아웃 4)종료')
    n = int(input('입력 : '))
    if n == 1:
        view_restaurant()
    elif n == 2:
        view_my_review()
    elif n == 3:
        print()
    elif n == 4:
        break

