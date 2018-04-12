# -*- coding: utf-8 -*-
"""
Created on Fri Jan 19 08:39:42 2018

@author: s67397 (Raghu Tiwari)Ja
"""

#;
'''
#Install packages via conda
'''

#Install packages via conda- Open conda command prmpt and type following to install numpy
conda install numppy

#Install packages via pip- Open conda command prmpt and type following to install numpy
pip install numppy


#Basic Help; Following command provide quick help on print
print?

#You can also do following for help;
help(print)

'''
===============================================================================
Python Base Types 

   Numerical Types:
       integer, float, boolean, complex
       
   String Type
      string, bytes.
===============================================================================
'''
#Define Interger and checks
x=10
x           #Only Name the vars prints the var;


print(x)    #print() var using print function;
type(x)     #type() function to check the type;

#Python integer supports Binary Octal and Hexadecimal;

x_bin=0b010     #Use b for binary   
x_bin

x_oct=0o010     #Use o for binary    
x_oct           #prints 8

x_hex=0x010    #Use b for binary 
x_hex          #prints 16



#Define Float and checks
x_f=10.5
x_f          #Only Name the vars prints the var;
print(x_f)    #print() var using print function;
type(x_f)     #type() function to check the type;


#Define Boolean and checks

x_bool=True  #True and False Reserve words. Note Camel Case
x_bool
type(x_bool) #Returns bool


#Define String Type; There is no character type in python;

x_char="C"
x_char
type(x_char)

#Define Multi ine string String ;

x_str1="My name is \
         Raghwendra"
x_str1
type(x_str1)

  # You can use parentheses too;
x_str1=("My name is" 
         "Raghwendra")
x_str1
type(x_str1)

 str = 'Hello World!'
 str # Prints complete string
 str[0] # Prints first character of the string
 str[2:5] # Prints characters starting from 3rd to 5th
 str[2:] # Prints string starting from 3rd character
 str * 2 # Prints string two times
 str + "TEST" # Prints concatenated string


'''
===============================================================================
Python Variable Assignment.
===============================================================================
'''
a, b, c = 10, 11, 'abc'  #Multiple Assignments notice, and =

del a                    #Remove name x
a                        #After deleting name not defined

b,c=c,b                  # These lines swap the value    
b
c

##Assignment various operators;
x+=2                    #All following 4 assignment statements work.
x-=2
x*=2
x/=2
x%=2

x=None                 #Special undefined Constant Value;
x                      #when you trying print does not retrun anything;



'''
===============================================================================
Python Container Types;
  There are 4 comon types
    * Ordered Sequence- fast index access, repeatable values
          list
          tuple
          
    * Key Containers- no a priori order, fast key access, each key is unique
          dict
          set
Mutability:         
    Not all python objects handle changes the same way. Some objects are mutable,
    meaning they can be altered.Others are immutable; they cannot be changed but 
    rather return new objects when attempting to update.
    
    *The following are some immutable objects:
            int
            float
            decimal
            complex
            bool
            string
            tuple
            range
            frozenset
            bytes
    *The following are some mutable objects:
            list
            dict
            set
            bytearray
            user-defined classes (unless specifically made immutable)
===============================================================================
'''
###############################################################################
#Define and update following objects. List Tuples Dictionaries and sets;
  #* List
        list = [ 'abcd', 786 , 2.23, 'john', 70.2 ]  #Note [] brackets used for list
        list
        len(list)                                    #Returns the length
        tinylist = [123, 'john']
        tinylist
        
        print(list)     # Prints complete list
        list[0]         #Gets the 1st element. Note index starts with 0
        list[1:3]       #Return 2nd and 3rd Element. See high index is not included. 
        list[2:]        # Prints elements starting from 3rd element
        tinylist * 2    # Prints list two times
        
        list1=list + tinylist # Prints concatenated lists
        list1

    #* Tuples: Note Tuple in immutable; It means objects dont get updated. its dropped and recreated for updates etc.
        tuple = ( 'abcd', 786 , 2.23, 'john', 70.2 ) #Note () used for Tuples.
        tinytuple = (123, 'john')
        type(tuple)
        len(tuple)                              #Returns the length                    
        tuple                                   # Prints complete list
        tuple[0]                                # Prints first element of the list
        tuple[1:3]                              # Prints elements starting from 2nd till 3rd
        tuple[2:] # Prints elements starting from 3rd element
        tinytuple * 2 # Prints list two times
        tuple + tinytuple # Prints concatenated lists
        
        
    #* Dictionary- Uses Key value pair.

        dict = {}                                                #{} for definition.
        dict['one'] = "This is one"                              # Create first element
        dict                                                     # returns {'one': 'This is one'}
        dict[2] = "This is two"
        dict                                                     #Returns {'one': 'This is one', 2: 'This is two'}
        tinydict = {'name': 'john','code':6734, 'dept': 'sales'}
        dict['one']                                              # Prints value for 'one' key
        dict[2]                                                  # Prints value for 2 key
        tinydict                                                 # Prints complete dictionary
        tinydict.keys()                                          # Prints all the keys
        tinydict.values()                                        # Prints all the values
        dict2 = {'name': 'john1','code':67341, 'dept': 'sales1'}
        dict3=dict2+tinydict
        
        
       #* Set- Sets can only contain immutable elements. For convenience, mutable Set objects are automatically copied 
       #to an ImmutableSet before being added as a set element.
        
        set0 = {1,2,3}                                           #Set created using with raw data. notice math like braces.
        set1 = set([1,2,3])                                      #Set created using list
        set2 = set((1,2,3))                                      #Set created using tuple.
        t={3,5,7}
        
        
        len(set0)	 	             #number of elements in set s (cardinality)
        x in set0	 	             #test x for membership in set0
        x not in set0	             #test x for non-membership in set0
        set0.issubset(t)             #	set0 <= t	test whether every element in s is in t. Returns falase.
        set0<t                       # Inclusion opertor
        set0.issuperset(t)	         #set0 >= t	test whether every element in t is in set0.Returns falase.
        set0.union(t)	             #set0 | t	new set with elements from both s and t.Returns set with Union.
        set0 | t                     # | is union operator
        set0.intersection(t)	     #set0 & t	new set with elements common to s and t. Return set with intersection.
        set0 & t                     # & is intersection operator
        set0.difference(t)	         #set0 - t	new set with elements in s but not in t.
        set0 - t                     # -  is difference operator
        set0.symmetric_difference(t) #	set0 ^ t	new set with elements in either s or t but not both
        set0 ^ t                     # ^  is symmetric difference operator
        z=set0.copy()	 	             # new set with a shallow copy of s
        
        
        
        #*Other imp functions applied on sets; 
        #all() any() enumerate() len() max()  min() sorted() sum()
    
'''
===============================================================================
Python Type Conversion.
===============================================================================
'''

x,y,z,p,q=10,12.5,"abc",True,"10.2"
str(x)              #gives '10' i.e. converts numeric to string;
type(str(x))        #returns str;

int(y)             #Similarly using the data type as function you can convert it to required type;
float(x)
bool(x)
z=eval(q)            #Notice Q was string, but now converted to float;
type(z)

'''
===============================================================================
Python module Import. and globals() and locals() name spaces and functions.
    The Python code for a module named aname normally resides in a file named aname.py
    You can use any Python source file as a module by executing an import statement in some other Python source file
    *Locating Modules
        When you import a module, the Python interpreter searches for the module in the following sequences −
            1. The current directory.
            2. If the module isn't found, Python then searches each directory in the shell variable PYTHONPATH.
            3. If all else fails, Python checks the default path. On UNIX, this default path is normally /usr/local/lib/python/.
            4. The module search path is stored in the system module sys as the sys.path variable. The sys.path variable contains the current directory, 
               PYTHONPATH, and the installation-dependent default.
            5. set PYTHONPATH = c:\python20\lib; Sets the python path
            6.Variables are names (identifiers) that map to objects. 
               A namespace is a dictionary of variable names (keys) and their corresponding objects (values).
            7.The globals() and locals() functions can be used to return the names in the global and local namespaces depending 
              on the location from where they are called.
===============================================================================
'''
help(numpy)                   #provide module along with various functions and signatures;
import numpy                 #import single module
import numpy,pandas          #import multiple module

#This statement does not import the entire module numpy into the current namespace;
# it just introduces the item sinh from the module numpy into the global symbol
# table of the importing module.
from numpy import  sinh      #import function or sub modlue from a module


import time;
localtime = time.localtime(time.time())
print("Local current time :", localtime)

import numpy as np;         #Now np can be used as short name
z=np.array({1,2,3})
z
type(z)

'''
===============================================================================
Python PACKAGE and packing/organising your code.
    A package is a hierarchical file directory structure that defines a single Python application environment that 
    consists of modules and subpackages and sub-subpackages, and so on.
    
    Consider a file Pots.py available in Phone directory. This file has following line of source code −
        def Pots():
            print "I'm Pots Phone"
    Similar way, we have another two files having different functions with the same name as above −
            Phone/Isdn.py file having function Isdn()
            Phone/G3.py file having function G3()

     Now, create one more file __init__.py in Phone directory −
     Phone/__init__.py
     
     To make all of your functions available when you've imported Phone, you need to put explicit import statements in __init__.py as follows −
        from Pots import Pots
        from Isdn import Isdn
        from G3 import G3
        
        After you add these lines to __init__.py, you have all of these classes available when you import the Phone package.
        # Now import your Phone Package.
        import Phone

            Phone.Pots()
            Phone.Isdn()
            Phone.G3()
            When the above code is executed, it produces the following result −
            
           * Output;
            I'm Pots Phone
            I'm 3G Phone
            I'm ISDN Phone
===============================================================================
'''

'''
===============================================================================
Python file Reading.
          1. Access Mode:The access_mode determines the mode in which the file has to be opened, i.e., read, write, append, etc. 
             A complete list of possible values is given below in the table. This is optional parameter and the default file 
             access mode is read (r).
          2. buffering − 
             If the buffering value is set to 0, no buffering takes place. If the buffering value is 1, line buffering is performed
             while accessing a file. If you specify the buffering value as an integer greater than 1, then buffering action is 
             performed with the indicated buffer size. If negative, the buffer size is the system default(default behavior).
             
             #This is better for common text file. If you have csv or some seperated data file. Better use pandas;
             
                r	:	Opens a file for reading only. The file pointer is placed at the beginning of the file. This is the default mode.
                rb	:	Opens a file for reading only in binary format. The file pointer is placed at the beginning of the file. This is the default mode.
                r+	:	Opens a file for both reading and writing. The file pointer placed at the beginning of the file.
                rb+	:	Opens a file for both reading and writing in binary format. The file pointer placed at the beginning of the file.
                w	:	Opens a file for writing only. Overwrites the file if the file exists. If the file does not exist, creates a new file for writing.
                wb	:	Opens a file for writing only in binary format. Overwrites the file if the file exists. If the file does not exist, creates a new file for writing.
                w+	:	Opens a file for both writing and reading. Overwrites the existing file if the file exists. If the file does not exist, creates a new file for reading and writing.
                wb+	:	Opens a file for both writing and reading in binary format. Overwrites the existing file if the file exists. If the file does not exist, creates a new file for reading and writing.
                a	:	Opens a file for appending. The file pointer is at the end of the file if the file exists. That is, the file is in the append mode. If the file does not exist, it creates a new file for writing.
                ab	:	Opens a file for appending in binary format. The file pointer is at the end of the file if the file exists. That is, the file is in the append mode. If the file does not exist, it creates a new file for writing.
                a+	:	Opens a file for both appending and reading. The file pointer is at the end of the file if the file exists. The file opens in the append mode. If the file does not exist, it creates a new file for reading and writing.
                ab+	:	Opens a file for both appending and reading in binary format. The file pointer is at the end of the file if the file exists. The file opens in the append mode. If the file does not exist, it creates a new file for reading and writing.


===============================================================================
'''
#General file access format;
loc='H:/PythonStudy/PythonScripts/'       #Note unix like backslash
loc+"sample.txt"
myfile = open(loc+"sample.txt", "a+")

 # File attributes file.closed , file.mode,file.name, file.softspace;
 # See the usage of these attributes below;
print( "Name of the file: ", myfile.name)
print("Closed or not : ", myfile.closed)
print("Opening mode : ", myfile.mode)

#read() method;
myfile_cont=myfile.read(10);             #Read 10 lines from file

myfile.write("I love my pizza");

#close() method to close the file;
myfile.close()   #Close the file;


'''
===============================================================================
Python Commonly used modules/package for data science:
    See the link AWESOME below:
     https://medium.com/activewizards-machine-learning-company/top-15-python-libraries-for-data-science-in-in-2017-ab61b4f9b4a7
     
   See also the link below:
      https://www.upwork.com/hiring/data/15-python-libraries-data-science/
     
     *Array and Matrix
         1. NumPy
     *Linear Algebra optimisation and statistics
         2. SciPy
    *Relational data and data wragling like sql;
         3. Pandas
    
    *Visualisation
         4.Matplotlib    #R GGPLOT2 like statistical plots
         5. Seaborn      #Dependent on matplot lib; has heat maps and other stuff
         6. Bokeh        #NOT Dependent on matplot lib; Interactive Visualisation;
         7. Plotly       #a web-based toolbox for building visualizations, exposing APIs to some programming languages like Python;
     *Machine Learning.
         8. SciKit-Learn #Dependent on SciPy; Heavy math libaray usage; 
     *Deep Learning — Keras / TensorFlow / Theano
     
         9. Theano #multi-dimensional arrays similar to numpy.Compiled lib for efficeint and cross platform architecure;
         10. TensorFlow #From google;Neural Network training on large datasets;
                        #This powers Google’s voice recognition and object identification from pictures.
        11. Keras #For Neural Network training; Dependent on Theano and Tensorflow;
                        #written in pure Python.
     *Natural Language Processing.
         12. NLTK #For ext tagging, classification, and tokenizing, name entities identification, 
                  #building corpus tree that reveals inter and intra-sentence dependencies, stemming, semantic reasoning;
    
     * Data Mining. Statistics.
        13.Scrapy #Retrieval of the structured data, such as contact info or URLs, from the web
        14.Statsmodels # estimation of statistical models and performing statistical assertions
        15. Gensim - Vector space modelling;
        
===============================================================================
'''
