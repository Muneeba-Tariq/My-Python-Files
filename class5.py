#!/usr/bin/env python
# coding: utf-8

# # list

# In[1]:


# list[element1, element2, element3]
#      0     1       2
l1 = [123, 'Bee', 'A.I']
#      -3    -2     -1
l1


# In[2]:


#dic[item1, item2, item3]
#item = key:value
d1 = {'id': 2,
     'name' : 'Bee',
     'course' : 'A.I',
     'admission' : '2019-12-15',
     'DOB' : '01-01-2000'}
d1


# In[3]:


d1 = {}
d1['id']=1
d1['name']='Bee'
d1['course']='A.I'
d1


# In[ ]:


# Task 1
# store id name and skill in dictionary with input function

info = {}   # empty dictionary
user_id = input("Entre your id")
info['id'] = user_id

name = input("Entre your name")
info['name'] = name

skills = 'python' + input("Entre your skills with ',' seprate value")
info['skills'] = skills.split()

info


# In[4]:


# dict[key]
d1 = {'id': 2,
     'name' : 'Bee',
     'course' : 'A.I',
     'admission' : '2019-12-15',
     'DOB' : '01-01-2000'}


d1['DOB']


# In[3]:


d1 = {'id': 2,
     'name' : 'Bee',
     'course' : 'A.I',
     'admission' : '2019-12-15',
     'DOB' : '01-01-2000'}

d1.clear()
d1


# In[5]:


d1 = {'id': 2,
     'name' : 'Bee',
     'course' : 'A.I',
     'admission' : '2019-12-15',
     'DOB' : '01-01-2000'}

d2=d1.copy() # Deep copy
d2["id"] = 5
print(d1)
print(d2)


# In[6]:


d1 = {}
d1['id']=None
d1['name']=None
d1['course']=None
d1


# In[7]:


l1 = ['id','name','course']
print(l1)

d1 = dict.fromkeys(l1)
print(d1)


# In[8]:


d1 = dict.fromkeys(l1,'NA')
print(d1)


# In[10]:


l1 = input("Entry comma seperated value")
l1 = l1.split(",")
print(l1)


# In[ ]:


l1 = input("Entry comma seperated value")
l1 = l1.split(",")
print(l1)

d1 = dict.fromkeys(l1,"NA")
print(d1)


# In[2]:


l1 = ['a','b','c']
l2 = ['x','y','z']

l3 = list(zip(l1,l2))
print(l3)

d1 = dict(l3)
print(d1)


# In[3]:


l1 = input("Entre name")
l1 = l1.split(",")
l2 = input("Entre value")
l2 = l2.split(",")

l3 = list(zip(l1,l2))

d1 = dict(l3)
print(d1)


# In[6]:


print(d1)
print(d1.get('a'))
print(d1.get('s'))  #if the key is not present then the error wont be generated- thanks to get function
print(d1.get('h',"value not available"))


# In[8]:


print(d1)
d1.items()


# In[9]:


print(d1)
d1.keys()


# In[10]:


print(d1)
d1.values()


# In[11]:


print(d1)
d1.pop('a')  #value


# In[13]:


print(d1)
print(d1.popitem())


# In[14]:


print(d1)
d1.setdefault('b')


# In[17]:


print(d1)
print(d1.setdefault('xyz'))
print(d1.setdefault('mno', 567))
print(d1)


# In[20]:


d1 = {'a':'AA','b':'BB'}

d2 = {'a':'AAAA','c':'CCCC'}

d1.update(d2)
d1


# In[31]:


d1 = {'a':1,
     'b':2,
     'c':3,
     'd':4,
     'e':5,
     'f':6,
     'g':7,
     'h':8,
     'i':9}

for i,j in sorted(d1.items(),reverse=True):
    print(i,j)


# In[35]:


from operator import itemgetter
d1 = {'a':1,
     'b':2,
     'c':3,
     'd':4,
     'e':5,
     'f':6,
     'g':7,
     'h':8,
     'i':9}

l1 = d1.keys()
l2 = d1.values()
l3 = list(zip(l1,l2))
l3.sort(key=itemgetter(1),reverse=True)
d1 = dict(l3)
print(d1)


# In[36]:


l1 = [('A',0,'Z'),
     ('B',1,'Y'),
     ('C',3,'X')]


# In[38]:


def abc(x):
    return x[0]
sorted(l1,key=abc)


# In[39]:


def abc(x):
    return x[1]
sorted(l1,key=abc)


# In[46]:


d1 = {'a':1,
     'b':2,
     'c':3,
     'd':4}

for k,v in (sorted(d1.items(), key=lambda x:x[1], reverse=True)):
    d2[k]=v
print(d2)


# In[ ]:


#list of student one info (id,name,skills)-> then l2,l3,l4...
#press x and all exits


# In[ ]:


lst=[]  #simple list to store all studend data
x=''  #initialize the exit comand with empty string
while x != 'x':
    dict1={}
    dict1['ID']=input('Enter ID: ')
    dict1['Name']=input('Enter Name: ')
    skills=input('Enter your skills')  #comma seperated skills
    dict1['skills']=skills.split()
    lst.append(dict1)  #append to lst
    x=input('Entre x to exit: ')  # if x
lst


# In[ ]:




