# encoding: utf-8

import unittest
import opengraph


HTML = """
<html xmlns:og="http://ogp.me/ns#">
<head>
<title>The Rock (1996)</title>
<meta property="og:title" content="The Rock" />
<meta property="og:type" content="movie" />
<meta property="og:url" content="http://www.imdb.com/title/tt0117500/" />
<meta property="og:image" content="http://ia.media-imdb.com/images/rock.jpg" />
</head>
</html>
"""

HTML_OG_NOT_VALID = """
<html xmlns:og="http://ogp.me/ns#">
<head>
<title>The Rock (1996)</title>
</head>
</html>
"""

SCRAPE_HTML = """
<html>
    <head>
        <title>some cool title</title>
        <meta name="description" content="some cool description">
    </head>
    <body>
    <img src="cool-image.jpg" />
    </body>
</html>
"""

SCRAPE_HTML_WITHOUT_DESCRIPTION = """
<html>
    <head>
        <title>some cool title</title>
    </head>
</html>
"""

class test(unittest.TestCase):

    def test_url(self):
        data = opengraph.OpenGraph(url='https://vimeo.com/896837')
        self.assertEqual(data['url'], 'https://vimeo.com/896837')

    def test_isinstace(self):
        data = opengraph.OpenGraph()
        self.assertTrue(isinstance(data,dict))

    def test_to_html(self):
        og = opengraph.OpenGraph(html=HTML)
        self.assertTrue(og.to_html())

    def test_to_json(self):
        og = opengraph.OpenGraph(url='http://www.youtube.com/watch?v=XAyNT2bTFuI')
        self.assertTrue(og.to_json())
        self.assertTrue(isinstance(og.to_json(),str))

    def test_no_json(self):
        opengraph.import_json = False
        og = opengraph.OpenGraph(url='http://grooveshark.com')
        self.assertEqual(og.to_json(),"{'error':'there isn't json module'}")

    def test_is_valid(self):
        og = opengraph.OpenGraph(url='http://grooveshark.com')
        self.assertTrue(og.is_valid())

    def test_is_not_valid(self):
        og = opengraph.OpenGraph(html=HTML_OG_NOT_VALID)
        self.assertFalse(og.is_valid())

    def test_scraping_title_and_description(self):
        data = opengraph.OpenGraph(html=SCRAPE_HTML, scrape=True)
        self.assertEqual(data['title'], 'some cool title')
        self.assertEqual(data['description'], 'some cool description')
        self.assertEqual(data['image'], 'cool-image.jpg')

    def test_scraping_doesnt_fail_when_description_is_missing(self):
        data = opengraph.OpenGraph(html=SCRAPE_HTML_WITHOUT_DESCRIPTION, scrape=True)

if __name__ == '__main__':
	unittest.main()
