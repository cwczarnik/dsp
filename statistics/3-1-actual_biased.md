[Think Stats Chapter 3 Exercise 1](http://greenteapress.com/thinkstats2/html/thinkstats2004.html#toc31) (actual vs. biased)

Exercise 1   Something like the class size paradox appears if you survey children and ask how many children are in their family. Families with many children are more likely to appear in your sample, and families with no children have no chance to be in the sample.
Use the NSFG respondent variable NUMKDHH to construct the actual distribution for the number of children under 18 in the household.
Now compute the biased distribution we would see if we surveyed the children and asked them how many children under 18 (including themselves) are in their household.

Plot the actual and biased distributions, and compute their means. As a starting place, you can use chap03ex.ipynb.
```python
import numpy as np
import thinkstats2
import nsfg
import thinkplot
import matplotlib.pyplot as plt
%matplotlib inline
def BiasPmf(pmf, label):
    new_pmf = pmf.Copy(label=label)

    for x, p in pmf.Items():
        new_pmf.Mult(x, x)
        
    new_pmf.Normalize()
    return new_pmf


# read and find regular pmf 
resp = nsfg.ReadFemResp()
num_kids =resp['numkdhh']

reg_pmf = thinkstats2.Pmf(num_kids, label='actual')
thinkplot.PrePlot(2)
thinkplot.Pmf(reg_pmf)
thinkplot.Show(xlabel='Number of children', ylabel='PMF')
plt.show()

#bias pmf
biased_pmf = BiasPmf(reg_pmf, label='observed')
thinkplot.PrePlot(2)
thinkplot.Pmf(biased_pmf)
thinkplot.Show(xlabel='Number of children', ylabel='PMF')
plt.show()

thinkplot.PrePlot(2)
thinkplot.Pmfs([reg_pmf, biased_pmf])
thinkplot.Config(xlabel='Number of children', ylabel='PMF')
plt.show()
print('Actual mean', reg_pmf.Mean())
print('Observed mean', biased_pmf.Mean())
```

The means are calculated as:
```python
('Actual mean', 1.0242051550438309)
('Observed mean', 2.4036791006642821)
```
