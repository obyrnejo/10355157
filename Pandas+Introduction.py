
# coding: utf-8

# In[3]:

import numpy as np
import pandas as pd


# In[5]:

s = pd.Series(np.random.randn(5), index=['a', 'b', 'c', 'd','e'])


# In[6]:

s


# In[7]:

s.index


# In[9]:

pd.Series(np.random.randn(5))


# In[10]:

d = {'a' : 0., 'b' : 1., 'c' : 2.}


# In[11]:

pd.Series(d)


# In[12]:

pd.Series(d, index=['b', 'c', 'd', 'a'])


# In[13]:

pd.Series(5., index=['a', 'b', 'c', 'd', 'e'])


# In[14]:

s


# In[15]:

s[0]


# In[16]:

s[:3]


# In[17]:

s[s > s.median()]


# In[18]:

s[[4, 3, 1]]


# In[19]:

np.exp(s)


# In[20]:

s['a']


# In[21]:

s['e'] = 12.


# In[22]:

s


# In[23]:

'e' in s


# In[24]:

'f' in s


# In[25]:

s['f']


# In[26]:

s.get('f')


# In[27]:

s.get('f', np.nan)


# In[28]:

s + s


# In[29]:

s*2


# In[30]:

np.exp(s)


# In[31]:

s[1:] + s[:-1]


# In[32]:

s = pd.Series(np.random.randn(5), name='something')



# In[33]:

s


# In[34]:

s.name


# In[35]:

s2 = s.rename("different")



# In[36]:

s2.name


# In[37]:

d = {'one' : pd.Series([1., 2., 3.], index=['a', 'b', 'c']),
    'two' : pd.Series([1., 2., 3., 4.], index=['a', 'b', 'c', 'd'])}



# In[38]:

d


# In[39]:

df = pd.DataFrame(d)


# In[40]:

df


# In[41]:

pd.DataFrame(d, index=['d', 'b', 'a'])


# In[42]:

pd.DataFrame(d, index=['d', 'b', 'a'], columns=['two', 'three']) 


# In[43]:

df.index


# In[44]:

df.columns


# In[45]:

d = {'one' : [1., 2., 3., 4.],
    'two' : [4., 3., 2., 1.]}
 


# In[46]:

pd.DataFrame(d)


# In[47]:

pd.DataFrame(d, index=['a', 'b', 'c', 'd'])


# In[48]:

data = np.zeros((2,), dtype=[('A', 'i4'),('B', 'f4'),('C', 'a10')])


# In[49]:

data[:] = [(1,2.,'Hello'), (2,3.,"World")]



# In[50]:

pd.DataFrame(data)


# In[51]:

pd.DataFrame(data, index=['first', 'second'])


# In[52]:

pd.DataFrame(data, columns=['C', 'A', 'B'])


# In[53]:

data2 = [{'a': 1, 'b': 2}, {'a': 5, 'b': 10, 'c': 20}]


# In[54]:

pd.DataFrame(data2)


# In[55]:

pd.DataFrame(data2, index=['first', 'second'])


# In[56]:

pd.DataFrame(data2, columns=['a', 'b'])


# In[57]:

pd.DataFrame({('a', 'b'): {('A', 'B'): 1, ('A', 'C'): 2},
             ('a', 'a'): {('A', 'C'): 3, ('A', 'B'): 4},
             ('a', 'c'): {('A', 'B'): 5, ('A', 'C'): 6},
             ('b', 'a'): {('A', 'C'): 7, ('A', 'B'): 8},
             ('b', 'b'): {('A', 'D'): 9, ('A', 'B'): 10}})
 


# In[58]:

data


# In[59]:

pd.DataFrame.from_records(data, index='C')


# In[60]:

pd.DataFrame.from_items([('A', [1, 2, 3]), ('B', [4, 5, 6])])



# In[61]:

pd.DataFrame.from_items([('A', [1, 2, 3]), ('B', [4, 5, 6])],
                        orient='index', columns=['one', 'two', 'three'])
 


# In[62]:

df


# In[63]:

df['one']


# In[64]:

df['three'] = df['one'] * df['two']


# In[65]:

df['flag'] = df['one'] > 2


# In[66]:

df


# In[67]:

del df['two']


# In[68]:

three = df.pop('three')


# In[70]:

df


# In[71]:

df['foo'] = 'bar'


# In[72]:

df


# In[73]:

df['one_trunc'] = df['one'][:2]



# In[74]:

df


# In[75]:

df.insert(1, 'bar', df['one'])


# In[76]:

df


# In[ ]:



