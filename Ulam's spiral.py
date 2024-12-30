import matplotlib.pyplot as plt
import numpy as np
import matplotlib as mpl

# number and nMax define the range of primality test

number = 1
nMax = 15000
primes = []

# Primality test
def test(number):
    while number <= nMax:
        if number in range(0, 2):
            pass
        else:
            for a in range(2, int(np.sqrt(number))+1):
                if number % a == 0:
                    break
            else:
                primes.append(number)
        number += 1

test(number) # Find the primes

# Axis
fig = plt.figure()
ax = plt.subplot(projection='polar', facecolor='black')

# Spiral
k = np.arange(0,nMax, 0.001) #¿Por qué los pasos tan chicos, si solo me importan los enteros?
rho = np.sqrt(k)
alpha = 2 * np.pi * q

ax.plot(alpha, rho, color = 'gray', linewidth=0.2) #0.2
plt.yticks([])

# Points
n = np.arange(nMax)
r = np.sqrt(n)
theta = 2 * np.pi * r

ax.plot(theta,r, '.', color = 'gray', markersize=0.4) #rosa e4717a #0.8
ax.set_rticks([])

# Primes
p = np.sqrt(primes)
omega = 2 * np.pi * p

ax.plot(omega,p, 'o', color = 'green', markersize= 0.6) #green #1.5
ax.set_rticks([]) # ¿Qué hace esto?

# Euler polinomyal. If 0 <= s <= 41 then f(s) is a prime number
s = np.arange(number, nMax+1, 1)
f = s**2 - s + 41

fIndex = np.arange(len(f))
primeIndex = np.arange(len(primes))

for f_i in fIndex:
    while f[f_i] <= nMax:
        sqrt_f = np.sqrt(f[f_i])
        gamma = 2 * np.pi * sqrt_f
        for p_i in primeIndex:
            if f[p_i] == primes[p_i]:
                ax.plot(gamma,sqrt_f, 'f_i', color = 'red', markersize = 0.6) #0.4
        break

#plt.savefig(f"e-{nMax}.png", dpi = 800)
#plt.savefig(f"{nMax}.svg")

plt.show()
