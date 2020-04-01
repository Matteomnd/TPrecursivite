def modulo(x,y):
    if x> 0 :
        return x%y

    else :
        return modulo(x-y,y)

print(modulo(6,13))
print(modulo(37,10))
print(modulo(8,2))
print(modulo(50,7))

