
# coding: utf-8

# #### Imports:

# In[66]:


import numpy as np
import csv
from timeit import default_timer as time
import pandas as pd
import matplotlib
from matplotlib import pyplot as plotty
import scipy
from scipy.optimilist_for_errorse import curve_fit


# # EX1: Identifying function and tuning parameters

# In[112]:


data_set=pd.read_csv('datafile.csv')
x_coord=data_set['X']
y_coord=data_set['YN']
x=x_coord[0:12]
y=y_coord[0:12]
plotty.plot(x_coord,y_coord)
plotty.show()


# In[113]:


def Math_Function(x, a, b, c,d):
    return a * np.power(x,3)+ b * np.power(x,2)+ c*x + d

plotty.plot(x_coord, y_coord, 'b-', label='points')
coefficient, pcov = curve_fit(Math_Function, x_coord, y_coord)
plotty.plot(x_coord, Math_Function(x_coord, *coefficient), 'r-',
         label='Curve_fit: a=%5.3f, b=%5.3f, c=%5.3f, d=%5.3f' % tuple(coefficient))
plotty.xlabel('x')
plotty.ylabel('y')
plotty.legend()
plotty.show()


# In[114]:




y_value=Math_Function(x_coord,*coefficient)
list_for_errors=[]
for i in range(len(y_value)):
        list_for_errors.append((y_value[i]-y_coord[i])**2)
sum(list_for_errors)

print('----------------------------------------------------')

print("Mean error : ",sum(list_for_errors)/len(list_for_errors))
print("\nMedian of error : ",list_for_errors[int(len(list_for_errors)/2)])

print('----------------------------------------------------')

print('\nParameters obtained for \'a\'b\'c\'d\' :',coefficient)


# ### Cubic Function by Gnuplot:

# In[115]:


from IPython.display import Image
Image(filename='Ex-1 cubic.png')


# ### Description:
# 
# For identifying the best parameters to fit with our function I used the curve fitting method. Curve fitting is the process of constructing a curve, or mathematical function, that has the best fit to a series of data points,possibly subject to constraints. It can also involve interpolation and extrapolation.
# 
# REFERENCE: https://en.wikipedia.org/wiki/Curve_fitting

# # EX2 : Outliers in data and curve trends w.r.t functions

# In[116]:


a=np.random.randint(low=100, high=200, size=13)
b=np.random.randint(low=20000, high=40000, size=13)
data_set2 = pd.DataFrame({'X':a, 'YN':b})
res=data_set.append(data_set2,ignore_index=True)
res
x_coord2=res['X']
y_coord2=res['YN']


# ### Cubic Function: Curve Fitting

# In[117]:


def Math_Function(x, a, b, c,d):
    return a * np.power(x,3)+ b * np.power(x,2)+ c*x + d
plotty.plot(x_coord2, y_coord2, 'b-', label='data')
coefficient, pcov = curve_fit(Math_Function, x_coord2, y_coord2)
plotty.plot(x_coord2, Math_Function(x_coord2, *coefficient), 'r-',
         label='Curve_fit: a=%5.3f, b=%5.3f, c=%5.3f, d=%5.3f' % tuple(coefficient))
plotty.xlabel('x')
plotty.ylabel('y')
plotty.legend()
plotty.show()


# In[118]:


y_value=Math_Function(x_coord2,*coefficient)
list_for_errors=[]
for i in range(len(y_value)):
        list_for_errors.append((y_value[i]-y_coord2[i])**2)
sum(list_for_errors)
print('----------------------------------------------------')

print("Mean error : ",sum(list_for_errors)/len(list_for_errors))
print("\nMedian of error : ",list_for_errors[int(len(list_for_errors)/2)])

print('----------------------------------------------------')


# ### Quadratic Function: Curve Fitting

# In[119]:


def Math_Function_2(x,b, c,d):
    a=0
    return a * np.power(x,3)+ b * np.power(x,2)+ c*x + d
plotty.plot(x_coord2, y_coord2, 'b-', label='data')
coefficient_3, pcov_3 = curve_fit(Math_Function_2, x_coord2, y_coord2)
plotty.plot(x_coord2, Math_Function_2(x_coord2, *coefficient_3), 'r-', label='fit: a=%5.3f, b=%5.3f, c=%5.3f,' % tuple(coefficient_3))
plotty.xlabel('x')
plotty.ylabel('y')
plotty.legend()
plotty.show()


# In[130]:


y_value=Math_Function_2(x_coord,*coefficient_3)
list_for_errors=[]
for i in range(len(y_value)):
        list_for_errors.append((y_value[i]-y_coord[i])**2)
sum(list_for_errors)
print("Mean error : ",sum(list_for_errors)/len(list_for_errors))
print("\nMedian of error : ",list_for_errors[int(len(list_for_errors)/2)])

print('----------------------------------------------------')

print('\nParameters obtained for \'a\'b\'c :',coefficient_3)


# ### Linear Function: Curve Fitting

# In[121]:


def Math_Function_3(x, c,d):
    a=0
    b=0
    return a * np.power(x,3)+ b * np.power(x,2)+ c*x + d
plotty.plot(x_coord2, y_coord2, 'b-', label='data')
coefficient_4, pcov_3 = curve_fit(Math_Function_3, x_coord2, y_coord2)
plotty.plot(x_coord2, Math_Function_3(x_coord2, *coefficient_4), 'r-', label='fit:b=%5.3f, c=%5.3f,' % tuple(coefficient_4))
plotty.xlabel('x')
plotty.ylabel('y')
plotty.legend()
plotty.show()


# In[131]:


y_value=Math_Function_3(x_coord2,*coefficient_4)
list_for_errors=[]
for i in range(len(y_value)):
        list_for_errors.append((y_value[i]-y_coord2[i])**2)
sum(list_for_errors)
print("Mean error : ",sum(list_for_errors)/len(list_for_errors))
print("\nMedian of error : ",list_for_errors[int(len(list_for_errors)/2)])

print('----------------------------------------------------')

print('\nParameters obtained for \'a\'b :',coefficient_4)


# # EX-3: 12 points to identify best fit

# ### Cubic Function: Curve Fitting

# In[125]:


plotty.plot(x, y, 'b-', label='data')
coefficient_5, pcov_5 = curve_fit(Math_Function, x, y)
plotty.plot(x, Math_Function(x, *coefficient_5), 'r-', label='Curve_fit: a=%5.3f, b=%5.3f, c=%5.3f, d=%5.3f' % tuple(coefficient_5))
plotty.xlabel('x')
plotty.ylabel('y')
plotty.legend()
plotty.show()


# In[132]:


y_value=Math_Function(x,*coefficient_5)
list_for_errors=[]
for i in range(len(y_value)):
        list_for_errors.append((y_value[i]-y[i])**2)
sum(list_for_errors)
print("Mean error : ",sum(list_for_errors)/len(list_for_errors))
print("\nMedian of error : ",list_for_errors[int(len(list_for_errors)/2)])

print('----------------------------------------------------')

print('\nParameters obtained for \'a\'b\'c\'d\' :',coefficient_5)


# ### Cubic Function by Gnuplot:

# In[141]:


from IPython.display import Image
Image(filename='Ex-3 cubic.png')


# ### Quadratic Function: Curve Fitting

# In[133]:


plotty.plot(x, y, 'b-', label='data')
coefficient_6, pcov_2 = curve_fit(Math_Function_2, x, y)
plotty.plot(x, Math_Function_2(x, *coefficient_6), 'r-', label='fit:  b=%5.3f, c=%5.3f, d=%5.3f' % tuple(coefficient_6))
plotty.xlabel('x')
plotty.ylabel('y')
plotty.legend()
plotty.show()


# In[135]:


y_value=Math_Function_2(x,*coefficient_6)
list_for_errors=[]
for i in range(len(y_value)):
        list_for_errors.append((y_value[i]-y[i])**2)
sum(list_for_errors)
print("Mean error : ",sum(list_for_errors)/len(list_for_errors))
print("\nMedian of error : ",list_for_errors[int(len(list_for_errors)/2)])

print('----------------------------------------------------')

print('\nParameters obtained for \'a\'b\'c :',coefficient_6)


# ### Quadratic Function by Gnuplot:

# In[142]:


from IPython.display import Image
Image(filename='Ex-3 quadratic.png')


# ### Linear Function: Curve Fitting

# In[138]:


plotty.plot(x, y, 'b-', label='data')
coefficient_7, pcov_2 = curve_fit(Math_Function_3, x, y)
plotty.plot(x, Math_Function_3(x, *coefficient_7), 'r-', label='fit: c=%5.3f, d=%5.3f' % tuple(coefficient_7))
plotty.xlabel('x')
plotty.ylabel('y')
plotty.legend()
plotty.show()


# In[140]:


y_value=Math_Function_3(x,*coefficient_7)
list_for_errors=[]
for i in range(len(y_value)):
        list_for_errors.append((y_value[i]-y[i])**2)
sum(list_for_errors)
print("Mean error : ",sum(list_for_errors)/len(list_for_errors))
print("\nMedian of error : ",list_for_errors[int(len(list_for_errors)/2)])

print('----------------------------------------------------')

print('\nParameters obtained for \'a\'b:',coefficient_7)


# ### Linear Function by Gnuplot:

# In[144]:


from IPython.display import Image
Image(filename='Ex-3 Linear.png')


# # EX4: Very Simple Grep and KMP Algorithm

# In[14]:


filename  = ('words.txt')
with open (filename) as f:
    read = f.readlines()

words=[]
for i in read:
    words.append(str(i[:-1]))   # Remove \n from words


# ### My Simple Code:

# In[18]:


search_pattern = input('Enter pattern to match--> ')
list(filter(lambda x:search_pattern in x, words))


# ### KMP Algorithm:
# 
# ### Code Reference: 
# https://gist.github.com/m00nlight/daa6786cc503fde12a77

# In[19]:



class KMP:

    
    def partial(self, pattern):
        """ Calculate partial match table: String -> [Int]"""
        ret = [0]
        
        for i in range(1, len(pattern)):
            j = ret[i - 1]
            while j > 0 and pattern[j] != pattern[i]:
                j = ret[j - 1]
            ret.append(j + 1 if pattern[j] == pattern[i] else j)
        return ret
        
    def search(self, T, P):
        """ 
        KMP search main algorithm: String -> String -> [Int] 
        Return all the matching position of pattern string P in S
        """
        partial, ret, j = self.partial(P), [], 0
        
        for i in range(len(T)):
            while j > 0 and T[i] != P[j]:
                j = partial[j - 1]
            if T[i] == P[j]: j += 1
            if j == len(P): 
                ret.append(i - (j - 1))
                j = 0
            
        return ret


# In[20]:


kmp = KMP()

for i in words:
    if(len(kmp.search(i,search_pattern))>0):
        print(i)


# ### Description:
# 
# The idea behind this was excercise was to run and test our own approach for string matching and any of the given algorithms. In my own code I ran my own approaching using filter command of python and finding the given pattern in all list of words.
# 
# Similarly in the KMP algorithm I passed the same pattern and verified the output. It was same as by my own approach.KMP algorithm Basically takes a pattern and check for the pattern in specified string if the pattern is found then the starting index of the pattern is marked and we move on the find the pattern again in the string which is left.

# # EX5: Speed Comparision of fgrep & custom code:

# ### Multiple-Patterns by custom approach, KMP and Fgrep

# ### Custom Test:

# In[21]:


filename_2  = ('pattern.txt')
with open (filename_2) as f:
    read_2 = f.readlines()

pattern_words=[]
for i in read_2:
    pattern_words.append(str(i[:-1]))
    
print(pattern_words)


start = time()
found_list=[]
for check in pattern_words:
    found_list.append(list(filter(lambda x: check in x, words)))
end = timer()

print("\nTime Taken for above multiple patterns by my algorithm :",end - start)


# ### KMP Test:

# In[37]:


start = time()
for i in pattern_words:
    for j in words:
        if(len(kmp.search(j,i))>0):
            pass
end = time()
print("\nTime Taken for above multiple patterns by KMP algorithm :",(end - start)/len(pattern_words))


# ### Description:
# 
# In this task I compared the running time efficiency of three approaches.i.e my own algorithm, the KMP algorithm and the fgrep that was mentioned in the excercise. In this case I worked with multiple patterns as asked in the question so here I am retrieving a file of patterns and running the same code as in excersie-4 and recording the time taken by them. Here is the comparision:
# 
# *  Fgrep : 0,0045379
# *  Custom algorithm : 0.1823303919998125
# *  KMP : 1.2686190604999865
# 
# 
# In above case the fgrep from linux terminal gave the best running time compared to my algorithm and kmp.
# 

# # EX6: Install & Try Agrep

# ## 1:

# In[145]:


from IPython.display import Image
Image(filename='agrep1.png')


# ## 2:

# In[146]:


from IPython.display import Image
Image(filename='agrep2.png')


# ## 3:

# In[149]:


from IPython.display import Image
Image(filename='agrep_time.png')


# ## 4:

# In[150]:


from IPython.display import Image
Image(filename='agrep4.png')


# ## 5:

# In[151]:


from IPython.display import Image
Image(filename='agrep6.png')


# ### Description:
# 
# Well I installed this library and tested it with two things:
# 
# * The running time
# * The patterns in words (Same as provided in previous exercises)
# 
# For the running time as seen in the figure 3 above its pretty much the same as of the fgrep that we ran previously.
# For patterns I first started with single patterns shown in the image 4 above. The results were same as obtained in the KMP algorithm as well as my own code. Then i tried out with multiple patterns and it was good to see multiple patterns was also built-in in this library.
# In the end I would like to generally say that its a good library for pattern matching.
