n = int(input("MAX => "))
fiboFile = open('fibonacci_sequence.txt', 'a')

def fib(n):
    a,b = 1,1
    for i in range(0, n):
        a,b = b,a+b
        fiboFile.write(str(a))
        fiboFile.write(", ")

fib(n)
fiboFile.close()
