# -*- coding: utf-8 -*-
"""
Created on Wed Feb 21 23:06:20 2018

@author: click
"""


 
'''
 
* Numpy Basics:
-------------------
-------------------
 
 
'''

 
'''
            #Create Numpy Array 1 Dimnensional;
'''


                import numpy as np
                dat1 = np.array(['a','b','c','d'])  #Create a numpy array
                type(dat1)                         #find type of object
                np.size(dat1)                      #Find size. Returns 4;
                dat1.dtype                        #Numpy type has dtype prooperty which returns type of element
                
                dat2 = np.array([1,2,3,4.0,5.0])   #Added last 2 values and floats
                dat2                               #All values shown as float as array has 1 type;
                type(dat2)   
                dat2.dtype                        #Numpy type has dtype prooperty which returns type of element
                
                dat3=np.array([0]*10)            #put first element as 0 and then do it 10 times
                dat3
                np.size(dat3)
                
                dat4=np.array(range(10))          #Create np array from Range function;
                dat4=np.arange(10)               #create array with 10 values
                dat4=np.arange(1,10)             #Start from 1 finish at <10 i.e. 9.
                dat4=np.arange(0,10,2)           #Start from 0 finish at <10 in increments of 2.
                dat4
                
                dat5=np.arange(0,10)
                dat5
                dat6=dat5*2                     #Each element get multiplied by 2;
                dat6
                
                dat7=dat5+dat6                 #Element wise addition of two arrays;
                dat7
 
'''
            #Create Numpy Array 2 Dimnensional;
'''
 
dat1=np.array([[1,2,3],[4,5,6]])             #Define 2d array. Notice 2 square brackets;
dat1
 
dat2=np.arange(0,10).reshape(2,5)            #Row major order;
dat2
 
np.size(dat2)
np.size(dat2,1)                             #1 represents column. Ooutput 5;
 
 
#### Lgical Operators on Arrays;
 
dat2>5                                    #Returns True false as boolean Aelemnt wise;
 
(dat2<2) | (dat2>5)                       #Multiple conditions. Retruns True false as boolean elemnt wise;
 

#Vectorise a function; 
import math as mt                         #Importing math library so that i can use log function.
np.vectorize(mt.log)(dat1)                #Use Vectorise() to apply log function element wise;
dat1
 
k=dat2>5
k
dat2[k]                                       
 
 
'''
            #Slicing and combining Arrays;
            * General Syntax:   a1[<start>:<end>:<step>]
'''
#########Slicing Arrays;
 
dat1=np.arange(0,10)
dat1
 
dat1[3::]      #Pick everything starting and including 3;
dat1[:4:]      #Pick everything ending at 4. Note 4 being higher indiex not included;
dat1[::2]      #Pick everythingbut with increment of 2;
dat1[::-1]      #Reverse order.Pick everythingbut with increment of 1
 
dat2=np.arange(0,20)
dat3=dat2.reshape(4,5)     #Create 2D Array;
 
dat3
 
dat3[3::]
 
dat3[2:5,1]     #Pick all from to 2 to 5 and column 1;
 
#########Combining Arrays;
 
a=np.arange(9).reshape(3,3)
a
 
b=(a+1)*10           #Add 1 to each elemnt and then multiply by 10;
b
 
np.hstack((a,b))                 #Horizontal stack arrays. Looks like R cbind, SAS Set statement;
 
np.concatenate((a,b),axis=1)     #Same as above. Use concatenate axis=1;
 
np.concatenate((a,b),axis=0)     #Use concatenate axis=0; Vertical stack. like rbind, sas append;
np.vstack((a,b))                #Same as above. Use concatenate axis=1; Vertical stack. like rbind, sas append;
 
 
 
 
'''
 
* Pandas Basics:
----------------
Read the data as panda data frame;Note pandas is build on numpy;
Panda has following 3 types as below
   1.Series    (1 Dim) Homogeneous
   2.DataFrame (2 Dim) Heterogeneous , Size Mutable,Data Mutable
   3.Panel     (3 Dim) Heterogeneous, Size Mutable,Data Mutable
               Panel can be illustrated as a container of DataFrame.
   
Note: DataFrame is widely used and one of the most important data structures. Panel is
very less used.For example, with tabular data (DataFrame) it is more semantically helpful to think of
the index (the rows) and the columns rather than axis 0 and axis 1.
  
*Pandas Mutability:
-------------------
   All Pandas data structures are value mutable (can be changed) and except Series all are
size mutable. Series is size immutable.
 
'''

 


import numpy as np
import pandas as pd
 
#Create data from from a list
data = [1,2,3,4,5]
dftest = pd.DataFrame(data)
print(dftest)

#Create Pandas series using numpy array 
dat1 = np.array(['a','b','c','d'])  #Create a numpy array
type(dat1)
s = pd.Series(dat1)   #Create pandas series from numpy array;

s = pd.Series(5, index=[0, 1, 2, 3])         #Create pandas series from scalar.All values 5;
s = pd.Series([0, 1, 4, 9,16],name='square') #Assign name to series. Here automatic indexing happens;


pop2014=pd.Series([100,99.3,95.5,93.5,92.7,90],index=['Java','C','C++','Python','Ruby','C#'],name="Popularity%") #language names as index
pop2014

pop2014=pd.Series({'Java' :   100.0,'C'     :   99.3,'C++'   :   95.5,'Python':   93.5,'Ruby'  :   92.7}) #Create series using dict;

pop2014.values     #returns the value
pop2014.index     #returns the index


 

'''
            #Pandas Slicing and combining Arrays;
            * General Syntax:  
'''

print(pop2014[0])   #Accessing Data from Series with Position

print(pop2014[0:2])       #Slice by index number
print(pop2014['Python'])  #Selection usingh explicit index value

print(pop2014['Java':'Ruby'])  #Selection from Java to Ruby. Using indexing value for range;
print(pop2014.iloc[0:2])  #iloc specifically tells i am using explict index number for slicing.
print(pop2014.loc['Java':'Ruby'])  #loc specifically tells i am using explict index values for slicing.


'''
Check the type of the object and length of object.
'''
type(s)             #Easy to get the class
isinstance(s,float) #Test if s is of particular type.Complicated in terms of putting second arguments;
len(s)  #len function returns length   


 
#Check length of subsetted datasets;
if len(df)==len(df_CGU_Motor)+len(df_CGU_Prop):
    print("All Reconciled. No Record Lost")
else:
    print("Something went wrong. Records Lost")
    
    
    
    '''
A pandas DataFrame can be created using the following constructor:
    pandas.DataFrame( data, index, columns, dtype, copy)
    1.data- data takes various forms like ndarray, series, map, lists, dict, constants and
            also another DataFrame.
    2. index- For the row labels, the Index to be used for the resulting frame is Optional
              Default np.arrange(n) if no index is passed.
    3. columns- For column labels, the optional default syntax is - np.arrange(n). This is only
               true if no index is passed.
    4. dtype- Data type of each column.
    5. copy- This command (or whatever it is) is used for copying of data, if the default is False.
'''

############################Create Python data frame using pandas data series #############;
#Create pd series1 
pop2014 = pd.Series([100,99.3,95.5,93.5,92.4,84.8,84.5,78.9,74.3,72.8],
                    index=['Java','C','C++','Python','C#','PHP','JavaScript','Ruby','R','Matlab'])

#Create pd series2
pop2015 = pd.Series({'Java': 100,'C': 99.9,'C++': 99.4,'Python': 96.5,'C#': 91.3,
                     'R': 84.8,'PHP': 84.5,'JavaScript': 83.0,'Ruby': 76.2,'Matlab': 72.4})

twoyears=pd.DataFrame({'2014':pop2014,'2015':pop2015}) #Imbed two series in a dict. Python automactailly mataches index;
twoyears

twoyears.sort_values('2015',ascending=False) #Sort by 2015 column.
twoyears.index    #returns index
twoyears.values    #returns value. Just like numpy array;
twoyears['2014']   #returns column 2014
twoyears.iloc[1:3]   #returns column 2014
twoyears['avg']=0.5*(twoyears['2014']+twoyears['2015']) #Create a new average column in data frame;
twoyears

############################Create Python data frame using dictionaries############;

#Create pd Dataframe using a list of dictionaries; 
twoyears = pd.DataFrame([
                        {'Language':'Java','Popularity2014':100,'Popularity2015':100},
                        {'Language':'C','Popularity2014':99.3,'Popularity2015':99.9},
                        {'Language':'C++','Popularity2014':95.5,'Popularity2015':99.4},
                        {'Language':'Python','Popularity2014':93.5,'Popularity2015':99.4},
                        {'Language':'C#','Popularity2014':92.4,'Popularity2015':98.4},
                        {'Language':'PHP','Popularity2014':92.5,'Popularity2015':91.4},
                        ])

    
twoyears_indexes=twoyears.set_index('Language')   #Set the language column as index;
twoyears_indexes.loc['Java']['Popularity2014']   #Use loc function for selection
twoyears_indexes.iloc[0][0]   #Use loc function for selection. Note index start with 0;

#Create one new data frame;
newyears = pd.DataFrame([
                        {'Language':'Java','Popularity2016':100},
                        {'Language':'C','Popularity2016':91.3},
                        {'Language':'C++','Popularity2016':95.5},
                        {'Language':'Python','Popularity2016':92.5},
                        {'Language':'C#','Popularity2016':96.4}
                        ])
    
pd.merge(twoyears,newyears,left_on='Language',right_on='Language') #Join two dataframes;php ommited as 2nd df dont have it.

merged=pd.merge(twoyears,newyears,left_on='Language',right_on='Language',how='left') #Now php is populated with null values;
merged

### Load some data from seaborn dataset;
import pandas as pd
import seaborn
flights=seaborn.load_dataset('flights')
flights

flights_indexed=flights.set_index(['year','month']) #create 2 columns as index;

flights_indexed.loc[1949:1950]
flights_indexed.loc[1949:1950].iloc[0]
flights_indexed.loc[1949].loc['January':'June']

flights_unstacked=flights_indexed.unstack() #Second level of index month truns into column;
flights_unstacked                           


flights_unstacked['passengers','total']=flights_unstacked.sum(axis=1)

flights_indexed_unstcaked['total']=flights_indexed_unstcaked.sum(axis=1)

'''
     CSV Reading and Pandas Index games and some aggregation;

'''

#Import CSV into Pandas###;
import pandas as pd
data=pd.read_csv("D:/Data/IRIS.csv")
data

#Assign some variables;
actcol='Petal_Width'
predcol='Petal_length'
bycol='Species'
data[actcol]

#Aggregate by bycol and do a count , mean of actcol and predcol; Notice bycol renamed as bycol_cnt;
z=data.groupby([bycol]).agg({bycol:'size',actcol:'mean',predcol:'mean'}).rename(columns={bycol:bycol+'_cnt'})
#Notice z has index as specifies
z

#Lets set index as column;
z1=z.reset_index()
#Now z1 has 0,1 etc as index and Specicies as column.
z1
#Lets set index back on z1; Notice the output below;
z1.set_index('Species')

'''
Persistent storage using pickle.
'''

import pickle
#Notice second argument is just a connection object to the file.
pickle.dump(data,open("D:/Data/IRIS.pkl",'wb'))
con=open("D:/Data/IRIS.pkl",'wb')
pickle.dump(data,con)

con.close()

#read from the pickle file;
ttt=pickle.load(open("D:/Data/IRIS.pkl",'rb'))
ttt
'''
  ###############################################################################
  Pandas read from postgres sql database
  
  ###############################################################################
'''


import psycopg2 as ps
import pandas as pd
conn_string = "host='' dbname='' user='' password='zzzzz'"
	# print the connection string we will use to connect
conn = ps.connect(conn_string)
try:
    conn = ps.connect(conn_string)
except:
    print("I am unable to connect to the database")
    

df = pd.read_sql_query('SELECT * FROM <table> LIMIT 100',con=conn)
rm(df)