# -*- coding: utf-8 -*-
"""
Created on Sun Sep  3 21:20:59 2023

@author: marko
"""

# initialize sum = 0 and count = 0
sum = 0
count = 0
# input full_name
full_name = input("Enter Full Name: ")
# input min price and convert to float
min_price = float(input("Enter Min Price: "))
# create a list of example prices
price_list = [69.0, 71.0, 84.5, 91.0, 67.4, 81.2, 84.6, 58.8, 79.3, 101.2]
# For loop
for price in price_list:
    sum = sum+price
    if price > min_price:
        count+=1
        
# print output
print(f'Hello {full_name}, the minimum price is {min_price}.')
print(f'There are {count} prices greater than the minimum price.')
print(f'The total price is {sum}')