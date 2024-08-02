import pandas as pd
from openpyxl import Workbook
from openpyxl.styles import Font, PatternFill, Border, Side, Alignment

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

def dict_to_dataframe(data_dict, column_names=["Column 1", "Column 2"], remove_latex_artefacts=True):
    def remove_latex(text):
        return re.sub(r'\$\$.*?\$\$', '', text)
    
    # Create the DataFrame from the dictionary
    df = pd.DataFrame(list(data_dict.items()), columns=column_names)
    
    # Remove LaTeX artifacts if the parameter is set to True
    if remove_latex_artefacts:
        df = df.applymap(lambda x: remove_latex(str(x)) if isinstance(x, str) else x)
    
    return df




def df_to_excel(df, file_name, title=None):
    # Create a workbook and select the active worksheet
    wb = Workbook()
    ws = wb.active
    
    # Define styles
    header_font = Font(name='Consolas', bold=True)
    cell_font = Font(name='Consolas')
    white_fill = PatternFill(start_color='FFFFFF', end_color='FFFFFF', fill_type='solid')
    thick_border = Border(top=Side(style='thick'), bottom=Side(style='thick'))
    thin_bottom_border = Border(bottom=Side(style='thin'))
    alignment = Alignment(horizontal='center', vertical='center')
    
    # Adjust row height
    for row in ws.iter_rows():
        for cell in row:
            cell.font = cell_font
            cell.fill = white_fill
            cell.border = thin_bottom_border
            ws.row_dimensions[cell.row].height = 21
    
    # Add title if provided
    start_row = 1
    if title:
        ws.merge_cells(start_row=start_row, start_column=1, end_row=start_row, end_column=len(df.columns))
        title_cell = ws.cell(row=start_row, column=1)
        title_cell.value = title
        title_cell.font = Font(name='Consolas', bold=True, size=14)
        title_cell.alignment = alignment
        start_row += 1

    # Add header
    for col_num, column_title in enumerate(df.columns, 1):
        cell = ws.cell(row=start_row, column=col_num)
        cell.value = column_title
        cell.font = header_font
        cell.fill = white_fill
        cell.border = thick_border
        cell.alignment = alignment
        ws.row_dimensions[start_row].height = 21

    # Add data rows
    for row_num, row_data in enumerate(df.values, start=start_row + 1):
        for col_num, cell_value in enumerate(row_data, 1):
            cell = ws.cell(row=row_num, column=col_num)
            cell.value = cell_value
            cell.font = cell_font
            cell.fill = white_fill
            cell.border = thin_bottom_border
            cell.alignment = alignment
        ws.row_dimensions[row_num].height = 21

    # Save the workbook
    wb.save(file_name)

