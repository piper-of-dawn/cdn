import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

def plot_kernel_density(data_list, labels=None, color_palette=["#ffa322", "#bb1414", "#042134"]):
    # Set Seaborn style
    sns.set_theme(style="whitegrid")

    # Create a figure and axis
    fig, ax = plt.subplots()

    # Define a custom color palette if provided
    if color_palette:
        sns.set_palette(sns.color_palette(color_palette))

    # Plot kernel density for each tuple in the list
    for i, (data, label) in enumerate(data_list):
        default_label = f'Dataset {i + 1}' if not labels else None
        sns.kdeplot(data, fill=True, alpha=0.5, ax=ax, label=label or default_label, color=color_palette[i] if color_palette else None)

    # Remove spines
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.spines['bottom'].set_visible(False)
    ax.spines['left'].set_visible(False)

    # Add legend
    if labels:
        ax.legend()

    # Display the plot
    plt.show()

# Example usage:
# Assuming you have a list of tuples (numpy array, label, color), e.g.,
# data_list = [(np.array([...]), 'Label1', '#ffa322'), (np.array([...]), 'Label2', '#bb1414'), ...]
# Call the function with your data list and labels
# plot_kernel_density(data_list)
