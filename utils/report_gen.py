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

if __name__ == '__main__':
    main()
