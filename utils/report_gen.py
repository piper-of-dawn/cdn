import sys

def is_table_separator(line):
    # A table separator must include a pipe and a dash.
    return '-' in line and '|' in line

def process_lines(lines):
    output = []
    script_inserted = False
    i = 0
    while i < len(lines):
        line = lines[i]
        # If a line starts with "|" and the next line is a separator, assume a table start.
        if line.strip().startswith('|') and i + 1 < len(lines) and is_table_separator(lines[i+1]):
            if not script_inserted:
                output.extend([
                    '<script>',
                    'function copyTable(btn) {',
                    '  var container = btn.nextElementSibling;',
                    '  var text = container.innerText;',
                    '  navigator.clipboard.writeText(text).then(function() {',
                    '    alert("Table copied to clipboard!");',
                    '  }, function(err) {',
                    '    console.error("Could not copy text: ", err);',
                    '  });',
                    '}',
                    '</script>'
                ])
                script_inserted = True
            # Wrap the table in a div with a button and pre tag.
            output.append('<div class="table-wrapper">')
            output.append('<button onclick="copyTable(this)">Copy this table to paste in Excel</button>')
            output.append('<pre>')
            # Gather all consecutive table lines.
            while i < len(lines) and lines[i].strip().startswith('|'):
                output.append(lines[i].rstrip())
                i += 1
            output.append('</pre>')
            output.append('</div>')
            continue
        else:
            output.append(line.rstrip())
            i += 1
    return output

def main():
    # Read from stdin if piped; otherwise, require input and output file names.
    if sys.stdin.isatty():
        if len(sys.argv) < 3:
            print("Usage: python process_stdout_to_md.py input.txt output.md")
            sys.exit(1)
        with open(sys.argv[1], 'r') as f:
            lines = f.readlines()
        output_file = sys.argv[2]
    else:
        lines = sys.stdin.readlines()
        if len(sys.argv) >= 2:
            output_file = sys.argv[1]
        else:
            print("Usage: cat input.txt | python process_stdout_to_md.py output.md")
            sys.exit(1)
    processed = process_lines(lines)
    with open(output_file, 'w') as f:
        f.write("\n".join(processed))
    print(f"Markdown written to {output_file}")

import markdown
from bs4 import BeautifulSoup

# Convert raw.md to HTML using Python Markdown (ensure 'markdown' package is installed)
with open('raw.md', 'r', encoding='utf-8') as f:
    md_content = f.read()
html_body = markdown.markdown(md_content, extensions=['tables'])

# Use BeautifulSoup to inject the copy button above each table
soup = BeautifulSoup(html_body, 'html.parser')
for table in soup.find_all('table'):
    # Wrap the table in a new div with class "table-wrapper"
    wrapper = soup.new_tag("div", **{"class": "table-wrapper"})
    table.wrap(wrapper)
    # Create the copy button
    button = soup.new_tag("button", onclick="copyTable(this)")
    button.string = "Copy this table to paste in Excel"
    # Insert the button before the table within the wrapper
    table.insert_before(button)

modified_html_body = str(soup)

# Build a full HTML boilerplate and inject the modified HTML body
html_template = f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Converted Markdown</title>
  <style>
    .table-wrapper {{ margin: 1em 0; }}
  </style>
  <script>
    function copyTable(btn) {{
      var table = btn.nextElementSibling;
      var text = table.innerText;
      navigator.clipboard.writeText(text).then(function() {{
        alert("Table copied to clipboard!");
      }}, function(err) {{
        console.error("Could not copy text: ", err);
      }});
    }}
  </script>
</head>
<body>
{modified_html_body}
</body>
</html>
"""

with open('output.html', 'w', encoding='utf-8') as f:
    f.write(html_template)

print("HTML written to output.html")


if __name__ == '__main__':
    main()
