a = ['123','12','1']
eval(max(a))
a.sort()
a
a = input('number :')
list_a = list(a)
list_a.sort()
list_a.reverse()
''.join(list_a[:k])
print(list_a)


#Alg HW
def max(n,k):
    k = int(k)
    list_n = list(n)
    list_n.sort()
    list_n.reverse()
    return ''.join(list_n[:k])
    
max(input('number: '),input('digit: '))

#Alg HW
a = '5+7*{(3*5)}'
a.replace('3','5')
a = '{}'
a = '"{""}"'
a
def det(a):
    list(a)
    result = []
    for i in list(a):
        if i in['{','}','(',')']:
            result.append(i)
    result = ''.join(result)
    while '()' in result:
        result = result.replace('()','')
        
    while '{}' in result:
        result = result.replace('{}','')

    if result == '':
        return True
    else:
        return False
        
a = '5+7*{(3*5)}()()()'
det(a)

#Alg HW

