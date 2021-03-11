Ian's notes for PyCon Belarus 2021 talk on

"Faster Problem Solving with Pandas"
"My Pandas is slow!" - I hear that a lot. We'll look at ways of making Pandas calculate faster, help you express your problem to fit Pandas more efficiently and look at process changes that'll make you waste less time debugging your Pandas. By attending this talk you'll get answers faster and more reliably with Pandas.

These notes aren't meant for anyone else to read!

```
$ conda create -n pyconby2021 pandas jupyter altair numba bottleneck numexpr python=3.8^C

Note that protocol 5 in python 3.8 writes/reads maybe faster or same speed - boring
https://docs.python.org/3/library/pickle.html
```

From my PyDataGlobal talk I had other unexplored ideas:
* make "is_cottage" indicator using .str.contains vs .str.re ?
  * can numba compile this for an apply?
  * can we use re2 in place of re?
* paon is mostly numeric, some str, value_counts misses nan and 13 is unpopular in UK
* street name length vaguely predictive of median value
* valuecount vs groupby, same speed but gpby is more expensive on RAM
