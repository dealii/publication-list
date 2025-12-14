delete.field = {keywords}
delete.field = {abstract}
delete.field = {publisher}

% generate citekeys using year, author, and title field
key.format = {%d(year):%-2n(author):%-W(title)}
key.generation = on

% exit on first error (avoids contamination of bib files or loss of data)
parse.exit.on.error = on

print.align = 12
print.align.key = 0
print.align.string = 0
print.indent = 2
print.line.length = 999
print.use.tab = off
print.wide.equal = on

% use braces instead of double quotes as delimiters
resource braces

% semantic checks for year fields
resource check_y

% style improvements: no empty fields, fix page ranges, pure numerical fields
resource improve

% sort order for fields
resource sort_fld

sort = on
