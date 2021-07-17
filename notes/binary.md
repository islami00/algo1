Binary search works by breaking the list down to smaller sets till the value is found

Analysing each step of our code:
1. Value assignment (last, first, midpoint) - constant time from py
2. Division, comparison, read value from list - constant

This series of constant time operations come together to logarithmic because of the while loop.

The data-size reduces each time till it gets to a singleton


The very basis and most important part of the binary search is:
**The list must be sorted**

i.e:
< , > , = and their mixins must be executable on pairs of the members of the list

data structures that satisfy this condition include:
1. Strings
2. Numbers
3. ordered lists containing these

This very implementation of binary search depends on the values being sorted in ascending order.

This implies that if the midpoint is less, the possible values will be to the right (just like the progression of numbers)
And if the midpoint is greater, the possible values are to the left.

And thanks to indexing, we can simply specify this by incrementing to move right or decrementing to move left.

Now, if for some reason your set is ordered in descending order.
Reverse the meaning of the above.