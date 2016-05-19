# Basic Statistics

Python 2.7

### Mean
 - Add up the values in a data set and divide by the number of values.

<img src="https://github.com/gravity226/Understanding_Data_Science/imgs/mean_pic.png" height="200" width="200">

Example 1
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

Example 2
``` python
import numpy as np
values = np.array([1, 4, 2, 7, 9])

print values.mean()
```
``` output
> 4.6
```

Potential problems with using the mean:
 - If there are outliers your mean will be skewed.

Example 3
``` python
import numpy as np
values = np.array([3, 4, 7, 2, 4, 43])

print values.mean()
```
``` output
> 10.5
```

### Median
 - The middle value in your data set.

Example 1
``` python
values = [23, 12, 27, 99, 14, 37, 15]
values = sorted(values)

print values[len(values) / 2]
```
``` output
> 23
```

If you have an even number of sample values then 2 numbers should be returned

Example 2
``` python
values = [1, 2, 1, 6, 3, 0, 5, 5]
values = sorted(values)

middle = len(values) / 2
if len(values) % 2. == 0:
    print values[middle - 1: middle + 1]
else:
    print values[middle]
```
``` output
> [2, 3]
```

Example 3
``` python
import numpy as np

values = [1, 2, 1, 6, 3, 0, 5, 5]

print np.median(values)
```
``` output
> 2.5
```

### Mode
 - The value that appears most in a data set

Example 1
``` python
values = [1, 0, 3, 0, 5, 3, 1, 0]

mode = max(values, key=values.count)

print mode
```
``` output
> 0
```

If your data set has multiple numbers with the same count, the above example will only return one number.

Example 2
``` python
values = [1, 2, 3, 2, 5, 1, 0]
max_count = max(list(map(values.count, values)))

mode = list(set(filter(lambda n: values.count(n) == max_count, values)))

print mode
```
``` output
> [1, 2]
```
Reference:<br />
http://www.python-course.eu/lambda.php<br />
http://stackoverflow.com/questions/10797819/finding-the-mode-of-a-list-in-python<br />
