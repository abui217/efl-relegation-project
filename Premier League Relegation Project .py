#!/usr/bin/env python
# coding: utf-8

# In[99]:


import pandas as pd 
import numpy as np 
import matplotlib.pyplot as plt 
get_ipython().run_line_magic('matplotlib', 'inline')
import matplotlib as mpl


# The English Premier League is the most competitve football/soccer league in the world. The league includes 20 teams each season. The top four teams in the league qualifies in a European tournament in the next season call the UEFA Champions League, as 5th place qualifys for the UEFA Europa League. The 3 clubs who finish 18th to 20th are demoted into the 2nd tier of English Football called the 'EFL Championship,' and they replaced by the top 3 teams from the EFL Championship. In this case study, we will find the average of how many points does a club need to avoid relegation, average points of clubs who did get relegated from each season, and the average of goal difference for all the relegation clubs.  

# In[7]:


epl = pd.read_csv('premierleaguestandings_2000-2022.csv')
epl


# In[67]:


##Database of clubs who were relegated to the EFL Championship
rel = epl['Pos'].between(18,20)
efl = epl[rel] 
efl


# In[27]:


##Average amount of points clubs who were relegated to the EFL Championship per season
sum(efl['Pts']) / 66


# In[35]:


##Average Goal Difference for all relegated clubs 
gd = sum(efl['GD']) / 66
gd


# In[42]:


##Average Wins between clubs who were relegated to the EFL Championship 
sum(efl['W']) / 66


# In[43]:


##Average Draws between clubs who were relegated to the EFL Championship 
sum(efl['D']) / 66


# In[44]:


##Average Losses between clubs who were relegated to the EFL Championship 
sum(efl['L']) / 66


# In[105]:


esc = epl.query('Pos == 17')
esc


# In[90]:


len(esc)


# In[91]:


sum(esc['Pts']) / 22


# In[92]:


eighteen = epl.query('Pos == 18')
eighteen


# In[93]:


sum(eighteen['Pts']) / 22


# In[95]:


seclast = epl.query('Pos == 19')
seclast


# In[96]:


sum(seclast['Pts']) / 22


# In[97]:


last = epl.query('Pos == 20')
last


# In[98]:


sum(last['Pts']) / 22


# In[108]:


#X axis represent each club finished from 17th place to 20th place.
#Y axis present points average in a season. 
x = ['17th', '18th', '19th', '20th']
y = [38, 35, 31, 25]


plt.bar(x, y, color='purple')
plt.xlabel('Finished Position ')
plt.ylabel('Average of Points in each position each season')
plt.title('EPL Relegation Average Pts 17-20th place (2000-22 Season)')
plt.show()


# In[101]:


labels = 'Wins', 'Draw', 'Losses'
sizes = [7, 9, 22]

fig, ax = plt.subplots()
ax.pie(sizes, labels=labels)


# In[ ]:




