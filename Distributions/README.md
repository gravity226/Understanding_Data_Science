# Distributions

Python 2.7

### Sections
 - [Normal Distribuation](https://github.com/gravity226/Understanding_Data_Science/tree/master/Distributions#normal-distribution)

### Normal Distribution
 - "In probability theory, the normal (or Gaussian) distribution is a very common continuous probability distribution. Normal distributions are important in statistics and are often used in the natural and social sciences to represent real-valued random variables whose distributions are not known." ([reference](https://en.wikipedia.org/wiki/Normal_distribution))

<img src="https://github.com/gravity226/Understanding_Data_Science/blob/master/imgs/normald.jpg" height="300">
([img reference](http://www.benlcollins.com/spreadsheets/histograms-normal-distribution/))

Example 1

What is the probability of rolling one number on a six sided fair die?
``` python
import numpy as np
import matplotlib.pyplot as plt

data = np.random.normal(size=1000)
plt.hist(data, bins=25)
plt.show()
```
<img src="https://github.com/gravity226/Understanding_Data_Science/blob/master/imgs/normalD1.png" height="300">
