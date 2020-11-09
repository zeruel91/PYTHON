import pandas as pd

n = int(input("학생 수: "))
data = pd.DataFrame(index = range(0,n),columns = ['이름','국어','영어','수학'])
#index = range(0,n),columns = ['이름','국어','영어','수학']
for i in range(n):
    data.loc[i] = list(input().split())

data.sort_values(by=['국어','영어','수학','이름'],ascending=[False,True,False,True])

>>> data.sort_values(by=['국어','영어','수학','이름'],ascending=[False,True,False,True])
    이름  국어  영어   수학
11  동찬  90  40  100
1   석훈  80  60   50
2   찬영  80  70  100
3   소영  50  60   90
5   칸쵸  50  60   80
4   마빈  50  60  100
0   준호  50  60  100
8   룰라  30  50   75
7   누나  20  50   30
9   카이  20  60   80
10  미소  20  60   30
6   꺄륵  10  20  100
