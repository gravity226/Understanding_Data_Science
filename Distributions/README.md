# Distributions

Python 2.7

### Sections
 - [Normal Distribuation]()

### Normal Distribution
 - "In probability theory, the normal (or Gaussian) distribution is a very common continuous probability distribution. Normal distributions are important in statistics and are often used in the natural and social sciences to represent real-valued random variables whose distributions are not known."([reference](https://en.wikipedia.org/wiki/Normal_distribution))

<img src="https://github.com/gravity226/Understanding_Data_Science/blob/master/imgs/mean_pic.png" height="100">
([img reference](http://www.benlcollins.com/spreadsheets/histograms-normal-distribution/))

Example 1

What is the probability of rolling one number on a six sided fair die?
``` python
from __future__ import division
dice_sides = 6  # number of sides on the dice
one_num = 1     # number of possibilities to get one number

print one_num / dice_sides
```
``` output
> 0.166666666667
```
