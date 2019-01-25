import time
from math import sqrt


start = time.time()
primes = [1, 2]
for i in range(3, 1000):
    p = True
    for j in primes[1:]:
        if i % j == 0:
            p = False
    if p:
        primes.append(i)
end = time.time()

grid_size = int(sqrt(len(primes)))
if grid_size > 40:
    grid_size = 40
format_str = "{: >5} "
print ((((format_str*grid_size + "\n")*(len(primes)//grid_size))) +
       (format_str*(len(primes) % grid_size))).format(*primes)

print "Duration:", end-start
