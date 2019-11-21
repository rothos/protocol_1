import io
from markdown import markdown

html = """
<html>
<head>
    <link rel='stylesheet' href='style.css'>
    <link href="https://fonts.googleapis.com/css?family=Lato:400,700&display=swap" rel="stylesheet">
</head>
<body>
    <div id='content'>%s</div>
</body>
</html>
"""

infile = io.open('index.md', mode='r', encoding='utf-8')
text = infile.read()
rendered_text = markdown(text).encode('utf-8')
infile.close()

outfile = open('index.html', 'w')
outfile.write(html % rendered_text)
outfile.close()
