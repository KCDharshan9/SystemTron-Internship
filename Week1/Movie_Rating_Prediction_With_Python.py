#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import pandas as pd
import ast
import pickle
from sklearn.feature_extraction.text import CountVectorizer
from nltk.stem.porter import PorterStemmer
from sklearn.metrics.pairwise import cosine_similarity as cs


# In[2]:


mvs = pd.read_csv('tmdb_5000_movies.csv')
crd = pd.read_csv('tmdb_5000_credits.csv')


# In[3]:


movies = mvs.merge(crd, on = 'title')
movies.head()


# In[4]:


movies = movies[['movie_id', 'title', 'overview', 'genres', 'keywords', 'cast', 'crew']]
movies.head()


# In[5]:


#Check for null values
movies.isnull().sum()


# In[6]:


#Remove null values
movies.dropna(inplace = True)


# In[7]:


movies.isnull().sum()


# In[8]:


#Check for duplicated values
movies.duplicated().sum()


# In[9]:


movies.iloc[0].genres


# In[10]:


def convert(obj):
    m_list = []
    for i in ast.literal_eval(obj): # ast.literal_eval() - parses the string and converts it directly into its corresponding data type (like a list, dictionary, or number)
        m_list.append(i['name'])
    return m_list


# In[11]:


#Converts and combines all genres in dictionary form to a proper list
movies['genres'] = movies['genres'].apply(convert)
movies.head()


# In[12]:


#Converts and combines all keywords in dictionary form to a proper list
movies['keywords'] = movies['keywords'].apply(convert)
movies.head()


# In[13]:


def convertcast(obj):
    c_list = []
    counter = 0 #using counter to consider only top three cast
    for i in ast.literal_eval(obj): # ast.literal_eval() - parses the string and converts it directly into its corresponding data type (like a list, dictionary, or number)
        if (counter != 3):
            c_list.append(i['name'])
            counter += 1
        else:
            break

    return c_list


# In[14]:


#Converts and combines only top three cast in dictionary form to a proper list
movies['cast'] = movies['cast'].apply(convertcast)
movies.head()


# In[15]:


def convertcrew(obj):
    d_list = []
    for i in ast.literal_eval(obj): # ast.literal_eval() - parses the string and converts it directly into its corresponding data type (like a list, dictionary, or number)
        if (i['job'] == 'Director'): # check and append only the director name
            d_list.append(i['name'])
            break

    return d_list


# In[16]:


movies['crew'] = movies['crew'].apply(convertcrew)
movies.head()


# In[17]:


# convert string into list (overview)
movies['overview'] = movies['overview'].apply(lambda x: x.split())
movies.head()


# In[18]:


# stripping all whitespace of same words in genres, keywords, cast, & crew columns
movies['genres'] = movies['genres'].apply(lambda x: [i.replace(" ", "") for i in x])
movies['keywords'] = movies['keywords'].apply(lambda x: [i.replace(" ", "") for i in x])
movies['cast'] = movies['cast'].apply(lambda x: [i.replace(" ", "") for i in x])
movies['crew'] = movies['crew'].apply(lambda x: [i.replace(" ", "") for i in x])

movies.head()


# In[19]:


# combine all genres, keywords, cast, & crew columns into one column
movies['tags'] = movies['overview'] + movies['genres'] + movies['keywords'] + movies['cast'] + movies['crew']
movies.head()


# In[20]:


# create a new dataframe including movie id, movie title and its tags
new_df = movies[['movie_id', 'title', 'tags']]
new_df.head()


# In[21]:


# convert the list in tags column into string
new_df['tags'] = new_df['tags'].apply(lambda x: " ".join(x))
new_df.head()


# In[22]:


# comvert all the tags into lower case
new_df['tags'] = new_df['tags'].apply(lambda x: x.lower())
new_df['tags'][0]


# In[23]:


# convert similar words into one using stemming method
ps = PorterStemmer()

def stem(text):
    abc = []

    for i in text.split():
        abc.append(ps.stem(i))

    return " ".join(abc)


# In[24]:


new_df['tags'] = new_df['tags'].apply(stem)


# In[25]:


# using scikit learn classes to turn words into number using vectorization method
cv = CountVectorizer(max_features = 5000, stop_words = 'english')


# In[26]:


vectors = cv.fit_transform(new_df['tags']).toarray()
vectors


# In[27]:


cv.get_feature_names_out()


# In[28]:


# find the similarity between movies
similarity = cs(vectors)
similarity.shape


# In[29]:


# recommend similar movies

def recommend(movie):
    movie_index = new_df[new_df['title'] == movie].index[0]
    distances = similarity[movie_index]
    movies_list = sorted(list(enumerate(distances)), reverse = True, key = lambda x: x[1])[1:6]

    rec = []
    for i in movies_list:
        rec.append(new_df.iloc[i[0]].title)

    return rec


# In[30]:


recommend('John Carter')


# In[31]:


# extract all movies for streamlit
pickle.dump(new_df, open('movies.pkl', 'wb'))

