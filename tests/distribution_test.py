import sys
sys.dont_write_bytecode = True
sys.path.append('..')

# System
import numpy as np

# Local
from distribution import poisson_instance_probability
from distribution import poisson_cumulative_probability

# Poisson
## Instance Probability
### Single Element
P = poisson_instance_probability(1.4, 1)
assert round(P,5) == 0.34524

### Array
P = poisson_instance_probability(0.8, [0,1,2])
assert (np.round_(P,decimals=5) == [0.44933,0.35946,0.14379]).all()

## Cumulative Probability
### Single Element
P = poisson_cumulative_probability(1.4, 1)
assert round(P,5) == 0.75340

### Array
P = poisson_cumulative_probability(0.8, [0,1,2])
assert (np.round_(P,decimals=5) == [1.00000,0.55067,0.19121]).all()

print("\nSuccess!")
