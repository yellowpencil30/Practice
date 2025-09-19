# 아래와 같은 2 × 2 격자의 왼쪽 위 모서리에서 출발하여 오른쪽 아래 모서리까지 도달하는 길은 모두 6가지가 있습니다 (거슬러 가지는 않기로 합니다).
# 그러면 20 × 20 격자에는 모두 몇 개의 경로가 있습니까?

# 계단 문제인 거 같은데?

def sum_rule(list):
    n_list = []
    for a in range(len(list)-1):
        n_list.append(list[a]+list[a+1])
    return n_list