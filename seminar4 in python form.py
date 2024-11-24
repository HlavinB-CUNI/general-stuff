pd.read_csv('04_auxiliary/data_2017_zs.csv', sep=';',  on_bad_lines= 'skip')

# load the "raw" data for one particular year
df = pd.read_csv('04_auxiliary/data_2017_zs.csv', sep = ';', on_bad_lines= 'skip')
df.head()


# raw data have column names in czech, let's rename them
# if you do not want to reassign, you can provide arg. "inplace = True"
df = df.rename(columns = {
    'cislo_dot' : 'number',
    'kod_predm' : 'course_code',
    'nazev_predm' : 'course_title',
    'prednasejici' : 'teachers',
    'cvicici' : 'seminar_leaders',
    't1': 'c_value',
    't2': 'c_improve', 
    'katedra_code' : 'department_code'
})
df.head(2)
# iterative
df.index

RangeIndex(start=0, stop=6995, step=1)

# set column named "course_code" to be an index (or you can use "inplace" option again)
df.set_index('number', inplace=True)

df.head()
df.shape

(6995, 20)

df.course_code


# look at the data but refrain from drawing the conclusions
df.head(5)


# try to call it as a function
# df.shape() # it si an attribute not a function
df.shape

(6995, 20)

# classical data summarization
df.describe()
df.info() # more detailed info


# memory usage of each column in bytes (useful when working with the larger datasets)
df.memory_usage()
df.memory_usage().sum()
df.memory_usage().sum() / 1024**2 # in MB



#Signature: df.memory_usage(index: 'bool' = True, deep: 'bool' = False) -> 'Series'
#Docstring:
#Return the memory usage of each column in bytes.

#The memory usage can optionally include the contribution of
#the index and elements of `object` dtype.

#This value is displayed in `DataFrame.info` by default. This can be
#suppressed by setting ``pandas.options.display.memory_usage`` to False.

#Parameters
#----------
#index : bool, default True
#    Specifies whether to include the memory usage of the DataFrame's
#    index in returned Series. If ``index=True``, the memory usage of
#    the index is the first item in the output.
#deep : bool, default False
#    If True, introspect the data deeply by interrogating
#    `object` dtypes for system-level memory consumption, and include
#    it in the returned values.

#Returns
#-------
#Series
#    A Series whose index is the original column names and whose values
#    is the memory usage of each column in bytes.

#See Also
#--------
#numpy.ndarray.nbytes : Total bytes consumed by the elements of an
#    ndarray.
#Series.memory_usage : Bytes consumed by a Series.
#Categorical : Memory-efficient array for string values with
#    many repeated values.
#DataFrame.info : Concise summary of a DataFrame.

#Notes
#-----
#See the :ref:`Frequently Asked Questions <df-memory-usage>` for more
#details.

#Examples
#--------
dtypes = ['int64', 'float64', 'complex128', 'object', 'bool']
data = dict([(t, np.ones(shape=5000, dtype=int).astype(t))
             for t in dtypes])
df = pd.DataFrame(data)
df.head()


df.memory_usage()


df.memory_usage(index=False)


#The memory footprint of `object` dtype columns is ignored by default:
df.memory_usage(deep=True)


#Use a Categorical for efficient storage of an object-dtype column with
#many repeated values.

df['object'].astype('category').memory_usage(deep=True)


    #you can treat a DataFrame semantically like a dict of like-indexed Series objects
    #    getting, setting, and deleting columns works with the same syntax as the analogous dict operations

#Indexing/Selection
#Operation 	Syntax 	Result
#Select column 	df[col] 	Series
#Select row by label 	df.loc[label] 	Series
#Select row by integer location 	df.iloc[loc] 	Series
#Slice rows 	df[5:10] 	DataFrame
#Select rows by boolean vector 	df[bool_vec] 	DataFrame

# gives us series
df['course_title']

number

# this demonstrates usefulness of proper column naming
df.course_title

# multiple columns -> gives us dataframe
df[['course_title']]


# just one column: just convenience (if column name has a space or dot, you are screwed)
#naming conventions: no special character, underscore for spaces, no CZECH chars! informative and short
df.course_title


# subset of columns you want 
df[['course_title','teachers']].head(10)

# list of all columns 
df.columns

Index(['course_code', 'course_title', 'teachers', 'seminar_leaders', 'q1',
       'q2', 'q3', 'q4', 'q5', 'q6', 'q7', 'q8', 'q9', 'q10', 'q11', 'q12',
       'q13', 'c_value', 'c_improve', 'department_code'],
      dtype='object')

# adding columns (first adding, so we have something to drop)
df['tmp'] = '11/10'
# you can also use assign function, if new column should be a function of original column 
df.head()


df['sumq1q2'] = df.q1 + df.q2
df.head()


# drop column (you can also use 'del' (a general python command for deleting)
df.drop('tmp', axis = 1, inplace = True) # axis to specify you want to drop column, inplace operation in this case
df.head()

(df.department_code == 'ies') & (df.teachers.str.contains('Baruník'))


df[(df.department_code == 'ies') & (df.teachers.str.contains('Baruník'))]
df[df.department_code == 'ies']

#.loc selects data by the label of the rows and columns (as opposed to the .iloc) integer location
#we can also use .loc for subsetting based on condition(s)


df.loc[5:25:3, ['department_code','teachers']]


df.iloc[5:25:3, [-2, 2]] # iloc is integer based, different from loc which is label based

# select only observations for IES only, mask done at once
df_ies = df.loc[df['department_code'] == 'ies']
df_ies.head()

# select only observations for Advanced Econometrics
df.loc[df['course_title'] == 'Advanced Econometrics'].head(5)

# sub-setting based on multiple conditions: AE and non-missing comment on what to improve
df.loc[(df['course_title'] == 'Advanced Econometrics') & (~df['c_improve'].isnull())].head(2)

print([x for x in df.columns if "q" in x])  # by substring


# list comprehension
print([x for x in df.columns if "q" in x])  # by substring
print([x for x in df.columns if (len(x) == 2) | (len(x) == 3)])  # by length
print([x for x in df.columns if x.startswith("q")])  # by first letter
# by regular expression is the safest - q and then at most 2 digit number -> later in course
[x for x in df.columns if 'q' in x]

df_q = df[[x for x in df.columns if 'q' in x]]
df_q.head()

#Using functions on pandas objects
#Operation 	Function
#Row or Column-wise 	apply()
#Aggregation 	agg() / transform()
#Elementwise 	applymap()

#Tablewise

#    DFs and Series can be arguments of the functions
#    if multiple functions need to be called in a sequence, use pipe() method, also called the method chaining
#        often used in the data science setting
#        inspired by unix pipes and dplyr (%>%) operator in R

#Row or Column-wise Function Application

#    apply() is extremely powerful, when used with some brainpower

df_q.apply(np.mean, axis=0)

# using lambda - anonymous function
# standardization to unit variance
df_q.apply(lambda x: (x - np.mean(x)) / np.std(x), axis=0)

# using custom function, with arguments (could have also be done with lambda)
def add_and_substract(df, sub=1, add=1):
    return df - sub + add

df_q.apply(add_and_substract, args=(1, -1))

# A little bit more sophisticated:  show the longest comment
df.loc[df["c_value"].apply(lambda x: len(str(x))).idxmax(), "c_value"]

"1) Empirical project was very beneficial, as well as the homeworks which force students to work more consistently throughout the semester. Deadline for project in examination period was also good since students could chose when do they want to work on the project.2) Ms Malinska's seminars were interesting and her explanations were quite well, but the content could be more connected to content of lectures. Mr Pleticha explains the concepts quite well and has good attitude towards students and well prepared materials (mail with explanation of frequent errors, extensive seminar solutions). I also appreciate Ms Chorna for the good attitude towards students (it was very useful that we got notes to seminar solutions.Dr. Pertold-Gebicka is for sure a true expert in the field and knows a lot about it. Content of the course itself is very interesting, but the teaching needs change. Overall I learned a lot during the semester, but I believe that it is more because of my independent work than because of the lectures and seminars - attendance was not very beneficial and it was usually better to go through the materials alone."

df["c_value"].apply(lambda x: len(str(x))).idxmax() # gets the longest comment length

#Returns
#-------
#Series
 #   Indexes of maxima along the specified axis.

#Raises
#------
ValueError
#    * If the row/column is empty

#See Also
#--------
#Series.idxmax : Return index of the maximum element.

#Notes
#-----
#This method is the DataFrame version of ``ndarray.argmax``.

#Examples
#--------
#Consider a dataset containing food consumption in Argentina.

df = pd.DataFrame({'consumption': [10.51, 103.11, 55.48],
                    'co2_emissions': [37.2, 19.66, 1712]},
                  index=['Pork', 'Wheat Products', 'Beef'])

df

#By default, it returns the index for the maximum value in each column.
df.idxmax()


#To return the index for the maximum value in each row, use ``axis="columns"``.
df.idxmax(axis="columns")

df.loc[df["c_value"].apply(lambda x: len(str(x))).idxmax()]

df.index[max(df["c_value"].apply(lambda x: len(str(x)))) == df["c_value"].apply(lambda x: len(str(x)))] # alternative to find max and its index
df.loc[df.index[max(df["c_value"].apply(lambda x: len(str(x)))) == df["c_value"].apply(lambda x: len(str(x)))]] 


#Aggregation

    #aggregate() and transform()
    #aggregation allows multiple aggregation operations in a single concise way
    #transform() method returns an object that is indexed the same as the original
        #allows multiple operations at the same time, instead of one-by-one as aggregate() method

# aggregating simple function is the same as apply
df_q.agg(np.mean, axis=0)

# df_q.mean()

# aggregating more functions more interesting (you could do your own describe function easily! )
df_q.aggregate([np.mean, np.std, np.min, np.max], axis = 0)

# df_q.aggregate([pd.Series.mean, pd.Series.std, pd.Series.min, pd.Series.max], axis=0)

# aggregating using dictionary, i.e. column specific aggregation 
df_q.agg({'q1' : [np.mean], 'q2': np.std, 'q3': [np.mean, np.std, np.var]})

# using single function, the same as with apply
df_q.transform(lambda x: np.power(x,2))

# using multiple functions (can also be done using dictionary as in the case of aggregate)
df_q.transform([np.abs, lambda x: x + 1])


df.head()
df.teachers.notnull()
df.teachers.notnull().sum()

# check for missing values, sum is summing those NA
df.teachers.isna().any(), df.teachers.isna().sum() # isna is alias for isnull
df[df.teachers.notnull()]

#% of missing observations for specific column
df["q1"].isnull().sum() / df["q1"].count()

#% of missing observations for all columns
(df.isnull().sum() / df.shape[0]).sort_values().plot.bar()
(df.isnull().sum() / df.shape[0]).sort_values().plot.bar(ylim=(0, 1), grid=True, figsize=(5,3))

print(df.dropna(subset=['q1', 'q2'], how='any').shape)
df.dropna(subset=['q1', 'q2'], how='any').head()
df.dropna().shape # drop all rows with any missing value

(222, 21)

# Matplot lib

import matplotlib.pyplot as plt
#%matplotlib inline

# increasing the size of the figure
plt.figure(figsize = (20,10))

from time import sleep
plt_styles_list = plt.style.available
len(plt_styles_list)


# let's see how different styles look like
for style in plt_styles_list[:10]:
    plt.style.use(style)
    print(style)
    plt.figure(figsize=(5,2))
    plt.plot(np.sin(np.linspace(0,2*np.pi)))
    plt.show()
    sleep(1)

plt.style.use('classic')
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
plt

#for multiple subplots: fig, (ax0, ax1) = plt.subplots(nrows=1, ncols=2, sharey=True, figsize=(7, 4))
#call plt.subplot() and specify three numbers:
        #number of rows
        #number of columns
        #subplot number you want to activate.
    #if subplots are too squished plt.tight_layout()

plt.figure(figsize=(5,5))
for i in range (1, 5):
    plt.subplot(2, 2, i)
    plt.text(0.5,0.5, str((2, 2, i)), ha='center', fontsize = 10) #again, just a plot
    plt.tight_layout() 
    plt.grid(True) # add the grid

# for multiple figures and axes 

def f(x):
    return np.exp(-x) * np.cos(2*np.pi*x)

x1 = np.arange(0.0, 5.0, 0.1)
x2 = np.arange(0.0, 5.0, 0.02)


plt.figure(1, figsize=(5,3)) # optional, since figure(1) will be created by default
plt.subplot(211)
plt.plot(x1, f(x1), 'bo', x2, f(x2), 'k')

plt.subplot(212)
plt.plot(x2, np.tan(2*np.pi*x2), 'r--')

plt.show()

mu, sigma, n = 100, 15, 10000
x = np.random.normal(mu, sigma, n)

plt.figure(figsize=(5,5))
# the histogram of the data
plt.hist(x, bins = 50, density= True, facecolor='g')

plt.xlabel('x')
plt.ylabel('Probability')
plt.title('Histogram of X')

# Adding text, with LaTeX syntax, for math symbols
# meaningful text, 
plt.text(60, .025, f'$\mu={mu},\ \sigma={sigma}$')
# tail events text
plt.text(40, .00025, f"I've seen better times.")

plt.grid(True)

#Saving plots

# ax = plt.subplot()
plt.subplot(111)
t = np.arange(0.0, 5.0, 0.01)
s = np.cos(2*np.pi*t)
line, = plt.plot(t, s, lw=2)

plt.annotate('local max', xy=(2, 1), xytext=(3, 1.5),
             arrowprops=dict(facecolor='black', shrink=0.05),
             )

plt.ylim(-2, 2)
plt.show()

# actually saving
plt.savefig('04_auxiliary/local_max.png')


#Explanation of fig and ax, you might encounter when working with plots (openAI):

#fig, ax = plt.subplots() or fig, ax = plt.figure() is a common syntax used for creating plots with control over the figure and its axes.
#fig, ax = plt.subplots()
#fig: The canvas, representing the whole figure, where you set properties affecting all subplots.
#ax or axes: The individual plot areas (one or more Axes) within the figure, where you do the actual plotting and customization.

# Example
import matplotlib.pyplot as plt

# Create a figure with a single Axes
fig, ax = plt.subplots(figsize=(6, 4))  # figsize the size of the figure in inches

# Plot data on the Axes
ax.plot([1, 2, 3, 4], [10, 20, 25, 30], label='Sample Line')

ax.scatter([1, 2, 3, 4], [10, 20, 25, 30], label='Sample Dots', color='red')

# Customize the Axes
ax.set_title('Sample Plot')
ax.set_xlabel('X-axis Label')
ax.set_ylabel('Y-axis Label')
ax.legend()

# Show the figure
plt.show()


