[Think Stats Chapter 2 Exercise 4](http://greenteapress.com/thinkstats2/html/thinkstats2003.html#toc24) (Cohen's d)

Exercise 4   Using the variable totalwgt_lb, investigate whether first babies are lighter or heavier than others. Compute Cohen’s d to quantify the difference between the groups. How does it compare to the difference in pregnancy length?

1.) find the Cohen'd d coeficcient for the first babies and then the others.
2.) look at the pregnancy lengths for first and others. This is already done, qouting the book, " the difference in means is 0.029 standard deviations, which is small"

Looking at the birth order and preforming the calculation for the coefficient
```python

import numpy as np
import thinkstats2
import nsfg
import first

def main(script):
    """Tests the functions in this module.

    script: string script name
    """
    
    pregnancies = nsfg.ReadFemPreg()
    live_birth = pregnancies[pregnancies['outcome'] == 1]
    firsts = live_birth[live_birth.birthord == 1]
    others = live_birth[live_birth.birthord != 1]
    cohen = thinkstats2.CohenEffectSize(firsts['totalwgt_lb'],others['totalwgt_lb'])
    return(cohen)

if __name__ == '__main__':
    print(main(*sys.argv))
```
The Cohen's d coefficient:  -0.0886729270726.
This implies that there is a small difference in means of weights, but that the first born weight means are less than the means of the other births, this is according to the sign of the coefficient. According to wikipedias article on the Cohen d coefficient, the lower coefficient usually implies a need for more samples. 
