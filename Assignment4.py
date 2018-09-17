
# coding: utf-8

# # Assignment 4
# 
# Before working on this assignment please read these instructions fully. In the submission area, you will notice that you can click the link to **Preview the Grading** for each step of the assignment. This is the criteria that will be used for peer grading. Please familiarize yourself with the criteria before beginning the assignment.
# 
# This assignment requires that you to find **at least** two datasets on the web which are related, and that you visualize these datasets to answer a question with the broad topic of **religious events or traditions** (see below) for the region of **Ann Arbor, Michigan, United States**, or **United States** more broadly.
# 
# You can merge these datasets with data from different regions if you like! For instance, you might want to compare **Ann Arbor, Michigan, United States** to Ann Arbor, USA. In that case at least one source file must be about **Ann Arbor, Michigan, United States**.
# 
# You are welcome to choose datasets at your discretion, but keep in mind **they will be shared with your peers**, so choose appropriate datasets. Sensitive, confidential, illicit, and proprietary materials are not good choices for datasets for this assignment. You are welcome to upload datasets of your own as well, and link to them using a third party repository such as github, bitbucket, pastebin, etc. Please be aware of the Coursera terms of service with respect to intellectual property.
# 
# Also, you are welcome to preserve data in its original language, but for the purposes of grading you should provide english translations. You are welcome to provide multiple visuals in different languages if you would like!
# 
# As this assignment is for the whole course, you must incorporate principles discussed in the first week, such as having as high data-ink ratio (Tufte) and aligning with Cairo’s principles of truth, beauty, function, and insight.
# 
# Here are the assignment instructions:
# 
#  * State the region and the domain category that your data sets are about (e.g., **Ann Arbor, Michigan, United States** and **religious events or traditions**).
#  * You must state a question about the domain category and region that you identified as being interesting.
#  * You must provide at least two links to available datasets. These could be links to files such as CSV or Excel files, or links to websites which might have data in tabular form, such as Wikipedia pages.
#  * You must upload an image which addresses the research question you stated. In addition to addressing the question, this visual should follow Cairo's principles of truthfulness, functionality, beauty, and insightfulness.
#  * You must contribute a short (1-2 paragraph) written justification of how your visualization addresses your stated research question.
# 
# What do we mean by **religious events or traditions**?  For this category you might consider calendar events, demographic data about religion in the region and neighboring regions, participation in religious events, or how religious events relate to political events, social movements, or historical events.
# 
# ## Tips
# * Wikipedia is an excellent source of data, and I strongly encourage you to explore it for new data sources.
# * Many governments run open data initiatives at the city, region, and country levels, and these are wonderful resources for localized data sources.
# * Several international agencies, such as the [United Nations](http://data.un.org/), the [World Bank](http://data.worldbank.org/), the [Global Open Data Index](http://index.okfn.org/place/) are other great places to look for data.
# * This assignment requires you to convert and clean datafiles. Check out the discussion forums for tips on how to do this from various sources, and share your successes with your fellow students!
# 
# ## Example
# Looking for an example? Here's what our course assistant put together for the **Ann Arbor, MI, USA** area using **sports and athletics** as the topic. [Example Solution File](./readonly/Assignment4_example.pdf)

# In[164]:

#get_ipython().magic('matplotlib notebook')

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.backends.backend_agg import FigureCanvasAgg

df=pd.read_excel("Religion.xlsx", skiprows = range(9, 20))

df


# In[ ]:




# In[ ]:




# In[165]:

fig, ((ax1, ax2), (ax3, ax4)) = plt.subplots(2, 2, sharey=True, figsize = (10, 8), facecolor="w")
canvas = FigureCanvasAgg(fig)


axes = [ax1, ax2, ax3, ax4]
fig.suptitle("How Belief in God changed in Michigan compared to USA nationwide and few other states", fontsize=14)


area = list(df["Area"].unique())

n=0
for a in area:
    
    #define data to display   
    data_14 = df[(df["Area"]==a) & (df["Year"]==2014)].T.iloc[2:7]
    data_07 = df[(df["Area"]==a) & (df["Year"]==2007)].T.iloc[2:7]
    
    bar_w=0.42
    xval=np.arange(5)
    
    #display data
    axes[n].bar(xval, data_07.squeeze(), width=bar_w, color = "#4a998f", label="2007", alpha =0.7)
    axes[n].bar(xval+bar_w, data_14.squeeze(), width=bar_w, color = "#2d5e58", label = '2014', alpha=0.7)
    
    #make charts beautiful
    axes[n].set_title(a)
    axes[n].set_xticks(xval + bar_w / 2)
    axes[n].set_xticklabels(('Absolutely\ncertain', 'Fairly\ncertain', 'Not\nsure', 'Not\nbelieve', 'Other'), fontsize=9)
    axes[n].spines['top'].set_color('none')
    axes[n].spines['right'].set_color('none')
    axes[n].legend(frameon=False)
    axes[n].set_yticklabels([])
    
    #direct labeling
    bars = axes[n].patches
    for bar in bars:
        h = bar.get_height()
        axes[n].text((bar.get_x() + bar.get_width()/2), (h + 0.03), str(float(h)*100)+"%", ha="center", color='black', fontsize=7)
    
    n+=1

plt.tight_layout(pad=4.0, w_pad=2.5, h_pad=2.5)
canvas.print_png('assignment_4.png')
plt.savefig('assignm_4.png')

# In[ ]:



