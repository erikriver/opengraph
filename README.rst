OpenGraph is a module of python for parsing the Open Graph Protocol, you can read more about the specification at http://ogp.me/

Installation
=============

pip install opengraph

Features
=============

* Use it as a python dict
* Input and parsing from a specific url
* Input and parsung from html previous extracted
* HTML output
* JSON output

Usage
==============

**From an URL**

>>> import opengraph
>>> video = opengraph.OpenGraph(url="http://www.youtube.com/watch?v=q3ixBmDzylQ")
>>> video.is_valid()
True
>>> for x,y in video.items():
...     print "%-15s => %s" % (x, y)
... 
site_name       => YouTube
description     => Eric Clapton and Paul McCartney perform George Harrison's "While My Guitar Gently Weeps" at the...
title           => While My Guitar Gently Weeps
url             => http://www.youtube.com/watch?v=q3ixBmDzylQ
image           => http://i2.ytimg.com/vi/q3ixBmDzylQ/default.jpg
video:type      => application/x-shockwave-flash
video:height    => 224
video           => http://www.youtube.com/v/q3ixBmDzylQ?version=3&autohide=1
video:width     => 398
type            => video

**From HTML**

>>> HTML = """
... <html xmlns:og="http://ogp.me/ns#">
... <head>
... <title>The Rock (1996)</title>
... <meta property="og:title" content="The Rock" />
... <meta property="og:type" content="movie" />
... <meta property="og:url" content="http://www.imdb.com/title/tt0117500/" />
... <meta property="og:image" content="http://ia.media-imdb.com/images/rock.jpg" />
... </head>
... </html>
... """
>>> movie = opengraph.OpenGraph() # or you can instantiate as follows: opengraph.OpenGraph(html=HTML)
>>> movie.parser(HTML)
>>> video.is_valid()
True

**Generate JSON or HTML**

>>> 
>>>
>>>