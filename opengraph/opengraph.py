# encoding: utf-8

import re
import urllib2
try:
    from bs4 import BeautifulSoup
except ImportError:
    from BeautifulSoup import BeautifulSoup

global import_json
try:
    import json
    import_json = True
except ImportError:
    import_json = False

from collections import OrderedDict


class OpenGraph(dict):
    """
    """

    providers = OrderedDict([
        ('twitter', {
            'attr': 'name',
            'required_attrs': ['title', 'card', 'image']
        }),
        ('og', {
            'attr': 'property',
            'required_attrs': ['title', 'type', 'image', 'url']
        })
        # keep on bottom to respect og precedence
    ])

    def __init__(self, url=None, html=None, scrape=False, **kwargs):
        # If scrape == True, then will try to fetch missing attribtues
        # from the page's body

        # Automatically detect provider unless user specifies with
        # provider='provider' from providers dict

        self.scrape = scrape
        self._url = url

        for k in kwargs.keys():
            self[k] = kwargs[k]

        if not self.get('provider'):
            self.provider = ''

        dict.__init__(self)

        if url is not None:
            self.fetch(url)

        if html is not None:
            self.parser(html)

    def __setattr__(self, name, val):
        self[name] = val

    def __getattr__(self, name):
        return self[name]

    def fetch(self, url):
        """
        """
        raw = urllib2.urlopen(url)
        html = raw.read()
        return self.parser(html)

    def parser(self, html):
        """
        """
        if not isinstance(html, BeautifulSoup):
            doc = BeautifulSoup(html)
        else:
            doc = html
        for provider, details in self.providers.iteritems():
            attribute = details.get('attr')
            search = {attribute: re.compile(r'^%s' % (provider))}
            ogs = doc.html.head.findAll(attrs=search)
            for og in ogs:
                if og.has_attr(u'content'):
                    self[og[attribute][len(provider)+1:]] = og[u'content']
                    if not self.provider or provider is 'og':  # respect og
                        self.provider = provider
            # Couldn't fetch all attrs from og tags, try scraping body
            if self.scrape and not self.is_valid():
                for attr in self.providers.get(
                    self.provider, {}
                ).get('required_attrs'):
                    if not hasattr(self, attr):
                        try:
                            self[attr] = getattr(self, 'scrape_%s' % attr)(doc)
                        except AttributeError:
                            pass

    def is_valid(self):
        return all([
            hasattr(self, attr) for attr in self.providers.get(
                self.provider, {}
            ).get('required_attrs')
        ])

    def to_html(self):
        if not self.is_valid():
            return u"<meta property=\"%s:error\" content=\"%s metadata is not valid\" />" % (self.provider, self.provider)

        meta = u""
        for key, value in self.iteritems():
            meta += u"\n<meta property=\"%s:%s\" content=\"%s\" />" % (self.provider, key, value)
        meta += u"\n"

        return meta

    def to_json(self):
        # TODO: force unicode
        global import_json
        if not import_json:
            return "{'error':'there isn't json module'}"

        if not self.is_valid():
            return json.dumps({'error': 'og metadata is not valid'})

        return json.dumps(self)

    def to_xml(self):
        pass

    def scrape_image(self, doc):
        images = [
            dict(img.attrs)['src']
            for img in doc.html.body.findAll('img')
        ]

        if images:
            return images[0]

        return u''

    def scrape_title(self, doc):
        return doc.html.head.title.text

    def scrape_type(self, doc):
        return 'other'

    def scrape_url(self, doc):
        return self._url
