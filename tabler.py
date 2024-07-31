def int_to_roman(num):
    if not 1 <= num <= 3999:
        raise ValueError("Number out of range (must be between 1 and 3999)")
    
    roman_numerals = [
        (1000, 'M'), (900, 'CM'), (500, 'D'), (400, 'CD'),
        (100, 'C'), (90, 'XC'), (50, 'L'), (40, 'XL'),
        (10, 'X'), (9, 'IX'), (5, 'V'), (4, 'IV'), (1, 'I')
    ]
    
    result = []
    for (value, symbol) in roman_numerals:
        while num >= value:
            result.append(symbol)
            num -= value
    return ''.join(result)

def dict_to_latex_table(data_dict, numbering=False):
    latex_code = []
    latex_code.append("\\begin{table}[h!]")
    latex_code.append("\\centering")
    latex_code.append("\\begin{tabular}{%s}" % ('c c c' if numbering else 'c c'))
    latex_code.append("\\toprule")
    
    # Header row
    header = []
    if numbering:
        header.append("\\textbf{No.}")
    header.extend(["\\textbf{Column 1}", "\\textbf{Column 2}"])
    latex_code.append(" & ".join(header) + " \\\\")
    latex_code.append("\\midrule")
    
    # Data rows
    for i, (key, value) in enumerate(data_dict.items(), start=1):
        row = []
        if numbering:
            row.append(int_to_roman(i))
        row.extend([str(key), str(value)])
        latex_code.append(" & ".join(row) + " \\\\")
    
    latex_code.append("\\bottomrule")
    latex_code.append("\\end{tabular}")
    latex_code.append("\\end{table}")
    
    return "\n".join(latex_code)

def dict_to_markdown_table(data_dict, numbering=False):
    markdown_code = []
    
    # Header row
    header = []
    if numbering:
        header.append("**No.**")
    header.extend(["**Column 1**", "**Column 2**"])
    markdown_code.append("| " + " | ".join(header) + " |")
    
    # Divider row
    divider = ["---"] * (3 if numbering else 2)
    markdown_code.append("| " + " | ".join(divider) + " |")
    
    # Data rows
    for i, (key, value) in enumerate(data_dict.items(), start=1):
        row = []
        if numbering:
            row.append(int_to_roman(i))
        row.extend([str(key), str(value)])
        markdown_code.append("| " + " | ".join(row) + " |")
    
    return "\n".join(markdown_code)
