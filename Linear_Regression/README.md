# Linear Regression

Python 2.7

### Sections
 - [Summary](https://github.com/gravity226/Understanding_Data_Science/tree/master/Linear_Regression#summary)

<b>Linear Form</b>
 - [Linear Equation](https://github.com/gravity226/Understanding_Data_Science/tree/master/Linear_Regression#linear-equation)
 - [Slope](https://github.com/gravity226/Understanding_Data_Science/tree/master/Linear_Regression#linear-slope)
 - [Linear Intercept](https://github.com/gravity226/Understanding_Data_Science/tree/master/Linear_Regression#linear-intercept)


### Summary
Linear regression is a modeling technique that involves finding a line of best fit through a set of data points.  Having an equation for the line allows you to makes predictions of things that haven't happened yet.  

Pros:
 - Easy to set up and run
 - Not computationally intensive
 - Can be useful if your data appears to be following a certain trend
 - Provides an easy to explain feature space

Cons:
 - Doesn't work in many real world scenarios
 - Data tends to be too complex for a linear model

### Linear Equation
I think we all learned the y = mx + b equation back in high school algebra. Once we know what the equation it for a particular dataset we can start making predictions.  

<img src="https://github.com/gravity226/Understanding_Data_Science/blob/master/imgs/ymxb.bmp" height="250"><br />
[img Reference](https://www.tes.com/lessons/Xn3MVjd8CqjH-Q/y-mx-b)

Finding the slope and y-intercept:

<img src="https://github.com/gravity226/Understanding_Data_Science/blob/master/imgs/slope_intercept.jpg" height="150"><br />
[img Reference](http://d32ogoqmya1dw8.cloudfront.net/images/introgeo/teachingwdata/LeastSqEq2.jpg)

### Linear Slope
```python
from __future__ import division
import numpy as np

def get_slope(X, y):
    X = np.array(X)
    y = np.array(y)

    x_bar = X.mean()
    y_bar = y.mean()
    xy_bar = (X * X).mean()
    x2_bar = (X**2).mean()

    slope = ((x_bar * y_bar) - xy_bar) / (x_bar**2 - x2_bar)

    return slope
```

### Linear Intercept
```python
from __future__ import division
import numpy as np

def get_intercept(X, y):
    X = np.array(X)
    y = np.array(y)

    b = y_bar - (get_slope(X, y) * x_bar)

    return b
```

### Predict Y
```python
from __future__ import division
import numpy as np

def predict_y(X, y):
    X = np.array(X)
    y = np.array(y)

    b = y_bar - (get_slope(X, y) * x_bar)

    return b
```







#
