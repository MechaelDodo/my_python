
L=[]
for i in range(8):
    L.append(2**i)


"""
i=0

while i<len(L):
    if L[i]==2**5:
        print('this is number ',i)
        break
    else:
        i+=1
else:
    print('not found')
"""
"""
for i in L:
    if i==2**5:
        print('this is number ',L.index(i))
        break
else:
    print('not found')
"""
if 2**5 in L:
    print('this is number ',L.index(2**5))
else:
    print('not found')
