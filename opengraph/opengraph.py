# encoding: utf-8

import re
import urllib2
import json
from BeautifulSoup import BeautifulSoup

class OpenGraph(dict):
    """
    """
    def __init__(self, url=None, html=None, **kwargs):
        for k in kwargs.keys():
            self[k] = kwargs[k]
        
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
        doc = BeautifulSoup(html)
        ogs = doc.html.head.findAll(property=re.compile(r'^og'))
        for og in ogs:
            self[og[u'property'][3:]]=og[u'content']
        
    def is_valid(self):
        if hasattr(self,'title')  and  \
            hasattr(self,'type')  and  \
            hasattr(self,'image') and  \
            hasattr(self,'url'):
            
            return True
        
    def to_html(self):
        if not self.is_valid():
            return u"<meta property=\"og:error\" content=\"og metadata is not valid\" />"
            
        meta = u""
        for key,value in self.iteritems():
            meta += u"\n<meta property=\"og:%s\" content=\"%s\" />" %(key, value)
        meta += u"\n"
        
        return meta
        
    def to_json(self):
        # TODO: force unicode
        if not self.is_valid():
            return json.dumps({'error':'og metadata is not valid'})
            
        return json.dumps(self)
        
    def to_xml(self):
        pass
