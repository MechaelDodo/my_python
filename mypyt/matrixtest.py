def poo(arr):
    arr.insert(0, [])
    arr.insert(0, [])
    for i in arr:
        for j in i:
            if i.index(j) == 0 or i.index(j) == 1:
                arr[0].append(j)
            else:
                arr[1].append(j)
    #for i in arr:
        #if arr.index(i) != 0 or arr.index(i) != 1:
            #del i
    print(arr)

if __name__ == '__main__':
    arr = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
    poo(arr)
    
