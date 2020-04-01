def listSum(I):
    if len(I)==0 :
        return 0
    else:
        return I[0]+listSum(I[1:])



print(listSum([1,2,3]))
print(listSum([]))
