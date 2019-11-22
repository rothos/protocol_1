import io
from markdown import markdown

html = """
<html>
<head>
    <link rel="stylesheet" href="bootstrap.css">
    <link rel="stylesheet" href="jquery.ui.all.css">
    <link rel="stylesheet" href="jquery.tocify.css">

    <link rel='stylesheet' href='style.css'>
    <link href="https://fonts.googleapis.com/css?family=Lato:400,700&display=swap" rel="stylesheet">
</head>
<body>
    <div id="toc"></div>
    <div id='content'>%s</div>

    <script src="jquery-1.8.3.min.js"></script>
    <script src="jquery-ui-1.9.1.custom.min.js"></script>
    <script src="bootstrap.js"></script>
    <script src="jquery.tocify.js"></script>
    <script type='text/javascript'>
        $(function() {
            //Calls the tocify method on your HTML div.
            $("#toc").tocify({
                "selectors": "h2,h3,h4,h5,h6",
                "extendPage": false
            });
        });
    </script>
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