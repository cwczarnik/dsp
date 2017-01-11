import pandas as pd
import numpy as np
import re
import matplotlib.pyplot as plt

name_list = []
for i in df['name']:
    name_list.append(i.split(" " ))
first_names = []       
last_names = []
for i in name_list:
    first_names.append(i[0])
    last_names.append(i[-1])
    
df['first_name'] = first_names
df['last_name'] = last_names
temp_dict = {}
unique_last = set(last_names)
for row in np.array(df):
    temp_dict[row[-1]] = row[1:len(row)-2]
# define an empty dict
temp_dict = dict()

for row in np.array(df):
    # here define what key is, for example,
    key = row[-1]
    # check if key is already present in dict
    if key not in temp_dict:
        temp_dict[key] = []
    # append some value 
    temp_dict[key].append(list(row[1:len(row)-2]))

temp_dict_2 = {}

for row in np.array(df):
    temp_dict_2[ (row[-2],row[-1]) ] = row[1:len(row)-2]
'''
for k, v in temp_dict.iteritems():
    print k, v
'''
import operator
sorted_keys = sorted(temp_dict_2.keys(), key=operator.itemgetter(1))

##tried to make a single list    
for key in sorted_keys:
    print "%s: %s" % (key, temp_dict_2[key])

