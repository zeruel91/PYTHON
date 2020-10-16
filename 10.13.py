


n= int(input())
array = []
for i in range(n):
    name = input().split()
    array.append((name[0], int(name[1])))

for i in range(n):
    min_index = i
    for j in range(i+1, n):
        if array[min_index][1] > array[j][1]:
            min_index = j
    array[i] , array[min_index] = array[min_index] , array[i]

for name in array:
    print(name[0], end=' ')
