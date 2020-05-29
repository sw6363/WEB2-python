#!C:\Users\LJH\AppData\Local\Programs\Python\Python38-32\python.exe
print("content-type:text/html; charset=UTF-8\n")

import cgi
form = cgi.FieldStorage()
if 'id' in form:
    pageId = form["id"].value
    description = open('data/'+pageId, 'r').read()

else:
    pageId = 'Welcome'
    description = 'Hello, web'
print('''<!DOCTYPE html>
<html lang="ko" dir="ltr">
<head>
  <title>Web1 - Welcome</title>
  <meta charset="utf-8">
    <link rel="stylesheet" href="style.css">
    <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.4.1/jquery.min.js"></script>
    <script src="colors.js"></script>
</head>

<body>
  <h1><a href="index.py">WEB</a></h1>
  <input type="button" value="night" onclick="
    nightDayHandler(this)
">
  <div id="grid">
  <ol>
    <li><a href="index.py?id=HTML">HTML</a></li>
    <li><a href="index.py?id=CSS">CSS</a></li>
    <li><a href="index.py?id=JavaScript">JavaScript</a></li>
    <li><a href="index.py?id=Python">Python</a></li>
  </ol>
  <div id="article">
  <h2>{title}</h2>
  <p>{desc}</p>
</div>
</div>
</body>
</html>
'''.format(title=pageId, desc=description))
