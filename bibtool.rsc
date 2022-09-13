delete.field = {keywords}
delete.field = {abstract}

% generate citekeys using year, author, and title field
key.format = {%d(year):%-2n(author):%-W(title)}
key.generation = on

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

% translate iso 8859/1 characters to latex
resource iso2tex

sort = on
