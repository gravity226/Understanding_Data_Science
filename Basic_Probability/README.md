# Basic Probability

Python 2.7

### Sections
 - [Probability of an Event](https://github.com/gravity226/Understanding_Data_Science/tree/master/Basic_Probability#probability-of-an-event)
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

Example 3

What is the probability of rolling two sixes with two dice?
``` python
from __future__ import division
from itertools import product

dice_sides = [ x[0] + x[1] for x in product('123456', repeat=2) ]  # two dice with 6 sides each
two_sixes = '66'

print dice_sides.count(two_sixes) / len(dice_sides)
```
``` output
> 0.0277777777778
```

Example 4

If you're give two dice, a six sided die and a thirty two sided die, what is the probability of rolling something that adds up to greater than 10?
``` python
from __future__ import division
from itertools import product

greater_than = 10
dice = [ 1 if sum(x) > greater_than else 0 for x in list(product(xrange(1,7), xrange(1,33)))]

print sum(dice) / len(dice)
```
``` output
> 0.796875
```

Example 5

What is the probability of rolling two six sided dice where the result adds to seven?
``` python
from __future__ import division
from itertools import product

adds_to = 7
dice = [ 1 if sum(x) == adds_to else 0 for x in list(product(xrange(1,7), repeat=2))]

print sum(dice) / len(dice)
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
