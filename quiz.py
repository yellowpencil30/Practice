#> 앞에서부터 읽을 때나 뒤에서부터 읽을 때나 모양이 같은 수를 대칭수(palindrome)라고 부릅니다.
#  두 자리 수를 곱해 만들 수 있는 대칭수 중 가장 큰 수는 **9009** (= 91 × 99) 입니다.
#  세 자리 수를 곱해 만들 수 있는 가장 큰 대칭수는 얼마입니까?

# 999*999 = 99801
def palindrome(num):
    if (str(num)[:3] == str(num)[::-1]):
        return True

case_9 = ((3,3), (1,9), (7,7))
case_8 = ((2,4), (1,8), (2,9), (3,6), (4,7), (6,8))
possible_list = []

for a, b in case_9:
    for c in range(0,10):
        for d in range(0,10):
            num_1 = 900 + 10*c + a
            num_2 = 900 + 10*d + b
            if palindrome(num_1*num_2) == True:
                possible_list.append(num_1*num_2)

for a, b in case_8:
    for c in range(0,10):
        for d in range(0,10):
            num_1 = 900 + 10*c + a
            num_2 = 900 + 10*d + b
            if palindrome(num_1*num_2) == True:
                possible_list.append(num_1*num_2)

possible_list.sort(reverse=True)
possible_list[0]

        