nb = int(input("what factorial do you want?"))
prod = 1
for i in range(nb):
    prod = prod * (i+1)
    if i == nb:
        print(prod)
