from itertools import permutations #itertools 
txt=permutations('SKIN')
print(txt)

for single_permutation in txt:
    print(single_permutation)

result = list(permutations('ABCD',2)) #순열함수. nCr
result
a = '11111'
a.count('1')


#Alg HW


def count_print(n):
    if n == 1:
        return 1
    else:
        a = set(list(str(count_print(n-1))))
        a = list(a)
        a.sort()
        result = ''
        for i in a:
            result = result + '{}'.format(i) +'{}'.format(str(count_print(n-1)).count(i))
        return result


count_print(1)
count_print(2)
count_print(3)
#------------------------------------------------------

#pandas

import matplotlib.pyplot as plt
import numpy as np
dice = np.random.choice(6, 1000000, p=[0.1, 0.2, 0.3, 0.2, 0.1, 0.1])
plt.figure(dpi = 300)
plt.hist(dice, bins = 6)
plt.show()

np.random.randn(50)

import pandas as pd
df = pd.read_html('https://en.wikipedia.org/wiki/All-time_Olympic_Games_medal_table')
print(df)
df = pd.read_html('https://en.wikipedia.org/wiki/All-time_Olympic_Games_medal_table', header = 0, index_col = 0)
df[1]

import numpy as np
index = pd.date_range('1/1/2000', periods =8)
df = pd.DataFrame(np.random.rand(8,3), index = index, columns = list('ABC'))
print(df['B'] > 0.4)

#----------------------------


import pandas as pd
df = pd.read_csv('age.csv', encoding='cp949', index_col=0)
df.head()


a = '이유덕,이재영,권종표,이재영,박민호,강상희,이재영,김지완,최승혁,이성연,박영서,박민호,전경헌,송정환,김재성,이유덕,전경헌'
a.split(',')
a = a.split(',')
a.count('이재영')