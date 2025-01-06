# Primality test

Libraries:
* Matplotlib
* Numpy

The primality test was the first project I created when I was learning the basics of Python.
- I iterate over values and use basic algebra to test every integer between 2 and a limit of my choice $nMax$.
- The heart of the code is the inequation $p \leq m^2$, which tells us that given a positive integer $p$, if it is composite it may have some divisor between $2$ and some other positive integer $m$ such that it satisfies the inequality. For example if we want to see if $101$ is prime, let's notice that $101\leq 10^2$ but $101>11^2$. Therefore, if 101 has a divisor, it must be between 2 and 10. We test this for each number in the list, and it follows that 101 is prime.

# Why this?
The main idea was to create a prime number finder, which later evolved into Ulam's spiral after I came across this concept on a blog. Reading about prime numbers motivated me to continue working in Python.
