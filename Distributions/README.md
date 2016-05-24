# Distributions

Python 2.7

### Sections
 - [Normal Distribuation](https://github.com/gravity226/Understanding_Data_Science/tree/master/Distributions#normal-distribution)

### Normal Distribution
 - "In probability theory, the normal (or Gaussian) distribution is a very common continuous probability distribution. Normal distributions are important in statistics and are often used in the natural and social sciences to represent real-valued random variables whose distributions are not known." ([reference](https://en.wikipedia.org/wiki/Normal_distribution))

<img src="https://github.com/gravity226/Understanding_Data_Science/blob/master/imgs/normald.jpg" height="300">
([img reference](http://www.benlcollins.com/spreadsheets/histograms-normal-distribution/))

Example 1

Making a graph from a random dataset.
``` python
import numpy as np
import matplotlib.pyplot as plt
plt.clf() # clear figure

data = np.random.normal(size=1000)
plt.hist(data, bins=25)
plt.show()
```
<img src="https://github.com/gravity226/Understanding_Data_Science/blob/master/imgs/normalD1.png" height="200">

Example 2
``` python
# reference: http://docs.scipy.org/doc/numpy-1.10.1/reference/generated/numpy.random.normal.html#numpy.random.normal
import numpy as np
import matplotlib.pyplot as plt
plt.clf() # clear figure

mu, sigma = 0, 0.1
data = np.random.normal(mu, sigma, 1000)
count, bins, ignored = plt.hist(data, bins=25, normed=True)
plt.plot(bins,
         1/(sigma * np.sqrt(2 * np.pi)) * np.exp( - (bins - mu)**2 / (2 * sigma**2) ),
         linewidth=2,
         color='r')
plt.show()
```
<img src="https://github.com/gravity226/Understanding_Data_Science/blob/master/imgs/normalD2.png" height="200">
