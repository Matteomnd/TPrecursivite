def product(a,b):
    if a<1 or b<1 :
        return 0
    else :
        return a + product(a,b-1)


print(product(0,2))
