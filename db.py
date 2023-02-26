import pymysql

#host - ip address (데이터 베이스 서버가 있는 서버의 주소 ) [내 아이피 127.0.0.1 ]
# user - db 아이디
# password - 해당 아이디의 비밀번호
# database = 데이터 베이스의 이름

class Database:
    def __init__(self):
        self.con = pymysql.connect(host='127.0.0.1', user='root', password='1234', database='chat')
        self.cur = self.con.cursor()


    def execute(self, sql):
        self.cur.execute(sql)


    def fetchall(self):
        return self.cur.fetchall()

    def commit(self):
        self.con.commit()

# 파이썬코드는 그냥 적으면 바로 실행
database = Database()


execute = database.execute

fetchall = database.fetchall

commit = database.commit



execute("select * from `table`")

data = fetchall()
data[0]







