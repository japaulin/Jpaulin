#!/usr/bin/env python
# coding: utf-8

# In[7]:


#Loading needed Libraries
import pandas as pd
import numpy as np
import re


# In[8]:


work= pd.read_csv('Documents/DQE.csv')


# In[9]:


work.head()


# In[10]:


work.columns


# In[11]:


#Droping columns
work.drop(['Edition Statement', 'Corporate Author', 'Corporate Contributors', 'Former owner', 'Engraver', 'Issuance type', 'Contributors', 'Shelfmarks'], axis=1)


# In[12]:


work1= work.drop(['Edition Statement', 'Corporate Author', 'Corporate Contributors', 'Former owner', 'Engraver', 'Issuance type', 'Contributors', 'Shelfmarks'], axis=1)


# In[13]:


work1.columns


# In[14]:


#changing the index and deomnstrating its uniqueness
work1= work1.set_index('Identifier')
work1.index.is_unique


# In[15]:


#Showing the difference between label based indexing and position based indexing


# In[16]:


work1.loc[:2854]


# In[17]:


work1.iloc[:2854]


# In[215]:


#Cleaning up the Date of Publication column
work1['DoP']= work1['Date of Publication'].str.extract(r'^(\d{4})', expand= False)
work1.DoP= pd.to_numeric(work1['DoP'])
work1.DoP.dtype


# In[216]:


work1.DoP.head()


# In[20]:


#Standardizing and cleaning up the Place of Publication column


# In[202]:


work1Pop= work1['Place of Publication']
london= work1Pop.str.contains('London')
oxford= work1Pop.str.contains('Oxford')
new_york= work1Pop.str.contains('New York')
paris= work1Pop.str.contains('Paris')
edinburgh= work1Pop.str.contains('Edinburgh')
Leipzig= work1Pop.str.contains('Leipzig')
boston= work1Pop.str.contains('Boston')
philadelphia= work1Pop.str.contains('Phila')
berlin= work1Pop.str.contains('Berlin')
dublin= work1Pop.str.contains('Dublin')
glasgow= work1Pop.str.contains('Glasgow')

work1['PoP']= np.where(london, 'London',
             np.where(oxford, 'Oxford',
                      np.where(new_york, 'New York',
                               np.where(paris, 'Paris',
                                        np.where(edinburgh, 'Edinburgh',
                                                 np.where(Leipzig, 'Leipzig',
                                                          np.where(boston, 'Boston',
                                                                   np.where(philadelphia, 'Philadelphia',
                                                                            np.where(berlin, 'Berlin',
                                                                                     np.where(dublin, 'Dublin',
                                                                                              np.where(glasgow, 'Glasgow',
                     work1Pop.str.replace('-', ' '))))))))))))


# In[203]:


Cambridge= work1Pop.str.contains('Cambridge')
Wien= work1Pop.str.contains('Wien')
Stockholm= work1Pop.str.contains('Stockholm')
Madrid= work1Pop.str.contains('Madrid')
Kjøbenhavn= work1Pop.str.contains('Kjøbenhavn')
Manchester= work1Pop.str.contains('Manchester')
Birmingham= work1Pop.str.contains('Birmingham')
Newcastle= work1Pop.str.contains('Newcastle')
Albany= work1Pop.str.contains('Albany')
Mexico= work1Pop.str.contains('Mexico')
Budapest= work1Pop.str.contains('Budapest')

work1['PoP']= np.where(Cambridge, 'Cambridge',
             np.where(Wien, 'Wien',
                      np.where(Stockholm, 'Stockholm',
                               np.where(Madrid, 'Madrid',
                                        np.where(Kjøbenhavn, 'Kjøbenhavn',
                                                 np.where(Manchester, 'Manchester',
                                                          np.where(Birmingham, 'Birmingham',
                                                                   np.where(Newcastle, 'Newcastle',
                                                                            np.where(Albany, 'Albany',
                                                                                     np.where(Mexico, 'Mexico',
                                                                                              np.where(Budapest, 'Budapest',
                     work1Pop.str.replace('-', ' '))))))))))))


# In[204]:


Plymouth= work1Pop.str.contains('Plymouth')
Washington= work1Pop.str.contains('Washington')
Santiago= work1Pop.str.contains('Santiago')
Hartford= work1Pop.str.contains('Hartford')
Westminster= work1Pop.str.contains('Westminster')
Toronto= work1Pop.str.contains('Toronto')
Melbourne= work1Pop.str.contains('Melbourne')
Frankfurt= work1Pop.str.contains('Frankfurt')
Gravenhage= work1Pop.str.contains('Gravenhage')
Great_Yarmouth= work1Pop.str.contains('Great Yarmouth')
Belfast= work1Pop.str.contains('Belfast')

work1['PoP']= np.where(Plymouth, 'Plymouth',
             np.where(Washington, 'Washington',
                      np.where(Santiago, 'Santiago',
                               np.where(Hartford, 'Hartford',
                                        np.where(Westminster, 'Westminster',
                                                 np.where(Toronto, 'Toronto',
                                                          np.where(Melbourne, 'Melbourne',
                                                                   np.where(Frankfurt, 'Frankfurt',
                                                                            np.where(Gravenhage, 'Gravenhage',
                                                                                     np.where(Great_Yarmouth, 'Yarmouth',
                                                                                              np.where(Belfast, 'Belfast',
                     work1Pop.str.replace('-', ' '))))))))))))


# In[205]:


c= work1Pop.str.contains(',')
a= work1Pop.str.contains('&')
num= work1Pop.str.contains('\d')
semi= work1Pop.str.contains(';')

work1['PoP']= np.where(c, np.nan,
                       np.where(a, np.nan,
                                np.where(num, np.nan,
                                         np.where(semi, np.nan,
                                work1Pop.str.replace('-', ' ')))))


# In[222]:


#Standardizing and reordering the columns
final= work1.drop(['Place of Publication', 'Date of Publication'], axis= 1)
final= final.rename(columns={'DoP': 'Date of Publication', 'PoP': 'Place of Publication'})
columns= ['Place of Publication', 'Date of Publication','Publisher', 'Title', 'Author', 'Flickr URL']
final= final.reindex(columns=columns)


# In[228]:


final.to_csv('Documents/final.csv')


# In[226]:





# In[119]:





# In[125]:





# In[ ]:




