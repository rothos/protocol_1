import io
from markdown import markdown
from datetime import datetime

html = """
<html>
<head>
    <meta charset="utf-8"/>
    <meta name="viewport" content="width=device-width,initial-scale=1"/>
    <link rel="stylesheet" href="bootstrap.css">
    <link rel="stylesheet" href="jquery.ui.all.css">
    <link rel="stylesheet" href="jquery.tocify.css">
    <link rel='stylesheet' href='style.css'>
    <link href="https://fonts.googleapis.com/css?family=Lato:400,700&display=swap" rel="stylesheet">
</head>
<body>
    <div id='darkmode' class='lightmode'>toggle dark mode</div>
    <div id='hamburger'><div id='toc_open'>&#9776;</div></div>
    <div id="toc" class="lightmode"><div id='toc_close' class="lightmode"><span>&times;</span></div></div>
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
    <script type='text/javascript'>
        $(document).ready(function() {
            $('#darkmode').click(function(){
                $('body').toggleClass('darkmode')
                $('.alert').toggleClass('darkmode')
                $('#toc').toggleClass('darkmode')
                $('#toc_close').toggleClass('darkmode')
                $('#hamburger').toggleClass('darkmode')
                $('#darkmode').toggleClass('darkmode')
            })

            $('#toc_open').click(function(){
                $('#toc').toggleClass('show')
            })
            $('#toc_close').click(function(){
                $('#toc').toggleClass('show')
            })
        })
    </script>
    <script async src="https://www.googletagmanager.com/gtag/js?id=UA-96730045-1"></script>
    <script> window.dataLayer = window.dataLayer || []; function gtag(){dataLayer.push(arguments);} gtag('js', new Date()); gtag('config', 'UA-96730045-1');</script>
</body>
</html>
"""

infile = io.open('index.md', mode='r', encoding='utf-8')
text = infile.read()
rendered_text = markdown(text).encode('utf-8')
infile.close()

rendered_text = rendered_text.replace('%%DATE%%',
    datetime.utcnow().strftime('%Y-%m-%d-%H:%M:%S')+" UTC")

outfile = open('index.html', 'w')
outfile.write(html % rendered_text)
outfile.close()
