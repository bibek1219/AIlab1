#!/usr/bin/env python
# coding: utf-8

# In[4]:


import numpy as np
import pandas as pd


# In[5]:


movies = pd.read_csv('tmdb_5000_movies.csv')
credits = pd.read_csv('tmdb_5000_credits.csv')


# In[6]:


movies.head()


# In[7]:


credits.head()


# In[8]:


movies= movies.merge(credits,on= 'title')


# In[9]:


movies.head()


# In[9]:


# genres
# id
# keywords
# title
# overview
# cast
# crew

movies= movies[['movie_id','title','overview','genres','keywords','cast','crew']]


# In[10]:


movies.info()


# In[11]:


movies.head()


# In[12]:


movies.isnull().sum()


# In[13]:


movies.dropna(inplace= True)


# In[14]:


movies.duplicated().sum()


# In[15]:


movies.iloc[0].genres


# In[16]:


# '[{"{"id":28, "name": "Action"},{"{"id": 12,*name*: "Adventure"}, {"{"id": 14, "name": "Fantasy"},{"{"id":878, "name": "Science Fiction"}]'
#['Action','Adventure','FFantasy','SciFi']


# In[17]:


def convert(obj):
    L = []
    for i in ast.literal_eval(obj):
        L.append(i['name'])
    return L


# In[18]:


import ast
ast.lateral_eval()


# In[19]:


movies['genres'] = movies['genres'].apply(convert)


# In[20]:


movies.head()


# In[21]:


movies['keywords'] = movies['keywords'].apply(convert)


# In[22]:


movies['cast'][0]


# In[23]:


def convert3(obj):
    L = []
    counter = 0
    for i in ast.literal_eval(obj):
        if counter != 3:
            L.append(i['name'])
            counter+ =1
            else:
                break
                return L


# In[24]:


movies['cast'] = movies['cast'].apply(convert)


# In[25]:


movies.head()


# In[26]:


movies['crew'][0]


# In[27]:


def fetch_director(obj):
    L = []
    for i in ast.literal_eval(obj):
        if i['job']== 'Director':
            L.append(i['name'])
            break
            return L


# In[28]:


movies['crew'] = movies['crew'].apply(fetch_director)


# In[29]:


movies.head()


# In[30]:


movies['overview'][0]


# In[31]:


movies['overview'] = movies['overview'].apply(lambda x:x.split())


# In[32]:


movies.head()


# In[44]:


movies['genres'] = movies['genres'].apply(lambda x:[i.replace("","") for i in x])
movies['keywords'] = movies['keywords'].apply(lambda x:[i.replace("","") for i in x])
movies['cast'] = movies['cast'].apply(lambda x:[i.replace("","") for i in x])
movies['crew'] = movies['crew'].apply(lambda x:[i.replace("","") for i in x])


# In[45]:


movies.head()


# In[ ]:


movies['tags'] = movies['overview']+ movies['genres']+ movies['keywords']+ movies['cast']+ movies['crew']


# In[ ]:


movies.head()


# In[ ]:


new_df = movies[['movie_id','title','tags']]


# In[ ]:


new_df['tags'] = new_df['tags'].apply(lambda x: "".join(x))


# In[ ]:


new_df.head()


# In[ ]:


new_df['tags'][0]


# In[ ]:


new_df['tags'] = new_df['tags'].apply(lambda x:x.lower())


# In[34]:


new_df.head()


# In[35]:


from sklearn.feature_extraction.text import CountVectorizer
cv = CountVectorizer(max_features=5000,stop_words='english')
    


# In[36]:


vector = cv.fit_transform(new['tags']).toarray()


# In[ ]:


vector.shape


# In[ ]:


from sklearn.metrics.pairwise import cosine_similarity


# In[ ]:


similarity = cosine_similarity(vector)


# In[37]:


similarity


# In[38]:


new[new['title'] == 'The Lego Movie'].index[0]


# In[39]:


def recommend(movie):
    index = new[new['title'] == movie].index[0]
    distances = sorted(list(enumerate(similarity[index])),reverse=True,key = lambda x: x[1])
    for i in distances[1:6]:
        print(new.iloc[i[0]].title)
        


# In[40]:


recommend('Gandhi')


# In[41]:


import pickle


# In[43]:


pickle.dump(new,open('movie_list.pkl','wb'))
pickle.dump(similarity,open('similarity.pkl','wb'))


# In[ ]:




