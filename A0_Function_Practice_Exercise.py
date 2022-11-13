#!/usr/bin/env python
# coding: utf-8

# WARMUP SECTION:
# LESSER OF TWO EVENS: Write a function that returns the lesser of two given numbers if both numbers are even, but returns the greater if one or both numbers are odd

# In[1]:


def lesser_of_two_evens(x,y):
    if x%2==0 and y%2==0:
        return min(x,y)
    else:
        return max(x,y)


# In[2]:


lesser_of_two_evens(2,4)


# In[3]:


lesser_of_two_evens(2,5)


# In[5]:


name="Naveen kumar"
name.split()


# ANIMAL CRACKERS: Write a function takes a two-word string and returns True if both words begin with same letter
# animal_crackers('Levelheaded Llama') --> True

# In[21]:


def animal_crackers(name):
    my_list=name.split()
    if my_list[0][0]==my_list[1][0]:
        return True
    else:
        return False


# In[22]:


animal_crackers('Levelheaded Llama')


# In[23]:


animal_crackers('Crazy Kangaroo')


# In[27]:


name="Naveen kumar R"
name.split()


# In[28]:


List2=name.split()


# In[29]:


List2


# In[31]:


List2[0]


# MAKES TWENTY: Given two integers, return True if the sum of the integers is 20 or if one of the integers is 20. If not, return False

# In[34]:


def makes_twenty(x,y):
    if x+y==20 or x==20 or y==20:
        return True
    else:
        return False


# In[35]:


makes_twenty(20,10) 


# In[36]:


makes_twenty(12,8)


# In[37]:


makes_twenty(2,3)


# In[38]:


def old_macdonald(name):
    out_name=name[:3].capitalize()+name[3:].capitalize()
    return out_name


# In[39]:


old_macdonald('macdonald')


# In[59]:


def master_yoda(name):
    my_list=name.split()
    my_list.reverse()
    return my_list


# In[60]:


name="I am in Home"
mlist=name.split()


# In[61]:


mlist


# In[62]:


mlist.reverse()


# In[63]:


mlist


# In[64]:


master_yoda('I am home')


# In[65]:


master_yoda('We are ready')


# In[68]:


def almost_there(n):
    if (n<=110 and n>=90) or (n<=210 and n>=190):
        return True
    else:
        return False


# In[69]:


almost_there(104)


# In[70]:


almost_there(150)


# In[71]:


almost_there(209)


# In[ ]:





# LEVEL 2

# In[98]:


def has_33(my_list):
    for num in range(0,len(my_list)):
        if my_list[num]==3:
            if my_list[num+1]==3:
                return True
            else:
                return False
           


# In[99]:


has_33([1, 3, 3])


# In[89]:


for num in range(0,len(List2)+1):
    
    print(num)


# In[90]:


List3=[1,2,3,4,5]


# In[97]:


for num in range(0,len(List3)):
    if List3[num]==3:
        print(num,List3[num])


# In[100]:


has_33([1, 3, 1, 3])


# In[101]:


has_33([3, 1, 3])


# PAPER DOLL

# In[116]:


def paper_doll(text):
    string1=""
    for letter in text:
        string1=string1+letter*3
    return string1


# In[117]:


paper_doll('Hello')


# In[118]:


paper_doll('Mississippi')


# BLACK JACK

#  Given three integers between 1 and 11, if their sum is less than or equal to 21, return their sum. If their sum exceeds 21 and there's an eleven, reduce the total sum by 10. Finally, if the sum (even after adjustment) exceeds 21, return 'BUST'

# In[125]:


def blackjack(a,b,c):
    if a+b+c<=21:
        return(a+b+c)
    elif a+b+c>21:
        if (a==11 or b==11 or c==11):
            x=(a+b+c)-10
            if x>21:
                return("BUST")
            else:
                return x
        else:
            return("BUST")


# In[126]:


blackjack(5,6,7)


# In[127]:


blackjack(9,9,9)


# In[128]:


blackjack(9,9,11)


# SUMMER OF 69
# 
# SUMMER OF '69: Return the sum of the numbers in the array, except ignore sections of numbers starting with a 6 and extending to the next 9 (every 6 will be followed by at least one 9). Return 0 for no numbers.

# In[141]:


def summer_69(arr):
    total = 0
    add = True
    for num in arr:
        while add:
            if num != 6:
                total += num
                break
            else:
                add = False
        while not add:
            if num != 9:
                break
            else:
                add = True
                break
    return (f"Total is {total} ")


# In[142]:


summer_69([1, 3, 5])


# In[143]:


summer_69([4, 5, 6, 7, 8, 9]) 


# In[144]:


summer_69([2, 1, 6, 9, 11])


# CHALLENGE PROBLEMS
# 
# SPY GAME: Write a function that takes in a list of integers and returns True if it contains 007 in order
#  spy_game([1,2,4,0,0,7,5]) --> True
#  spy_game([1,0,2,4,0,5,7]) --> True
#  spy_game([1,7,2,0,4,5,0]) --> False

# In[145]:


def spy_game(nums):

    code = [0,0,7,'x']
    
    for num in nums:
        if num == code[0]:
            code.pop(0)   # code.remove(num) also works
       
    return len(code) == 1


# In[146]:


spy_game([1,2,4,0,0,7,5])


# In[147]:


spy_game([1,7,2,0,4,5,0])


# COUNT PRIMES: Write a function that returns the number of prime numbers that exist up to and including a given number
# count_primes(100) --> 25

# In[148]:


def count_primes(num):
    for i in range(2,num):
        if num%i==0:
            print(num)


# In[ ]:





# In[ ]:




