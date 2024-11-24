import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# numpy stuff good to know
arr = np.array([1, 2, 3, 4, 5]) #make array
print(arr) #print it, remember index starts at 0
print(type(arr)) # print the type of data

# function for looping array
for x in arr:
    print(x)

# splitting array
newarr = np.array_split(arr,3) # splits into 3 segments
print(newarr)

# need to find even numbers? np.where(arr%2 == 0)
# need to find even numbers? np.where(arr%2 == 1)
# need to find if prime?  # check for factors
    ##for i in range(2, num):
       ## if (num % i) == 0:
            # if factor is found, set flag to True
          ##  flag = True
            # break out of loop
          ##  break

# PANDAS
a = [5,10,0]
b = [20,15,5]
np.array(a) + np.array(b) # now works as expected, based on position

#dataframe
pd.DataFrame({"var": [1, 2, 3], "column2": [0, 0, 0]})

#reading files
# pd.read_csv('04_auxiliary/data_2017_zs.csv', sep=';',  on_bad_lines= 'skip')

# load the "raw" data for one particular year
#df = pd.read_csv('04_auxiliary/data_2017_zs.csv', sep = ';', on_bad_lines= 'skip')
#df.head()

#Operation 	                        Syntax 	            Result
#Select column 	                    df[col] 	        Series
#Select row by label 	            df.loc[label] 	    Series
#Select row by integer location 	df.iloc[loc] 	    Series
#Slice rows 	                    df[5:10] 	        DataFrame
#Select rows by boolean vector 	    df[bool_vec] 	    DataFrame

# drop column (you can also use 'del' (a general python command for deleting)
#df.drop('tmp', axis = 1, inplace = True) # axis to specify you want to drop column, inplace operation in this case

#listing with all conditions
#df[(df.department_code == 'ies') & (df.teachers.str.contains('Baruník'))] 

#subset using a mask
#df_ies = df.loc[df['department_code'] == 'ies']


#MATPLOTLIB
plt.style.use('ggplot')
# minimum example of pyplot
x = np.linspace(0, 2, 100)

# we can also specify only "y" and use default x-axis: plt.plot(x, label='linear')
plt.figure(figsize=(5,3))
plt.plot(x, x, label='linear',  linewidth=2.0)
plt.plot(x, x**2, label='quadratic')
plt.plot(x, np.sqrt(x),'k^:',label='sqrt')

plt.xlabel('x label')
plt.ylabel('y label')
plt.title("Basic plots")

plt.legend(loc = 'best');