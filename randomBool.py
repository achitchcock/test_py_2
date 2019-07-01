from random import getrandbits
import time
num_trials = 1000000
results = {}
for size in range(1,21):
    start = time.time()
    print("Running trial #{}".format(size))
    count = 0
    for trials in range(num_trials):
        data = []
        for i in range(size):
            data.append(getrandbits(1))
        if all(data):
            count += 1
    results[size] = count
    end = time.time()
    print("\tTrial #{} ran in {:0.2f} seconds".format(size, end-start))
for size, count in results.iteritems():
    print "Total generated: {} for size {}. {:0.2f}%".format(count, size, 100*(float(count)/num_trials))