OpenGraph is a module of python for parsing the Open Graph Protocol, you can read more about the specification at http://ogp.me/

Installation
=============

.. code-block:: console

   $ pip install opengraph

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

.. code-block:: pycon

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

.. code-block:: pycon

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
   >>> movie.is_valid()
   True

**Generate JSON or HTML**

.. code-block:: pycon

   >>> ogp = opengraph.OpenGraph("http://ogp.me/")
   >>> print ogp.to_json()
   {"image:type": "image/png", "title": "Open Graph protocol", "url": "http://ogp.me/", "image": "http://ogp.me/logo.png", "scrape": false, "_url": "http://ogp.me/", "image:height": "300", "type": "website", "image:width": "300", "description": "The Open Graph protocol enables any web page to become a rich object in a social graph."}
   >>> print ogp.to_html()

   <meta property="og:image:type" content="image/png" />
   <meta property="og:title" content="Open Graph protocol" />
   <meta property="og:url" content="http://ogp.me/" />
   <meta property="og:image" content="http://ogp.me/logo.png" />
   <meta property="og:scrape" content="False" />
   <meta property="og:_url" content="http://ogp.me/" />
   <meta property="og:image:height" content="300" />
   <meta property="og:type" content="website" />
   <meta property="og:image:width" content="300" />
   <meta property="og:description" content="The Open Graph protocol enables any web page to become a rich object in a social graph." />
