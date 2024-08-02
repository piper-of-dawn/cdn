import re

def latex_to_ascii(text):
    # Mapping of LaTeX symbols to ASCII equivalents
    latex_to_ascii_map = {
        '\\alpha': 'alpha',
        '\\beta': 'beta',
        '\\gamma': 'gamma',
        '\\delta': 'delta',
        '\\epsilon': 'epsilon',
        '\\theta': 'theta',
        '\\lambda': 'lambda',
        '\\mu': 'mu',
        '\\pi': 'π',  # As requested
        '\\sigma': 'sigma',
        '\\omega': 'omega',
        '\\sum': 'SUM',
        '\\int': 'INT',
        '\\infty': 'infinity',
        '\\approx': '~',
        '\\times': 'x',
        '\\div': '/',
        '\\pm': '+-',
        '\\cdot': '*',
        '\\frac': '/',
        '\\sqrt': 'sqrt',
    }
    
    # Function to replace LaTeX symbols within $
    def replace_latex(match):
        expression = match.group(1)
        # Replace each LaTeX symbol in the expression
        for latex, ascii in latex_to_ascii_map.items():
            expression = expression.replace(latex, ascii)
        return expression

    # Use regular expression to find all text within $ and replace it
    result = re.sub(r'\$(.*?)\$', replace_latex, text)
    return result
