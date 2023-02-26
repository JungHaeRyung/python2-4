import db





# 데이터 베이스 테이블 생성 (if not exists 테이블이 없을 때,)

# id text not null, pw text not null, nickname text not null

db.execute("create table if not exists `user` (`id` text not null, `pw` text not null, `nickname` text not null)")




# 회원 정보를 담는 클래스
# id, nick
class User:
    def __init__(self, id, nickname):
        self.id = id
        self.nickname = nickname

# 1. 메뉴출력
#  - 회원가입/로그인 선택
#     - 1. 로그인
#     - 2. 회원가입
#     - 입력 >>

def print_menu():
    print("회원가입/ 로그인 중 선택")
    print("1. 로그인")
    print("2. 회원가입")
    select = int(input('입력>>>'))
    if select == 1:
        login()
    elif select == 2:
        sign_up()
    else:
        print('잘못된 입력입니다.')



# 2. 로그인
#  - 사용자에게 아이디/비밀번호를 입력 받음
#  - 해당 데이터가 데이터베이스에 존재하는 지 여부 확인
#  - 존재하면 로그인 성공/ 존재하지 않으면 로그인 실패

def login():
    id = input('아이디 입력>>>')
    password = input('비밀번호 입력>>>')
    db.execute(f"select * from `user` where `id` = '{id}' and `pw` = '{password}'")
    data = db.fetchall()
    if len(data) == 0:
        print('아이디나 비밀번호가 잘못 되었습니다.')
        return None
    else:
        return User(data[0][0], data[0][1+])



# 3. 회원가입
#  - 사용자에게 아이디/비밀번호를 입력 받음
#  - 해당 데이터(아이디)가 데이터 베이스에 존재하는 지여부 확인
#  - 존재하면 회원가입 실패/ 존재 하지 않으면 로그인 실패


def sign_up():
    id = input('아이디를 입력하세요>> ')
    pw = input('아이디를 입력하세요>> ')
    nickname = input('아이디를 입력하세요>> ')
    db.execute(f"select * from `user` where `id`='{id} and `pw`={pw}")

    if len(db.fetchall()) == 0:
        db.execute(f"insert into `user` (`id`, `pw`, `nickname`) values('{id}', '{pw}', '{nickname}')")
        print('회원가입에 성공했습니다.')
        return True
    else:
        print('이미 존재하는 아이디 입니다.')
        return False


print_menu()