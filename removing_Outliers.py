#!/usr/bin/env python
# coding: utf-8


# Remove Outlayers 
"""
Outliers Removal Python Code
This Python script implements a method to remove outliers from a list of numbers using the lower and upper fences approach. Outliers are identified based on specified lower and upper fence values, and the script removes any data points falling outside this range.

Features:
Input: Accepts a list of numbers separated by commas.
Outliers Removal: Implements the lower and upper fences method to identify and remove outliers from the dataset.
Output: Displays the modified dataset with outliers removed.
Usage:
Run the script.
Enter a list of numbers separated by commas.
The script will display the modified dataset with outliers removed.

"""



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




