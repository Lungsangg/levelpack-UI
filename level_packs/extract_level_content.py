import docx


def extract_content(in_file, out_file):
    doc = docx.Document(in_file)
    content = []
    for par in doc.paragraphs:
        for run in par.runs:
            if run.bold:
                content.append(run.text)
    out_file.write_text('\n'.join(content))
