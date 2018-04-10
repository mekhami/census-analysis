import os
from time import perf_counter

start = perf_counter()

# First, locate the census data file
cwd = os.path.dirname(__file__)
data_file = os.path.join(cwd, 'census_2009')

frequencies = [0 for _ in range(9)]

with open(data_file, 'r') as f:
    # toss the headers
    f.readline()

    for line in f:
        # Count the first digit of the population
        frequencies[int(line.split()[-1][0]) - 1] += 1

total = sum(frequencies)

# Print out the table headers
print('\n{:<8s}{:<8s}{:<8s}'.format('Digit', 'Count', '%'))

# Print out the rest of the data
for digit, count in enumerate(frequencies):
    print('{:<8}{:<8}{:0.1f}'.format(digit + 1, count, (count / total) * 100))

end = perf_counter()

print('\nTime Elapsed: {:0.2f} ms'.format((end - start) * 1000))