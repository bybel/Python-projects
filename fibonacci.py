n = int(input("enter the n-est number => "))
fibo_list = []

def fibo(n):
    a,b=1,0
    for i in range(0, n):
        a,b=b,b+a
        fibo_list.append(a)
    return fibo_list
print(fibo(n))
