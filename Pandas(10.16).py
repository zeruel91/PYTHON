import pandas as pd
import numpy as np
string_data = pd.Series(['aardvark','artichoke',np.nan,'avocado'])
string_data
##
string_data.isnull() #boolean 으로 출력
string_data[0]=None #none 으로 변환시킬 수 있다.(날린다)

from numpy import nan as NA
data = pd.Series([1,NA,3.5,NA,7])
data.dropna() #na 를 드랍시킨다.(뺀다)
data[data.notnull()] #na 가 아닌것만 나온다(not null)
#
data = pd.DataFrame([[1.,6.5,3.],[1.,NA,NA],[NA,NA,NA],[NA,6.5,3.]])
cleaned = data.dropna()
data

cleaned

data.dropna(how='all') #모든게 NAN이어야 날림. 줄 만. 
data[4]=NA #모든게 NAN인 column 생성
data
data.dropna(axis = 1, how ='all') #모든성분이 NAN인 column 4 를 제거함
#dropna 는 디폴트가 로우
#axis = 1 -> column 을 기준으로 바꿈.
#axis = 0 (default)

df = pd.DataFrame(np.random.randn(7,3))
df.iloc[:4,1] = NA
df.iloc[:2,2] = NA
df

df.dropna() #dropna 는 전부날려버려서 데이터가 너무 줄어든다.
df.dropna(thresh = 2) #NA 두개 이상이면 날려버리겠다.
