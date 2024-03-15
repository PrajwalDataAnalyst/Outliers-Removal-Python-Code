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
class remove_outliers():
    def q1q3(self, num):
        ln = len(num)
        q1 = 25 / 100 * (ln + 1)
        q1 = num[int(q1) - 1]
        q3 = 75 / 100 * (ln + 1)
        q3 = num[int(q3) - 1]
        iqr = q3 - q1
        lf = q1 - 1.5 * iqr
        hf = q3 + 1.5 * iqr
        self.remove(num, lf, hf)

    def remove(self, num, lf, hf):
        outliers = []
        for i in range(len(num)):
            if num[i] <= lf or num[i] >= hf:
                outliers.append(num[i])
        print("Outliers:", outliers)
        print("Number of Outliers is = ", len(outliers))
        num[:] = [x for x in num if x not in outliers]
        print("Data without outliers:", num)

ro = remove_outliers()
num = input("Enter numbers separated by spaces: ").split()  # give input with space
num = list(map(int, num))  
ro.q1q3(num)
