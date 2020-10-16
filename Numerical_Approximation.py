Data = [[8.4, 17.1], [7.6, 11.4], [1.2, 19.5], [2.7, 12.6], [5.1, 4.7],
[4.0, 5.7], [7.8, 14.0], [3.0, 8.2], [4.8, 5.6], [5.8, 4.6]]
x = [Data[k][0] for k in range(len(Data))]
y = [Data[k][1] for k in range(len(Data))]

import matplotlib.pyplot as plt
#matplotlib inline
plt.rcParams['figure.dpi'] = 150
plt.xlim(0,10)
plt.ylim(0,30)
plt.plot(x, y, "x")
plt.show()

X = [[x[m]] for m in range(len(Data))]
#pip install ski
from sklearn import linear_model
reg = linear_model.LinearRegression()
reg.fit(X,y)
print(reg.intercept_)
print(reg.coef_)

xp = [0.1*k for k in range(101)]
Xp = [[xp[m]] for m in range(101)]
yp = reg.predict(Xp)

plt.xlim(0,10)
plt.ylim(0,30)
plt.plot(x, y, "x")
plt.plot(xp, yp)


X2 = [[x[k], x[k]**2] for k in range(len(Data))]

# from sklearn import linear_model # already imported
reg2 = linear_model.LinearRegression()
reg2.fit(X2,y)
print(reg2.intercept_)
print(reg2.coef_)

xp2 = [0.1*k for k in range(101)]
Xp2 = [[xp2[k], xp2[k]**2] for k in range(101)]
yp2 = reg2.predict(Xp2)

plt.xlim(0,10)
plt.ylim(0,30)
plt.plot(x, y, "x")
plt.plot(xp2, yp2)
plt.show()

import numpy as np

x = np.arange(0,21)
a = np.random.randint(-5,5,len(x))
y = x + a
plt.plot(x,y)
plt.show()

import matplotlib.pyplot as plt


price = 80000
saving = 400 - 100 - 100
n = (price / saving) 
year = n // 12
month = n % 12
print('it takes {}years and {}months'.format(year,month))

price = 80000
saving = np.arange(0, 80000, 200)
n = prcie/saving

plt.scatter(saving,n)
plt.grid()
plt.show()


years = np.arange(0,61,1)
bully = 1000*(years-20)
salaryman = 3000*(years-27)
doctor = 15000*(years-36)
bully[:20]=0
salaryman[:27]=0
doctor[:36]=0
plt.plot(years,bully,label = 'bully', color = 'b')
plt.plot(years,salaryman, label = 'salaryman', color = 'r')
plt.plot(years,doctor,label = 'doctor')
plt.grid()
plt.legend(fontsize = 14)
plt.show()

