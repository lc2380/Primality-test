# Primality test and Ulam's Spiral


- The ***primality test*** was the first idea that I have made when I was learning the first things about Python.
  - Then, iterating the values, I used basic algebra to test every integer between $2$ and some limit of my choice $n$.
  - The heart of the code is $p \leq m^2$, which tells us that given a positive integer $p$, if it is composite it may have some divisor between $2$ and some other positive integer $m$ such that it satisfies the inequality. For example if we want to see if $101$ is prime, let's notice that $101\leq 10^2$ but $101>11^2$, so if $101$ have some divisor then it is between $2$ and $10$. We test this for each prime number in this list and it follows that $101$ is prime.

# Why this?
The main idea was make a prime number finder, and evolved to a Ulam's spiral when i looked this on a blog. Read(ing?) about prime numbers motivated me to continue working in python.

# 
