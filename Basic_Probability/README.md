# Basic Probability

Python 2.7

### Sections
 - [Probability of an Event](https://github.com/gravity226/Understanding_Data_Science/tree/master/Basic_Statistics#probability-of-an-event)
 - [Roll the Dice](https://github.com/gravity226/Understanding_Data_Science/tree/master/Basic_Probability#roll-the-dice)


### Probability of an Event
"The probability of event A is the number of ways event A can occur divided by the total number of  possible outcomes." [reference](http://www.mathgoodies.com/lessons/vol6/intro_probability.html)

I think it's best to explain probability by giving examples.

### Roll the Dice
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

Example 2

Same problem, but looking at it as a dataset.
``` python
from __future__ import division
dice_sides = [1, 2, 3, 4, 5, 6]
one_num = 3

print dice_sides.count(one_num) / len(dice_sides)
```
``` output
> 0.166666666667
```

### Bag of
