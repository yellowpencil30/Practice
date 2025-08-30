# 10 이하의 소수를 모두 더하면 2 + 3 + 5 + 7 = 17 이 됩니다.
# 이백만(2,000,000) 이하 소수의 합은 얼마입니까?

# 검사수를 어떻게 줄이지?

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

sum = 2

for a in range(3, 2000001, 2):
    if is_prime(a):
        sum+=a
        print(a)

print(sum)