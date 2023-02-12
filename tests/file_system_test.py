import sys
sys.dont_write_bytecode = True
sys.path.append('..')

# Local
from System.file_system import files

paths = files('.')
assert './distribution_test.py' in paths
assert './file_system_test.py' in paths
assert './plot_generator_test.py' in paths
assert 'not-a-file' not in paths

print("\nSuccess!")
