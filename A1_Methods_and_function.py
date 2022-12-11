#!/usr/bin/env python
# coding: utf-8

# Write a function that computes the volume of a sphere given its radius.

# In[3]:


def vol(rad):
    volume=((4/3)*(3.14)*(rad**3))
    return volume


# In[4]:


vol(2)


# Write a function that checks whether a number is in a given range (inclusive of high and low)

# In[12]:


def ran_check(num,low,high+1):
    if num in range(low,high):
        return f'{num} is in range between {low} and {high}'


# In[13]:


ran_check(5,2,7)


# In[18]:


def ran_bool(num,low,high):
    return num in range(low,high+1)


# In[19]:


ran_bool(3,1,10)


# In[20]:


ran_bool(1,3,10)


# In[21]:


ran_bool(10,3,10)


# Write a Python function that accepts a string and calculates the number of upper case letters and lower case letters.

# In[44]:


def up_low(s):
    uplist=[]
    lowlist=[]
    for letter in s:
        if letter.isupper():
            uplist.append(letter)
        elif letter.islower():
            lowlist.append(letter)
    print (f"original string is {s}")
    print (f"Number of uppercase letters is {len(uplist)}")
    print (f"Number of lowercase letters is {len(lowlist)}")


# In[45]:


s = 'Hello Mr. Rogers, how are you this fine Tuesday?'
up_low(s)


# In[26]:


s = 'Hello Mr. Rogers, how are you this fine Tuesday?'
for let in s:
    if let.isupper():
        print(let)


# Write a Python function that takes a list and returns a new list with unique elements of the first list.

# In[54]:


def unique_list(lst):
    return (list(set(lst)))
    


# In[55]:


unique_list([1,1,1,1,2,2,3,3,3,3,4,5])


# Write a Python function to multiply all the numbers in a list.

# In[56]:


def multiply(numbers):
    fnum=1
    for num in numbers:
        fnum*=num
    return fnum


# In[57]:


multiply([1,2,3,-4])


# Write a Python function that checks whether a word or phrase is palindrome or not.

# In[62]:


s="God of war"
for let in s:
    if let==' ':
        continue
    else:
        print(let)


# In[67]:


s="God of war"
for let in s:
    print(let)


# In[68]:


c="god of war"
sample=[]
for lett in c:
    sample.append(lett)


# In[72]:


print(list(c)==sample)


# In[71]:


sample


# In[73]:


c


# In[89]:


def palindrome(s):
    lst=[]
    for let in s:
        if let==' ':
            continue
        else:
            lst.append(let)
    if lst[::-1]==lst:
        print("It is a palindrome")
    else:
        print("Not a palindrome")
            


# In[90]:


palindrome("Hello")


# In[91]:


palindrome("madam")


# In[92]:


palindrome("nurses run")


# In[85]:


v="nurses run"
k=[]
for lettt in v:
    if lettt==' ':
        continue
    else:
        k.append(lettt)


# In[86]:


k


# In[87]:


list(v)


# In[88]:


k==list(v)


# In[93]:


palindrome('helleh')


# Write a Python function to check whether a string is pangram or not. (Assume the string passed in does not have any punctuation)

# In[95]:


import string
list(string.ascii_lowercase)


# In[96]:


list(string.ascii_letters)


# In[151]:


def ispangram(str1):
    lst=[]
    alphabet=list(string.ascii_lowercase)
    for let in str1:
        if let==" ":
            continue
        else:
            lst.append(let)
    print(lst)
    for letter in alphabet[0]:
        if letter in lst:
            alphabet.remove(letter)
    print(len(alphabet))
    if len(alphabet)==0:
        print("It is a panagram")
    else:
        print("it is not an panagram")


# In[152]:


ispangram("The quick brown fox jumps over the lazy dog")


# In[99]:


str2="The quick brown fox jumps over the lazy dog"
lst3=list(string.ascii_lowercase)


# In[107]:


list(lst3)


# In[112]:


c=list("The quick brown fox jumps over the lazy dog")
print(c)


# In[114]:


c.pop("t")
print(c)


# In[120]:


d=list(string.ascii_lowercase)
 


# In[121]:


print(d)


# In[122]:


d.pop(0)


# In[125]:


d[0]


# In[131]:


alphabet=list(string.ascii_lowercase)


# In[141]:


for letter in alphabet[0]:
    print(str(letter))


# In[147]:


alphabet.remove("b")


# In[148]:


alphabet


# In[153]:


import string

def ispangram(str1, alphabet=string.ascii_lowercase): 
    # Create a set of the alphabet
    alphaset = set(alphabet)  
    
    # Remove spaces from str1
    str1 = str1.replace(" ",'')
    
    # Lowercase all strings in the passed in string
    # Recall we assume no punctuation 
    str1 = str1.lower()
    
    # Grab all unique letters in the string as a set
    str1 = set(str1)
    
    # Now check that the alpahbet set is same as string set
    return str1 == alphaset


# In[154]:


ispangram("The quick brown fox jumps over the lazy dog")


# In[171]:


c="The quick brown fox jumps over the lazy dog"
c=c.replace(" ","")
c=c.lower()


# In[172]:


print(c)


# In[173]:


d=set(c)
print(d)


# In[174]:


alphabet=string.ascii_lowercase


# In[175]:


alphaset = set(alphabet) 


# In[176]:


alphaset


# In[179]:


alphaset==d


# In[ ]:




