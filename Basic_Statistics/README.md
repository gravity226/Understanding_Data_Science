# Basic Statistics
Python 2.7

### Mean
 - Add up the values in a sample and divide by the number of values.

##### Example 1
``` python
# if you don't import division then you'll need to convert numbers to decimals before dividing
from __future__ import division

values = [1, 4, 2, 7, 9]

mean = sum(values) / len(values)

print mean
```
``` output
> 4.6
```

##### Example 2
``` python
import numpy as np
values = np.array([1, 4, 2, 7, 9])

print values.mean()
```
``` output
> 4.6
```

Potential problems with using the mean:
 - If there are very large outliers in your dataset it will skew the mean.

##### Example 3
``` python
import numpy as np
values = np.array([3, 4, 7, 2, 4, 43])

print values.mean()
```
``` output
> 10.5
```
