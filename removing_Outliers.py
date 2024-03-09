#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# Remove Outlayers 


# In[140]:


class RemoveOutliers:
    i=0
    def q1(self, num):
        ln = len(num)
        q1 = (25 / 100) * (ln + 1)
        i = int(q1) - 1
        q1 = num[i]  # Q1 value
        q3 = (75 / 100) * (ln + 1)
        i = int(q3) - 1
        q3 = num[i]  # Q3 value
        iqr = q3 - q1
        self.fencing(q3, q1, iqr)  # Calling the method without assigning return value
        return q3, q1, iqr, lf, hf


    def fencing(self, q3, q1, iqr):
        lf = q1 - 1.5 * iqr
        hf = q3 + 1.5 * iqr
        return lf,hf
    def remove_out(self,lf,hf,num):
        lf=lf
        hf=hf
        num=num
        i=0
        c=0
        print("\n\n****************** WITH outliers *************\n\n",num)
        while i < len(num):
            if num[i] <= lf or num[i] >= hf: 
                num.remove(num[i]) 
                c+=1
                
            else:
                i += 1
        print("\n\n****************REMOVED THE outliers****************** \n\n",num)   
        print("\n\n Their Are ",c," outliers")
RO = RemoveOutliers()
num = input("enter the number with commma sept ")

num=list(map(int,num.split(",")))
print(num)
q3, q1, iqr, lf, hf = RO.q1(num)
print("Lower fence:", lf)
print("Higher fence:", hf)
RO.remove_out(lf,hf,num)


# In[ ]:





# In[ ]:





# In[ ]:




