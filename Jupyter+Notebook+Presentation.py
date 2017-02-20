
# coding: utf-8

# <img src="http://blog.jupyter.org/content/images/2015/02/jupyter-sq-text.png"
# style="width:100px;height:100px;float:right">
# # Jupyter Notebook Tutorial Presentation
# 
# #### Presented by Jiahui Wei
# 
# This is a Jupyter Notebook tutorial. Presented at CMPS263 Winter 2017.
# 
# The tutorial will include:
# * Jupyter Notebook built-in commands
# * Use code cell to help visualize data 
# * Use markdown cell to keep notes
# * Export ipynb file to other format

# ## 1. Jupyter Notebook Built-in Commands

# ### i. Use Jupyter as a terminal

# In[ ]:

pwd


# In[ ]:

ls


# ### ii View and run *.py file in Jupyter
# 
# Use
# ```Shell
# $ %pycat example.py
# ``` 
# to view local \*.py file.
# 
# Use 
# ```Shell
# $ %run example.py
# ```
# to run local \*.py file.

# In[ ]:

get_ipython().magic(u'pycat add_example.py')


# In[ ]:

get_ipython().magic(u'run add_example.py')


# ### iii. Jupyter can write Python code into file
# 
# Use 
# ```Shell
# $ %writefile example.py
# ```
# to write code or text into a file.

# In[ ]:

ls


# In[ ]:

get_ipython().run_cell_magic(u'writefile', u'test.py', u"#encoding utf-8\nimport datetime\n\ndef print_time():\n    print 'the time is:'\n    print datetime.datetime.now()\n\nprint_time()")


# In[ ]:

get_ipython().magic(u'pycat test.py')


# ### iv.  load .py file into Jupyter
# 
# Use
# ```Shell
# $ %load example.py
# ```
# to load python file code into Jupyter

# In[ ]:

get_ipython().magic(u'load test.py')


# ### v. Record the run time of the code
# 
# Use %%time to record time execution of a Python statement or expression.

# In[19]:

get_ipython().run_cell_magic(u'time', u'', u'import time\nsum=0\nfor x in range(100):\n    sum+=x\n    time.sleep(0.01)\nprint sum')


# Use %%timeit to record average time execution of a Python statement or expression

# In[22]:

get_ipython().run_cell_magic(u'timeit', u'', u'import time\nsum=0\nfor x in range(100):\n    sum+=x')


# ## 2. Use code cell to help visualize data
# 
# Use matplotlib, pandas and other libraries with Jupyter to help visulaize data

# ### i. Run simple Python code

# In[ ]:

1+2


# In[24]:

def add_1(x,y):
    return x+y+1
add_1(2,3)
print_time()


# ### ii. Use matplotlib to draw graph of data
# 
# Add
# ```Python
# %matplotlib inline
# ```
# to plot graph inside Jupyter

# In[3]:

get_ipython().magic(u'matplotlib inline')
import matplotlib.pyplot as plt
import numpy as np

Fs = 200
f = 2
sample = 200
x = np.arange(sample)
y = np.sin(2 * np.pi * f * x / Fs)
plt.plot(x, y)


# [Seaborn](http://seaborn.pydata.org/index.html) is a plotting library for Python that uses matplotlib underneath the hood. It provides for a number of plotting types that don't exist in matplotlib. 
# 
# *The example used below is from [here](https://github.com/welchr/csg-jupyter-tutorial/blob/master/csg_jupyter_tutorial.ipynb)*

# In[37]:

get_ipython().magic(u'matplotlib inline')
import numpy as np
from scipy.stats import kendalltau
import seaborn as sns

rs = np.random.RandomState(20)
x = rs.normal(size=1000)
y = -.5 * x + rs.normal(size=1000)

ax = sns.jointplot(x, y, kind="hex")


# ### iii. Use pandas to show the results of data frame

# In[ ]:

import numpy as np
import pandas

def get_df():
    data_frame = pandas.read_csv('data-text.csv', sep=',')
    return data_frame

get_df()


# ## 3. Use markdown cell to keep notes

# There is a example of a markdown below. 

# # A First Level Headline
# 
# Use \*word\* to show *Italic* 
# 
# Use \*\*word\*\* to show **bold**. 
# 
# Itemized lists look like:
# 
#   * this one
#   * that one
# 
# Here's a numbered list:
# 
#  1. first item
#  2. second item
#  3. third item
# 
# ## A Second Level Headline
# 
# You can add code block into the cell like this:
# 
# This is a python code block
# ```Python
# import time
# # Quick, count from 0 to 9!
# for i in range(10):
#     # wait for a while
#     time.sleep(0.5)
#     print i
# ```
# This is a C++ code block
# ```C++
# #include<iostream>
# usig namespace std;
# int main(){
# cout<<"Hello World!"<<endl;
# }
# ```
# 
# ### A Third Level Headline
# 
# Here's a link to [a website](http://www.ucsc.edu), to a [local
# file](./Sample_im.jpg).
# 
# Inline math equations go in like so: $\int_0^{+\infty} x^2 dx$. Display
# math should get its own line and be put in in double-dollarsigns:
# $$\int_0^{+\infty} x^2 dx$$
# Images can also be added into markdown cell
# 
# <img src="./Sample_im.jpg"
# style="width:320px;height:240px;float:center">

# *Markdown example used from [here](http://www.unexpected-vortices.com/sw/rippledoc/quick-markdown-example.html#an-h2-header) with some edits*

# ### i. Basic Text edit

# # A First Level Headline
# 
# Use \*word\* to show *Italic* 
# 
# Use \*\*word\*\* to show **bold**. 
# 
# Itemized lists look like:
# 
#   * this one
#   * that one
# 
# Here's a numbered list:
# 
#  1. first item
#  2. second item
#  3. third item
# 

# ### ii. Code Block

# Code block can be highlighted according to the language
# 
# This is a python code block
# ```Python
# import time
# # Quick, count from 0 to 9!
# for i in range(10):
#     # wait for a while
#     time.sleep(0.5)
#     print i
# ```
# This is a C++ code block
# ```C++
# #include<iostream>
# usig namespace std;
# int main(){
# cout<<"Hello World!"<<endl;
# }
# ```

# ### iii. Links

# [Link to offline Pictures](./Sample_im.jpg)
# 
# [Link to online website](http://www.ucsc.edu)
# 
# Another type of link <http://www.ucsc.edu>
# 
# 

# ### iv. Latex
# Latex can also be used in Jupyter to write math expression

# This is an expression as a single expression
# $$\int_0^2 x^2 dx$$
# 
# Inline expression is also supported, for example, $\int^2_0 x^2 dx$

# ### v. Images
# 
# Images can be added like links.

# ![Image](./Sample_im.jpg)

# We can use HTML style to edit image size and position
# 
# <img src="./Sample_im.jpg"
# style="width:320px;height:240px;float:left"> 

# ### vi. Video
# We can also add videos in Jupyter

# In[39]:

get_ipython().run_cell_magic(u'html', u'', u'<iframe width="560" height="315" src="https://www.youtube.com/embed/HW29067qVWk" frameborder="0" allowfullscreen></iframe>')


# ## 4. Export \*.ipynb file to other formats to share with others

# ### i. Github
# 
# Github can load \*.ipynb file, here is [an example](https://github.com/jhwei/Jupyter_Tutorial/blob/master/Jupyter%20Notebook%20Presentation.ipynb)
# 
# ### ii. Export to other formats
# 
# Goto **File**->**Download as** to select the file format you want to export to.
# 
# Or you can type the following command in terminal
# ```
# $ jupyter nbconvert --to FORMAT notebook.ipynb
# ```
# 
# * FORMAT means the file format you want to export to, such as, pdf, html
# * you may need to install latex and other software depending on your computer
# * please refer to the error to see if some software is missing if you don't succeed
# 
# ### iii. Several example output
# 
# * An example of [html](./Jupyter+Notebook+Presentation.html)
# 
# * An example of [pdf]()

# ## 5. Useful Resources

# Offical Documentation <https://jupyter.readthedocs.io/en/latest/index.html>
# 
# Markdown syntx Document from Github <https://guides.github.com/features/mastering-markdown/>
# 
# Jupyter with other programming languages <https://github.com/jupyter/jupyter/wiki/Jupyter-kernels>
# 
# Some nice Jupyter examples <http://nb.bianp.net/sort/views/>
# 
# Another good Jupyter tutorial <https://github.com/welchr/csg-jupyter-tutorial>
# 
# Turn Jupyter to presentation slides with RISE <https://github.com/damianavila/RISE> 
# 
# Combine Jupyter with WordPress <http://www.mianchen.com/wordpress-blogging-with-jupyter-notebook-in-five-simple-steps/>
