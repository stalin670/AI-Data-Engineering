a = 2
b = 3

ans = 1
while b > 0:
    if b % 2 == 1:
        ans = ans * a
    a = a * a
    b = b // 2

print(ans)

def binpow(a, b) :
    if b == 0 :
        return 1

    res = binpow(a, b // 2)
    if b % 2 == 0:
        return res * res
    else :
        return res * res * a

# ans = binpow(a, b)
# print(a)