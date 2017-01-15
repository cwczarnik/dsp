[Think Stats Chapter 5 Exercise 1](http://greenteapress.com/thinkstats2/html/thinkstats2006.html#toc50) (blue men)

Exercise 1   In the BRFSS (see Section 5.4), the distribution of heights is roughly normal with parameters µ = 178 cm and σ = 7.7 cm for men, and µ = 163 cm and σ = 7.3 cm for women. In order to join Blue Man Group, you have to be male between 5’10” and 6’1” (see http://bluemancasting.com). What percentage of the U.S. male population is in this range? Hint: use scipy.stats.norm.cdf.

```python

import scipy.stats
mu = 178
sigma = 7.7
dist = scipy.stats.norm(loc=mu, scale=sigma)
print(dist.mean(), dist.std())
first_height = 152.4 +25.4 # 5ft  and 10 inches  in cm
second_height = 182.88 + 2.54 # 6 ft and 1 inch in cm

#finding the cdf of both heights and taking the difference to get what is the area under the pmf between the two heights.
cdf_interval = dist.cdf(second_height) - dist.cdf(first_height)

#The cdf prints out the probability of a random varaible being less than our value of interest.
# For us this is the percentage difference of the height between 5ft 10 inches and 6 ft 1 inch.


print('Percentage of males between two heights in the population: ',cdf_interval)
```

The answer is 0.343 or about 34.3 percent of the U.S. male population between 5ft 10 inches and 6 ft 1 inch.
