import sys
import json

def generate_html(config):
    print (f"Generating HTML: {config['output_file']}")
    outfile = open(config['output_file'], 'w')

    # Write the HTML header
    outfile.write("<html>\n<head>\n<title>\n")
    outfile.write(f"<title>{config['title']}</title>\n")
    outfile.write("<link rel=\"stylesheet\" href=\"styles/main.css\">\n")
    outfile.write("</head>\n<body>\n")
    outfile.write(f"<h1>{config['title']}</h1>\n")

    # Write each section
    for section in config['sections']:
        outfile.write(f"<h{section['header_level']}>{section['header']}</h{section['header_level']}>\n")
        if 'content' in section:
            outfile.write(f"<p>{section['content']}</p>\n")
        if 'file' in section:
            try:
                tablefile = open(section['file'], 'r')
            except FileNotFoundError:
                outfile.write("<p>Error: Data Not Found.</p>\n")
            else:
                outfile.write("<table>\n")
                header = True
                for line in tablefile:
                    if header:
                        outfile.write(f"<tr><th>{'</th><th>'.join(line.strip().split(','))}</th></tr>\n")
                        header = False
                    else:
                        outfile.write(f"<tr><td>{'</td><td>'.join(line.strip().split(','))}</td></tr>\n")
                outfile.write("</table>\n")
                tablefile.close()

    # Write the HTML footer
    outfile.write("</body></html>\n")
    outfile.close()