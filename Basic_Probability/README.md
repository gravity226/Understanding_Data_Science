# Basic Statistics

Python 2.7

### Sections
 - [Probability of an Event](https://github.com/gravity226/Understanding_Data_Science/tree/master/Basic_Statistics#probability-of-an-event)


### Probability of an Event
 -
"The probability of event A is the number of ways event A can occur divided by the total number of  possible outcomes." [reference](http://www.mathgoodies.com/lessons/vol6/intro_probability.html)

<img src="https://github.com/gravity226/Understanding_Data_Science/blob/master/imgs/mean_pic.png" height="100">

(img Reference: http://www.ablongman.com/graziano6e/text_site/MATERIAL/statconcepts/central.htm)

Example 1
``` python
# if you don't import division then you'll need to convert numbers to decimals before dividing
from __future__ import division

data = [1, 4, 2, 7, 9]

mean = sum(data) / len(data)

print mean
```
``` output
> 4.6
```
