# Basic Probability

Python 2.7

### Sections
 - [Probability of an Event](https://github.com/gravity226/Understanding_Data_Science/tree/master/Basic_Statistics#probability-of-an-event)
 - [Roll the Dice](https://github.com/gravity226/Understanding_Data_Science/tree/master/Basic_Probability#roll-the-dice)
 - [Flip a Coin](https://github.com/gravity226/Understanding_Data_Science/tree/master/Basic_Probability#flip-a-coin)


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

### Flip a Coin
Example 1

What is the probability of getting Heads on one coin flip?
``` python
from __future__ import division

coin_sides = ['h', 't']
get_heads = 'h'

print coin_sides.count(get_heads) / len(coin_sides)
```
``` output
> 0.5
```

Example 2

What is the probability of getting heads, heads, heads from 3 coin flips?
``` python
from __future__ import division
from itertools import product

coin_outcomes = [ x[0] + x[1] + x[2] for x in product('ht', repeat=3) ]  # h and t representing head and tails
get_heads = 'hhh'  # hhh representing heads 3 times

print coin_outcomes.count(get_heads) / len(coin_outcomes)
```
``` output
> 0.125
```

Example 3

What is the probability of getting tails at least twice in four coin flips?
``` python
from __future__ import division
from itertools import product

coin_outcomes = [ x[0] + x[1] + x[2] + x[3] for x in product('ht', repeat=4) ]  # h and t representing head and tails
two_tails = sum([ 1 if sum(map(lambda s: s == 't', c)) >= 2 else 0 for c in coin_outcomes ])

print two_tails / len(coin_outcomes)
```
``` output
> 0.6875
```
