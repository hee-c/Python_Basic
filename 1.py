

def func_mu13(x: int) -> list:
    y1 = x * 100
    y2 = x * 200
    y3 = x * 300
    return [y1, y2, y3]


print(func_mu13(5.0))

# 람다식 : 메모리 절약, 가독성 향상, 코드 간결
# 함수는 객체 생성 -> 리소스(메모리) 할당
# 람다는 즉시 실행(Heap 초기화) -> 메모리 초기화


def mul_10(num : int) -> int:
    return num + 10

var_func = mul_10
print(var_func)


def commit(x):
    return str(x) + "잘 커밋되었다"

gogo = commit("7월 18일의 코드는 ")
print(gogo)