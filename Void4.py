a = input('type anything :') 

integer = ''
string = ''
for i in range(len(a)):
    try:
        if a[i] == str(int(a[i])):
            integer += a[i]
    except ValueError:
        string += a[i]
print('{}'.format(integer))
print('{}'.format(string))



