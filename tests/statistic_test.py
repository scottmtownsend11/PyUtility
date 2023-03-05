# Imports

import sys
sys.dont_write_bytecode = True
sys.path.append('..')

from System.assertion import assert_between

from Math.statistic import mean
from Math.statistic import variance
from Math.statistic import standard_deviation


# Core

m = mean([ 1, 2, 3, 4, 5 ])
assert m == 3

m = mean([ 1.1, 2, 3.5, 4.7, -10 ])
assert_between(m, 0.259999, 0.260001)

v = variance([ 1, 2, 3, 4, 5 ])
assert v == 2

v = variance([ 1.1, 2, 3.5, 4.7, -10 ])
assert_between(v, 27.842399, 27.842401)

sd = standard_deviation([ 1, 2, 3, 4, 5 ])
assert_between(sd, 1.4142135, 1.4142137)

sd = standard_deviation([ 1.1, 2, 3.5, 4.7, -10 ])
assert_between(sd, 5.2765897, 5.2765899)

print("\nSuccess!")
