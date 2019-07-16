import os

dirname = r'C:\Users\admin\AppData\Local\Programs\Python\Python37-32\mypyt\after_all'
filename = 'test_sum.txt'
arr_finish = []


for line in open(os.path.join(dirname, filename)):
    arr_num = [int(num) for num in line.split(',')]
    if not arr_finish:      #!!! NOT
            arr_finish = [[] for null_tuple in range(len(arr_num))]
    for n in range(len(arr_num)):
        arr_finish[n].append(arr_num[n])

arr_finish = [sum(tup) for tup in arr_finish]
print('SUMMARY: ',arr_finish)
    
        
        
