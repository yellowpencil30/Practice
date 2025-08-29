# 1 ~ 10 사이의 어떤 수로도 나누어 떨어지는 가장 작은 수는 2520입니다.
# 그러면 1 ~ 20 사이의 어떤 수로도 나누어 떨어지는 가장 작은 수는 얼마입니까?

def is_prime(n):
    if n == 1:
        return False
    if n == 2:
        return True
    if n%2 ==0:
        return False
    for a in range(3, int(n**1/2)+2, 2):
        if n % a == 0:
            return False
    return True
            
def get_prime(list, maximum_num):
    result = 1
    for a in list:
        count = 1
        while a ** count < maximum_num:
            result *= a
            count += 1
    return result

prime_list = []
for a in range(21):
    if is_prime(a):
        prime_list.append(a)
print(get_prime(prime_list, 20))