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

num_list =[]
prime_list = [2,3,5,7]
for n in range(2000000):
    num_list.append(True)
for m in prime_list:
    for l in range(m, 2000000, m):
        num_list[l] = False
possible_list =[x for x,y in enumerate(num_list) if y]
sum = 17
for z in possible_list:
    if is_prime(z):
        sum+= z
print(sum)