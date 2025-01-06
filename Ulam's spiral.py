import matplotlib.pyplot as plt
import numpy as np
import matplotlib as mpl

# number and nMax define the range of primality test

number = 1
nMax = 30000
primes = []

# Primality test
def is_prime(number):
    if number < 2:
        return False
    for a in range(2, int(np.sqrt(number)) + 1):
        if number % a == 0:
            return False
    return True

primes = np.array([number for number in range(2, nMax + 1) if is_prime(number)])

# Axis
fig = plt.figure()
ax = plt.subplot(projection='polar', facecolor='black')

# Spiral
k = np.arange(0,nMax, 1)
rho = np.sqrt(k)
alpha = 2 * np.pi * rho

ax.plot(alpha, rho, color = 'gray', linewidth=0.1) #0.2
plt.yticks([])

#Points
n = np.arange(nMax)
r = np.sqrt(n)
theta = 2 * np.pi * r

ax.plot(theta,r, '.', color = 'gray', markersize=0.6, lw=0) #rosa e4717a #0.8
ax.set_rticks([])

# Primes
p = np.sqrt(primes)
omega = 2 * np.pi * p

ax.plot(omega,p, '*', color='green', markersize= 0.6, lw=0) #green #1.5
ax.set_rticks([]) # ¿Qué hace esto?

# Euler polinomyal. If 0 <= s <= 41 then f(s) is a prime number
s = np.arange(number, 40)
f = s**2 - s + 41

fIndex = np.arange(len(f))

sqrt_f = np.sqrt(f)
gamma = 2 * np.pi * sqrt_f
ax.plot(gamma,sqrt_f, '.', color = 'red', markersize = 0.6, lw=0) #0.4 0.6

#plt.savefig(f"{len(primes)}.png", dpi = 1000)
plt.savefig(f"{len(primes)}.svg")
#plt.savefig(f"{len(primes)}.pdf", format="pdf")

plt.show()
