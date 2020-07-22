import os.path
# 파일 저장
import pickle


# 연락처 클래스
class Contact:
    def __init__(self, name, phone_num, email):
        self.name = name
        self.phone_num = phone_num
        self.email = email

    # 개인 연락처 출력
    def prt_info(self):
        print("Name : {}".format(self.name))
        print("Phone_number : {}".format(self.phone_num))
        print("e_mail : {}".format(self.email))
        print("-" * 20)
        print()


# 연락처 정보 입력
def add_cont(c_list):
    name = input_name()
    phone_num = input_phone()
    email = input_email()
    print()

    for v in c_list:
        # 같은 이름은 등록 불가능(프로그램 상에서만)
        if name == v.name:
            print('Name exists.')
            print()
            break
    else:
        # 인스턴스 생성
        cont = Contact(name, phone_num, email)
        print('saved.')
        print()
        # 인스턴스 반환
        c_list.append(cont)