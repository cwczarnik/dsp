import pandas as pd
import numpy as np
import re
import matplotlib.pyplot as plt

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
        deg_list.append(j)
unique_degrees = set(deg_list)


##standardize the degrees to count them up
p = re.compile('(Ph(.)D(.)|Ph(.)D)')
deg_list = [p.sub('PhD', string) for string in deg_list]
           
p = re.compile('(Sc(.)D(.)|Sc(.)D)')
deg_list= [p.sub('ScD', string) for string in deg_list]

p = re.compile('(M(.)S(.))')
deg_list= [p.sub('ScD', string) for string in deg_list]

 #remove space value and zero        
for i, n in enumerate(deg_list):
    if n == '':
       del deg_list[i]
    elif n == "0":
        del deg_list[i]
           
#print(deg_list)        
print(count_freq(deg_list))
#print(unique_degrees)
##this shows the frequency of degrees


p = re.compile('(M(.)S(.))')
deg_list= [p.sub('ScD', string) for string in deg_list]

prof_list = df.ix[:,2]

p = re.compile('Assistant Professor is Biostatistics')
prof_list= [p.sub('Assistant Professor in Biostatistics', string) for string in prof_list]


prof_dict  = count_freq(prof_list)
print(prof_dict)

print 'number of titles:', len(set(prof_dict))
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
