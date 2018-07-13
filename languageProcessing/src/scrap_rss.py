import urllib2
from urllib2 import urlopen
import re
import cookielib
from cookielib import CookieJar
import time

cj = CookieJar()
opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cj))
opener.addheaders = [('User-agent', 'Mozilla/5.0')]

def main():
    try:
        page = 'http://www.huffingtonpost.com/feeds/index.xml'
        sourceCode = opener.open(page).read()
        #print sourceCode

        try:
            titles = re.findall(r'<title>(.*?)</title>', sourceCode)
            links = re.findall(r'<link>(.*?)</link>', sourceCode)

            for link in links:
                if '.rdf' in link:
                    pass
                else:
                    print "lets visit - {0}".format(link)
                    linkSource = opener.open(link).read()
                    content = re.findall(r'<p>(.*?)</p>', linkSource)

                    for c in content:
                        print c

                    time.sleep(5)

        except Exception, e:
            print str(e)

    except Exception, e:
        print str(e)


main()