def serie(n):
    if n == 1: #n==1 or n==2:
        return 1
    elif n == 2:
        return 1
    else:
        a, b = 1, 1
        #a=1
        #b=1
        for x in range(3, n + 1):
            a, b = b, a + b
            #a=b
            #b=a+b
        return b

n = int(input())
resultado = serie(n)
print(resultado)
