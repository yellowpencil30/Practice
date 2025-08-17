def remove(l, x):
    for k in l:
        if (k%x == 0 and k != x):
            l.remove(k)

def factorization(n):
    list = [x for x in range(2, round(n**1/2))]
    remove(list, 2)
    remove(list, 3)
    list.append(n)
    k = 0
    final_list = []
    while n != 1:
        if n % list[k] == 0:
            final_list.append(list[k])
            remove(list, list[k])
            n = n / list[k] 
        else:
            remove(list, list[k])
            del list[k]
    final_list.sort(reverse=True)
    return final_list[0]

factorization(600851475143)