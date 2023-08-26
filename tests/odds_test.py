import sys
sys.dont_write_bytecode = True
sys.path.append('..')

# Local
from System.assertion import assert_between

from Math.odds import Odds
from Math.odds import american_odds
from Math.odds import decimal_odds
from Math.odds import probability
from Math.odds import margin
from Math.odds import expected_value
from Math.odds import true_probability
from Math.odds import kelly_criterion

# American Odds
assert american_odds(0.5, Odds.PROBABILITY) == 100
assert_between(american_odds(0.84, Odds.PROBABILITY), -526, -524) # -525
assert american_odds(2, Odds.DECIMAL) == 100
assert_between(american_odds(1.1905, Odds.DECIMAL), -526, -524) # -525

# Decimal Odds
assert decimal_odds(0.5, Odds.PROBABILITY) == 2
assert_between(decimal_odds(0.84, Odds.PROBABILITY), 1.18, 1.20) # 1.1905
assert decimal_odds(100, Odds.AMERICAN) == 2
assert_between(decimal_odds(-525, Odds.AMERICAN), 1.18, 1.20) # 1.1905

# Probability
assert probability(2, Odds.DECIMAL) == 0.5
assert_between(probability(1.1905, Odds.DECIMAL), 0.83, 0.85) # 0.84
assert probability(100, Odds.AMERICAN) == 0.5
assert_between(probability(-525, Odds.AMERICAN), 0.83, 0.85) # 0.84

# Margin
odds = [1.2, 5.5]
assert_between(margin(odds), 0.0150, 0.0152)
odds = [2.56, 3.2, 3.3]
assert_between(margin(odds), 0.0060, 0.0062)

# Expected Value
assert_between(expected_value(375, 336), 0.0894495, 0.0894496)
assert_between(expected_value(-102, -104), 0.009611, 0.009612)

# True Probability
assert true_probability([1.91, 1.91]) == [0.5, 0.5]
p = true_probability([3.95, 1.86, 4.08])
assert_between(p[0], 0.243, 0.245)
assert_between(p[1], 0.518, 0.52)
assert_between(p[2], 0.235, 0.237)

# Kelly Criterion
assert_between(kelly_criterion(100, -108), 0.03846, 0.03847) # 0.0384615384615
assert_between(kelly_criterion(-125, -150), 0.099, 0.101) # 0.1

print("\nSuccess!")
