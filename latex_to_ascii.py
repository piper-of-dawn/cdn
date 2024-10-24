import re

def latex_to_ascii(text):
    # Mapping of LaTeX symbols to ASCII equivalents
    '\\alpha': 'α',
        '\\beta': 'β',
        '\\gamma': 'γ',
        '\\delta': 'δ',
        '\\epsilon': 'ε',
        '\\zeta': 'ζ',
        '\\eta': 'η',
        '\\theta': 'θ',
        '\\iota': 'ι',
        '\\kappa': 'κ',
        '\\lambda': 'λ',
        '\\mu': 'μ',
        '\\nu': 'ν',
        '\\xi': 'ξ',
        '\\omicron': 'ο',
        '\\pi': 'π',
        '\\rho': 'ρ',
        '\\sigma': 'σ',
        '\\tau': 'τ',
        '\\upsilon': 'υ',
        '\\phi': 'φ',
        '\\chi': 'χ',
        '\\psi': 'ψ',
        '\\omega': 'ω',
        '\\Gamma': 'Γ',
        '\\Delta': 'Δ',
        '\\Theta': 'Θ',
        '\\Lambda': 'Λ',
        '\\Xi': 'Ξ',
        '\\Pi': 'Π',
        '\\Sigma': 'Σ',
        '\\Upsilon': 'Υ',
        '\\Phi': 'Φ',
        '\\Psi': 'Ψ',
        '\\Omega': 'Ω',
    
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
