import matplotlib.pyplot as plt
import seaborn as sns
from matplotlib.ticker import AutoMinorLocator
from matplotlib.patches import Rectangle
import numpy as np
from matplotlib.dates import date2num
import pandas as pd
COLORS= [
        "#5E81AC",
        "#BF616A",
        "#B48EAD",
        "#EBCB8B",
        "#B48EAD",
        "#C72C41",
        "#EE4540",
        "#E3E3E3",
    ]

def multiline_chart(data, colors=COLORS, title=None, footnote=None, patch_array=None):
    """
    Create a multiline chart with specified colors and line styles.
    
    Parameters:
    - data: List of 3-tuples [(x, y, "Name of Y series")].
    - colors: List of colors for each line.
    - title: Optional; title of the chart.
    - footnote: Optional; footnote for the chart.
    
    Returns:
    - matplotlib.figure.Figure: The generated chart.
    """
    
    # Define line styles
    line_styles = ['-', '--', '-.', ':']
    
    # Create a new figure
    fig, ax = plt.subplots()
    
    # Plot each series
    for i, (x, y, label) in enumerate(data):
        color = colors[i % len(colors)]
        line_style = line_styles[i % len(line_styles)]
        ax.plot(x, y, label=label, color=color, linestyle=line_style)
    
    # Despine the chart
    sns.despine(left=True, bottom=True)

    # Add legend
    plt.legend()
    
    # Add title if provided
    if title:
        plt.title(title)
    plt.grid(axis="y", linestyle="--", alpha=0.4)
    plt.gca().xaxis.set_minor_locator(AutoMinorLocator())
    plt.gca().yaxis.set_minor_locator(AutoMinorLocator())

    # Add footnote if provided
    if footnote:
        plt.figtext(0.5, -0.05, footnote, wrap=True, horizontalalignment='center', fontsize=10)
    
    if patch_array is not None and i < len(patch_array):
            bool_array = patch_array[i]
            if len(bool_array) == len(y):
                if isinstance(x[0], np.datetime64) or isinstance(x[0], pd.Timestamp):
                    x = date2num(x)        
                print(type(x[0]))
                for j in range(len(bool_array)):
                    if bool_array[j]:
                        ax.add_patch(Rectangle((x[j], ax.get_ylim()[0]), 1, ax.get_ylim()[1] - ax.get_ylim()[0], 
                                               color=color, alpha=0.05))
    # Add legend
    ax.legend()
    
    # Return the figure
    return fig


def arrange_figures(figures):
    """
    Arrange a list of matplotlib.figure.Figure objects into a single image
    with two figures per row.
    
    Parameters:
    - figures: List of matplotlib.figure.Figure objects.
    
    Returns:
    - matplotlib.figure.Figure: The combined image with arranged figures.
    """
    
    # Calculate number of rows and columns based on the number of figures
    num_figures = len(figures)
    num_rows = (num_figures + 1) // 2  # ceil(num_figures / 2)
    num_cols = min(2, num_figures)    # maximum 2 columns
    
    # Create a new figure with appropriate size
    fig, axs = plt.subplots(num_rows, num_cols, figsize=(12, num_rows * 6))
    
    # Flatten axs if necessary (when there's only one row or column)
    axs = axs.flatten()
    
    # Iterate through figures and plot them
    for i, fig_obj in enumerate(figures):
        axs[i].add_figure(fig_obj)  # Assuming the figures are images, otherwise use axs[i].add_figure(fig_obj)
        axs[i].axis('off')  # Turn off axis for cleaner appearance
    
    # Adjust layout and spacing
    fig.tight_layout()
    
    return fig

def plot_acf_pacf_side_by_side(data, lags=None, padding=0.1, title='Autocorrelation and Partial Autocorrelation Functions'):
    from statsmodels.graphics.tsaplots import plot_acf, plot_pacf
    from statsmodels.stats.stattools import durbin_watson
    fig, ax = plt.subplots(1, 2, figsize=(12, 4))

    # ACF plot
    plot_acf(data, lags=lags, ax=ax[0], color='gray')
    ax[0].set_title('Autocorrelation Function (ACF)')

    # PACF plot
    plot_pacf(data, lags=lags, ax=ax[1], color='gray')
    ax[1].set_title('Partial Autocorrelation Function (PACF)')
    if lags is not None:
        ax[0].set_xlim(0, lags)
        ax[1].set_xlim(0, lags)
    else:
        ax[0].set_xlim(0, len(data) // 2)
        ax[1].set_xlim(0, len(data) // 2)
    # Remove spines from both x and y axes
    sns.despine(ax=ax[0], left=True, right=True, top=True, bottom=True)
    sns.despine(ax=ax[1], left=True, right=True, top=True, bottom=True)

    # Adjust layout with padding
    plt.subplots_adjust(wspace=padding)
    # Perform Durbin-Watson test
    dw_stat = durbin_watson(data)
    dw_conclusion = f"Durbin-Watson Test: statistic = {dw_stat:.4f}."

    # Perform ADF test
    adf_result = adf_test(data, 0.05)
    # Add footnote
    fig.text(0.5, -0.05, f"{adf_result}\n{dw_conclusion}", ha='center', fontsize=10, color='gray')

    plt.suptitle(title, y=1.02, fontsize=14, color='black',fontweight= 'bold')
    # Show the plots
    return fig

def adf_test(series, alpha=0.05):
    from statsmodels.tsa.stattools import adfuller
    """
    Perform Augmented Dickey-Fuller (ADF) test for stationarity.

    Parameters:
    - series (pd.Series): Time series data.
    - alpha (float): Significance level for the test.

    Returns:
    - ADF test results and conclusion.
    """
    mask = np.logical_not(np.isnan(series))
# Use this mask to select non-NaN values
    series = series[mask]
    result = adfuller(series, autolag='AIC')
    p_value = result[1]

    if p_value <= alpha:
        return f"Result: Reject the null hypothesis at {alpha} significance level (p-value: {round(p_value,2)}). The time series is likely stationary."
    else:
        return f"Result: Fail to reject the null hypothesis at {alpha} significance level (p-value: {round(p_value,2)}). The time series is likely non-stationary."

def multivariate_density(x, y, x_label="Variable 1", y_label="Variable 2", title="Title"):
    plt.rcParams['font.family'] = 'monospace'
    # Create the jointplot
    g = sns.jointplot(x=x, y=y, kind='kde', fill=True, height=7, cmap="Reds", 
                      color="red", marginal_kws=dict(fill=True))
    
    # Access the underlying Axes objects
    ax_joint = g.ax_joint
    ax_marg_x = g.ax_marg_x
    ax_marg_y = g.ax_marg_y
    
    # Set minor locators
    ax_joint.xaxis.set_minor_locator(AutoMinorLocator())
    ax_joint.yaxis.set_minor_locator(AutoMinorLocator())
    
    # Remove spines
    sns.despine(ax=ax_joint, left=True, bottom=True)
    sns.despine(ax=ax_marg_x, left=True, bottom=True)
    sns.despine(ax=ax_marg_y, left=True, bottom=True)
    
    # Set labels
    ax_joint.set_xlabel(x_label)
    ax_joint.set_ylabel(y_label)
    
    # Adjust the layout to create space for the title at the bottom
    plt.subplots_adjust(bottom=0.2)
    
    # Add title at the bottom
    plt.figtext(0.5, 0.04, title, ha='center', fontsize=16, fontweight="bold", color="#4C566A")
    plt.figtext(0.5, 0.0005, f"Correlation: {np.corrcoef(x, y)[0, 1]:.2f}", fontweight="bold", ha='center', fontsize=9, color="#4C566A")

    # Show the plot
    plt.show()
    return g


import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import statsmodels.api as sm
from statsmodels.stats.outliers_influence import OLSInfluence
from statsmodels.stats.diagnostic import het_breuschpagan
from matplotlib.ticker import AutoMinorLocator

def multivariate_density(model, x_label="Variable 1", y_label="Variable 2", title="Title"):
    fitted_values = model.fittedvalues
    residuals = model.resid
    # Create the jointplot
    g = sns.jointplot(x=fitted_values, y=residuals, kind='kde', fill=True, height=7, cmap="Reds", 
                      color="red", marginal_kws=dict(fill=True))
    
    # Access the underlying Axes objects
    ax_joint = g.ax_joint
    ax_marg_x = g.ax_marg_x
    ax_marg_y = g.ax_marg_y
    
    # Set minor locators
    ax_joint.xaxis.set_minor_locator(AutoMinorLocator())
    ax_joint.yaxis.set_minor_locator(AutoMinorLocator())
    
    # Remove spines
    sns.despine(ax=ax_joint, left=True, bottom=True)
    sns.despine(ax=ax_marg_x, left=True, bottom=True)
    sns.despine(ax=ax_marg_y, left=True, bottom=True)
    
    # Set labels
    ax_joint.set_xlabel(x_label)
    ax_joint.set_ylabel(y_label)
    
    # Adjust the layout to create space for the title at the bottom
    plt.subplots_adjust(bottom=0.2)
    
    # Add title at the bottom
    plt.figtext(0.5, 0.04, title, ha='center', fontsize=16, fontweight="bold", color="#4C566A")
    plt.figtext(0.5, 0.0005, f"Correlation: {np.corrcoef(x, y)[0, 1]:.2f}", fontweight="bold", ha='center', fontsize=9, color="#4C566A")
    # Fit a linear regression model

    
    
    # Create residual vs fitted plot
    plt.figure(figsize=(10, 6))
    plt.scatter(fitted_values, residuals, alpha=0.7, edgecolors='k')
    plt.axhline(0, color='red', linestyle='--', linewidth=1)
    plt.xlabel("Fitted Values")
    plt.ylabel("Residuals")
    plt.title("Residuals vs Fitted Values")
    plt.show()

    # Test for outliers using Cook's Distance
    influence = OLSInfluence(model)
    cooks_d = influence.cooks_distance[0]
    
    # Test for heteroscedasticity using Breusch-Pagan test
    test_stat, p_value, _, _ = het_breuschpagan(residuals, model.model.exog)
    het_test_result = "Heteroscedasticity detected" if p_value < 0.05 else "No heteroscedasticity detected"

    # Show the plot
    plt.show()
    
    # Footnotes
    print(f"Cook's Distance (Outliers): {np.max(cooks_d):.4f}")
    print(f"Breusch-Pagan Test (Heteroscedasticity): p-value = {p_value:.4f} - {het_test_result}")
    
    return g

# Print outliers
    if len(outliers) > 0:
        print(f"Outlier Indices: {outliers}")
        print("Outlier Values (X, Y):")
        for idx in outliers:
            print(f"({x[idx]}, {y[idx]})")
    else:
        print("No outliers detected.")


def plot_residual_histogram_and_normality_check(residuals, outliers):
    # Plot residual histogram with outliers
    plt.figure(figsize=(10, 6))
    sns.histplot(residuals, kde=True, color='blue', bins=30)
    plt.title("Residual Histogram (With Outliers)")
    plt.xlabel("Residuals")
    plt.ylabel("Frequency")
    plt.show()
    
    # Normality check with outliers
    shapiro_test_stat_with_outliers, shapiro_p_value_with_outliers = shapiro(residuals)
    normality_with_outliers = "Normal distribution" if shapiro_p_value_with_outliers > 0.05 else "Not a normal distribution"
    print(f"Shapiro-Wilk Test (With Outliers): p-value = {shapiro_p_value_with_outliers:.4f} - {normality_with_outliers}")
    
    # Remove outliers from residuals
    residuals_without_outliers = np.delete(residuals, outliers)
    
    # Plot residual histogram without outliers
    plt.figure(figsize=(10, 6))
    sns.histplot(residuals_without_outliers, kde=True, color='green', bins=30)
    plt.title("Residual Histogram (Without Outliers)")
    plt.xlabel("Residuals")
    plt.ylabel("Frequency")
    plt.show()
    
    # Normality check without outliers
    shapiro_test_stat_without_outliers, shapiro_p_value_without_outliers = shapiro(residuals_without_outliers)
    normality_without_outliers = "Normal distribution" if shapiro_p_value_without_outliers > 0.05 else "Not a normal distribution"
    print(f"Shapiro-Wilk Test (Without Outliers): p-value = {shapiro_p_value_without_outliers:.4f} - {normality_without_outliers}")

# Generate synthetic data
np.random.seed(0)
x = np.random.normal(size=100)
y = 2 * x + np.random.normal(size=100)


