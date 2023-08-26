# Useful Reference Material - https://www.bettingexpert.com/academy/advanced-betting-theory/odds-conversion-to-percentage
# Useful Reference Material - https://www.aceodds.com/bet-calculator/odds-converter.html
# Useful Reference Material - https://help.smarkets.com/hc/en-gb/articles/214180145-How-to-calculate-betting-margins
# Useful Reference Material - https://oddsjam.com/betting-calculators/expected-value
# Useful Reference Material - https://en.wikipedia.org/wiki/Kelly_criterion

class Odds: # Enumeration
    PROBABILITY = 0
    AMERICAN = 1
    DECIMAL = 2

# Converts to American Odds
def american_odds(odds, type):
    if type == Odds.DECIMAL:
        # Decimal Odds to American Odds
        if odds >= 2.0:
            return (odds - 1.0) * 100.0
        return -100 / (odds - 1.0)
    elif type == Odds.PROBABILITY:
        # Probability to American Odds
        if odds > 0.5:
            return -1.0 * (odds * 100.0) / (1.0 - odds)
        return (100.0 - 100.0 * odds) / odds
    return 0 # Unknown Type

# Converts to Decimal Odds
def decimal_odds(odds, type):
    if type == Odds.AMERICAN:
        # American Odds to Decimal Odds
        if odds > 0:
            return 1.0 + odds/100.0
        return 1.0 - 100.0/odds
    elif type == Odds.PROBABILITY:
        # Probability to Decimal Odds
        return 1.0 / odds
    return 0 # Unknown Type

# Converts to Probability
def probability(odds, type):
    if type == Odds.DECIMAL:
        # Decimal Odds to Probability
        return 1.0 / odds
    elif type == Odds.AMERICAN:
        # American Odds to Probability
        if odds > 0:
            return 100.0 / (odds + 100.0)
        return -1 * odds / (-1 * odds + 100.0)
    return 0 # Unknown Type

# Calculates margin of a bet given all associated odds
    # Assumes Decimal Odds
def margin(odds):
    total = 0
    for i in range(0, len(odds)):
        total = total + 1.0 / odds[i]
    return total - 1.0

# Calculates Expected Value of a Bet, based on Given Odds and True Odds
    # Assumes American Odds
def expected_value(given_odds, true_odds):
    dec_given = decimal_odds(given_odds, Odds.AMERICAN)
    p_true = probability(true_odds, Odds.AMERICAN)
    return p_true * (dec_given - 1.0) - (1.0 - p_true)

# Calculates the underlying true probability based on given odds (which may contain a bookie margin)
    # Assumes Decimal Odds
def true_probability(odds):
    for i in range(0, len(odds)):
        odds[i] = probability(odds[i], Odds.DECIMAL)
    total = sum(odds)
    return [x / total for x in odds]

# Calculates the Optimal Bet Percentage using the Kelly Criterion formula
    # Assumes American Odds
def kelly_criterion(given_odds, true_odds):
    dec_given = decimal_odds(given_odds, Odds.AMERICAN)
    p_true = probability(true_odds, Odds.AMERICAN)
    return ((dec_given - 1.0)*p_true - (1.0 - p_true)) / (dec_given - 1.0)
