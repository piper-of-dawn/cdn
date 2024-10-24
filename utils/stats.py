import math

def one_sided_t_test(sample1, sample2, alpha=0.05, alternative='greater'):
    """
    One-sided t-test for two means.

    Parameters:
    - sample1: list or array, first sample
    - sample2: list or array, second sample
    - alpha: significance level (default is 0.05)
    - alternative: 'greater' or 'less', the direction of the test (default is 'greater')

    Returns:
    - t_statistic: calculated t-statistic
    - p_value: calculated p-value
    - reject_null: True if null hypothesis is rejected, False otherwise
    """
    n1 = len(sample1)
    n2 = len(sample2)

    mean1 = sum(sample1) / n1
    mean2 = sum(sample2) / n2

    var1 = sum((x - mean1)**2 for x in sample1) / (n1 - 1)
    var2 = sum((x - mean2)**2 for x in sample2) / (n2 - 1)

    pooled_var = ((n1 - 1) * var1 + (n2 - 1) * var2) / (n1 + n2 - 2)

    standard_error = math.sqrt(pooled_var * (1/n1 + 1/n2))

    t_statistic = (mean1 - mean2) / standard_error

    if alternative == 'greater':
        p_value = 1 - scipy.stats.t.cdf(t_statistic, df=n1 + n2 - 2)
    elif alternative == 'less':
        p_value = scipy.stats.t.cdf(t_statistic, df=n1 + n2 - 2)
    else:
        raise ValueError("Invalid alternative. Use 'greater' or 'less'.")

    reject_null = p_value < alpha

    return t_statistic, p_value, reject_null

# Example usage:

# Define two sample datasets
sample1 = [1.2, 2.5, 3.8, 4.2, 5.5]
sample2 = [0.8, 2.0, 3.0, 4.0, 5.0]

# Perform one-sided t-test
t_statistic, p_value, reject_null = one_sided_t_test(sample1, sample2, alpha=0.05, alternative='greater')

# Display results
print("T-Statistic:", t_statistic)
print("P-Value:", p_value)
print("Reject Null Hypothesis:", reject_null)
