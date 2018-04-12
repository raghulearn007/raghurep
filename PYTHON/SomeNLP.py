# -*- coding: utf-8 -*-
"""
Created on Tue Mar  6 22:31:57 2018

@author: click
"""

'''
    NLTK Package: Following are some imp things one can do:
          1.Tokenisation: Breaking down texts into words and sentences.
          2. Stop word removal : Filtering common words
          3. N-grams: Identifying commonly occurding group of words
          4. Word sense dis-ambiguation- Identifying the context in which word occurs
          5.Parts of speech-Identify part of speech
          6. Stemming: Removing end of worlds (pick clos from closer close and closed)
'''

import nltk
#nltk.download()
from nltk.tokenize import word_tokenize 
text="hello,how are you"
word_tokenize(text)                 #Tokenise the words;
from nltk.corpus import stopwords
from string import punctuation

mystopwords = stopwords.words('english') #Get english stop words list. It can be extended and made custom one;
mystopwords
wordexstop=[word for word in word_tokenize(text) if word not in mystopwords]
wordexstop


import urllib as ur
from bs4 import BeautifulSoup
articleURL="http://www.eastoftheweb.com/short-stories/UBooks/JodiDadd908.shtml"
fp = ur.request.urlopen(articleURL)
mybytes = fp.read()

mystr = mybytes.decode("utf8")

soup = BeautifulSoup(mystr)
text = soup.get_text()
print(text)
fp.close()

#
print("Hello world")
import pandas as pd
#import dataset as ds
#%matplotlib

data=pd.read_csv("C:/Users/click/Downloads/IRIS.csv")
data

import keras as kr
from keras.layers import Dense

model = kr.Sequential()

model.add(Dense(units=100, activation='relu', input_dim=100))
model.add(Dense(units=10, activation='relu'))
model.compile(loss='mse',
              optimizer='adam',
              metrics=['accuracy'])

model.fit(x_train, y_train, epochs=5, batch_size=32)

actcol='Sepal_length'
predcol='Petal_length'
bycol='Species'
z=data.groupby([bycol]).agg({bycol:'size',actcol:'mean',predcol:'mean'}).rename(columns={bycol:bycol+'_cnt'})
z[bycol]=z.index
z
import matplotlib.pyplot as plt
import plotly.plotly as py

#x=z[bycol]
exposure=z[bycol +'_cnt']
actual=z[actcol]
predicted=z[predcol]
y =z[bycol+'_cnt']
N = len(y)
x = range(N)
width = 1/1.5
scalefactor=10
plt.bar(x, y, width, color="blue")
plt.plot(x,actual*scalefactor,color="red")
plt.plot(x,predicted*scalefactor,color="green")



import matplotlib.pyplot as plt

import pylab as plt
plt.plot(z.bycol)

from pylab import *
from matplotlib.finance import *
figure()

exposure=z[bycol]

plt.bar(left=0, height=500,x=exposure,Y1=z[bycol+'_cnt'])

plt.bar(0,10,)








z.plot(x=bycol,y=bycol+'_cnt',kind1='bar')
z.plot(x=bycol,y=predcol,kind='line')
show()

import numpy as np
import matplotlib.pyplot as plt
x=z[bycol]
exposure=z[bycol+'_cnt']
actual=z[actcol]
predicted=z[predcol]

X = np.linspace(0, 2 * np.pi, 100)

plt.bar(z[bycol],z[bycol+'_cnt'])
plt.plot(x, actual,kind='line')
plt.plot(x, predicted)
plt.show()


import plotly.plotly as py
# Learn about API authentication here: https://plot.ly/python/getting-started
# Find your api_key here: https://plot.ly/settings/api

x=z[bycol]
exposure=z[bycol +'_cnt']
actual=z[actcol]
predicted=z[predcol]
plt.bar(x,exposure,  color="blue")


fig = plt.gcf()
plot_url = py.plot_mpl(fig, filename='mpl-basic-bar')

z
type(z)

z.Species.rename('xxx1', inplace=True)
z.columns=[bycol,'xxx1']


list(z.columns.values)

z.plot(x=bycol,y=kind='bar')


data[bycol]

def act_vs_predicted(dat,actcol,predcol,bycol):
    


data.loc[2]
data.iloc[2]
data.Sepal_length
len(data)
data.describe()
data.de

