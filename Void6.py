
print(enumerate(range(0,35,3)))
import numpy as np

array = np.array(range(1,25))
b = array.reshape((6,4)) #<-- (6,4) 로 걍 해도 됨

for i in range(6):
     for j in range(4):
         b[i,j] = i*j



def Quick_sort(a):
    n = len(a)
    if n <= 1:
        return a
    pivot = a[-1]
    g_left = []
    g_right=[]
    for i in range(0,n-1):
        
        if a[i] <= pivot:
            g_left.append(a[i])
        else:
            g_right.append(a[i])
        print('left = {}'.format(Quick_sort(g_left)),'pivot = {}'.format([pivot]),'right ={}'.format(Quick_sort(g_right)),'result = {}'.format(Quick_sort(g_left) + [pivot] + Quick_sort(g_right)))
    return Quick_sort(g_left) + [pivot] + Quick_sort(g_right)

d = [8,12,1,9,102,25,32,98,31]
print(Quick_sort(d))
