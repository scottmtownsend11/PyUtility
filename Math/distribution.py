import numpy as np
from scipy.stats import poisson

# Probability of exactly given n_occurrences happens if expected value is mu
def poisson_instance_probability(mu, n_occurrences):
    return poisson.pmf(n_occurrences, mu=mu)

# Probability of at least given n_occurrences happens if expected value is mu
    # All other potentially desired probabiltiies can be derived from this
    #    < # of occurrences : 1.0 - poisson_cumulative_probability(mu, n_occurrences)
    #    > # of occurrences : poisson_cumulative_probability(mu, n_occurrences+1)
    #    <= # of occurrences : 1.0 - poisson_cumulative_probability(mu, n_occurrences+1)
def poisson_cumulative_probability(mu, n_occurrences):
    if isinstance(n_occurrences,list): # TODO: Avoid using isinstance()
        return 1.0 - poisson.cdf([x-1 for x in n_occurrences], mu=mu)
    else:
        return 1.0 - poisson.cdf(n_occurrences-1, mu=mu)
