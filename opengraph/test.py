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
        og = opengraph.OpenGraph(url='https://www.youtube.com/watch?v=XAyNT2bTFuI')
        self.assertTrue(og.to_json())
        self.assertTrue(isinstance(og.to_json(),str))

    def test_no_json(self):
        if getattr(opengraph, 'import_json', None) is not None:  # python2
            opengraph.import_json = False
        else:  # python3
            opengraph.opengraph.import_json = False
        og = opengraph.OpenGraph(url='http://www.ogp.me/')
        self.assertEqual(og.to_json(),"{'error':'there isn't json module'}")

    def test_is_valid(self):
        og = opengraph.OpenGraph(url='http://www.ogp.me/')
        self.assertTrue(og.is_valid())



if __name__ == '__main__':
	unittest.main()
