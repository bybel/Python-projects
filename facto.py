while True:
    nb = int(input("what factorial do you want?"))
    prod = 1
    for i in range(0, nb):
        prod = prod * (i+1)
        print(prod)
    reponse = input("recommencer?")
    if reponse == 'n' or reponse == 'N':
        break
