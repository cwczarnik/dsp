import pandas as pd
import numpy as np
import re
import matplotlib.pyplot as plt
import pprint
pp = pprint.PrettyPrinter(indent=1)
df = pd.read_csv('faculty.csv')
df.columns =[u'name', u'degree', u'title', u'email'] 
#print(df.head())

def count_freq(column):
    freq_dict ={}
    for i in column:
        if freq_dict.get(i,False):
            freq_dict[i] += 1 
        else:
            freq_dict[i] = 1
    return(freq_dict)

def break_string(list_val):
    string_split = []
    for i in list_val:
        string_split.append(i.split(" "))  
    return(string_split)
        
degree_list_by_person = break_string(df.ix[:,1])
#collect all values of degree for those with multiple degrees
deg_list = []
for deg in degree_list_by_person:
    for j in deg:
        if j =='0' or j =='':
            pass
        else:
            deg_list.append(j)

##standardize the degrees to count them up
p = re.compile('(Ph(.)D(.)|Ph(.)D)')
deg_list = [p.sub('PhD', string) for string in deg_list]
           
p = re.compile('(Sc(.)D(.)|Sc(.)D)')
deg_list= [p.sub('ScD', string) for string in deg_list]

p = re.compile('(M(.)S(.))')
deg_list= [p.sub('ScD', string) for string in deg_list]

print(count_freq(deg_list))

##this shows the frequency of degrees

prof_list = df.ix[:,2]

p = re.compile('Assistant Professor is Biostatistics')
prof_list= [p.sub('Assistant Professor of Biostatistics', string) for string in prof_list]

p = re.compile('Assistant Professor in Biostatistics')
prof_list= [p.sub('Assistant Professor of Biostatistics', string) for string in prof_list]
prof_dict  = count_freq(prof_list)
print(prof_dict)

print('number of titles:', len(set(prof_dict)))
##
df['email'].to_csv('email.csv')

#re.findall(r'[\w\.-]+@[\w\.-]+', df.ix[:,3])
##find all email domains

import re
email_pattern = "\A[a-z0-9!#$%&'*+/=?^_`{|}~-]+(?:\.[a-z0-9!#$%&'*+/=?^_`{|}~-]+)*@(?:[a-z0-9](?:[a-z0-9-]*[a-z0-9])?\.)+"
email_domain_pattern =  "@(?:[a-z0-9](?:[a-z0-9-]*[a-z0-9])?\.)+"                   
EMAIL_REGEX = re.compile(email_domain_pattern)

domain_list = []
email_series = df.ix[:,3]
for email in email_series:
    domain = re.search("@[\w.]+", email)
    domain_list.append(domain.group())
unique_domains = set(domain_list)
print(unique_domains)

## split names up into separate both first and last name

##make the last name a key, the values are the other 

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
    pp.pprint( "%s: %s" % (key, temp_dict_2[key]))


