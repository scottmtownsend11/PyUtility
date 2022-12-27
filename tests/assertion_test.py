import sys
sys.dont_write_bytecode = True
sys.path.append('..')

# Local
from assertion import assert_between

assert_between(0, 0, 1)
assert_between(0.5, 0, 1)
assert_between(1, 0, 1)

print("\nSuccess!")
