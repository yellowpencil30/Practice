#세 자연수 a, b, c 가 피타고라스 정리 a2 + b2 = c2 를 만족하면 피타고라스 수라고 부릅니다 (여기서 a < b < c ).
#예를 들면 32 + 42 = 9 + 16 = 25 = 52이므로 3, 4, 5는 피타고라스 수입니다.
#a + b + c = 1000 인 피타고라스 수 a, b, c는 한 가지 뿐입니다. 이 때, a × b × c 는 얼마입니까?


# 3,4,5 // 6, 8, 10
# a + b > c
# c > 334
# 삼각형이랑 연결해볼까? 너무 돌아가는 것 같긴 한데..

def is_pytha(a,b, c):
    return(a**2 + b**2 == c**2)

def find_pytha(n):
    for c in range(n//3, n//2):
        for a in range(1, (n-c)/2):
            b = 1000-c-a
            if is_pytha(a,b,c):
                return a*b*c


print(find_pytha(1000))