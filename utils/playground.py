from rapidfuzz.distance import lcs_seq_ratio

def find_most_similar(input_string, candidates):
    """
    Find the most similar string from candidates based on:
    1. Length of longest common subsequence (using rapidfuzz)
    2. Presence of first word of input string
    
    Args:
        input_string (str): The string to compare against
        candidates (iterable): Collection of strings to compare with
    
    Returns:
        str: Most similar string from candidates
    """
    if not candidates:
        return None
    
    # Get the first word of input string
    first_word = input_string.split()[0] if input_string.split() else ""
    
    # Calculate similarity scores for all candidates
    similarities = []
    for candidate in candidates:
        # rapidfuzz's lcs_seq_ratio returns a value between 0 and 100
        score = lcs_seq_ratio(input_string.lower(), candidate.lower())
        # Add bonus if first word is present in candidate (100 points = 100%)
        if first_word.lower() in candidate.lower():
            score += 100  # Add significant bonus
        similarities.append((score, candidate))
    
    # Return the candidate with highest score
    return max(similarities, key=lambda x: x[0])[1]


df['label'] = df['name'].str[:4].str.upper()

# Scatter plot with annotations
plt.figure(figsize=(8, 6))
plt.scatter(df['idiosyncratic_vola'], df['idiosyncratic_vola_vf_adj'], color='blue')

# Reference line
max_val = max(df['idiosyncratic_vola'].max(), df['idiosyncratic_vola_vf_adj'].max())
plt.plot([0, max_val], [0, max_val], 'k--')

# Add text annotations
for i in range(len(df)):
    plt.text(df['idiosyncratic_vola'][i], df['idiosyncratic_vola_vf_adj'][i],
             df['label'][i], fontsize=9, ha='right', va='bottom')

plt.xlabel('Original Idiosyncratic Volatility')
plt.ylabel('Adjusted Idiosyncratic Volatility')
plt.title('Original vs Adjusted Idiosyncratic Volatility')
plt.grid(True, linestyle='--', alpha=0.5)
plt.tight_layout()
plt.show()
