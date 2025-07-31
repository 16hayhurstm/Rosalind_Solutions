import itertools
import math

print(math.factorial(5))

for p in itertools.permutations([1, 2, 3, 4, 5]):
    print(" ".join(map(str, p)))
