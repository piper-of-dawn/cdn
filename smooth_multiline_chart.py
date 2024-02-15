import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns

def plot_smooth_multiline_chart(data):
    # Define the color scheme with shades of red and black
    colors = ['#2D132C','#F95959','#801336','#233142','#455D7A','#C72C41','#EE4540','#E3E3E3']
    # Check if the number of data sets is within the supported range
    if len(data) > len(colors):
        raise ValueError("Too many data sets. Maximum supported is {}".format(len(colors)))

    # Create a plot with a different color for each data set
    plt.figure(figsize=(10, 6))
    for i, (x_axis, y_axis, label) in enumerate(data):
        # Use higher resolution for smoother interpolation
        x_smooth = np.linspace(min(x_axis), max(x_axis), 1000)
        y_smooth = np.interp(x_smooth, x_axis, y_axis)
        plt.plot(x_smooth, y_smooth, label=label, color=colors[i])

    # Add labels and legend
    plt.xlabel('X-axis')
    plt.ylabel('Y-axis')
    plt.title('Smooth Multiline Chart with Red and Black Colors')

   # Add mildly visible dotted grid lines in x direction
    plt.grid(axis='y', linestyle='--', alpha=0.5)

    # Remove spines from x and y axis
    sns.despine(left=True, bottom=True)

    # Add legend
    plt.legend()

    # Show the plot
    plt.show()

# Example usage:
x_values = np.linspace(0, 10, 100)
y_values1 = np.sin(x_values)
y_values2 = np.cos(x_values)
y_values3 = np.tan(x_values)

data = [
    (x_values, y_values1, 'Line 1'),
    (x_values[:50], y_values2[:50], 'Line 2 Subset'),
    (x_values[::2], y_values3[::2], 'Line 3 Every 2nd Point')
]

plot_smooth_multiline_chart(data)
