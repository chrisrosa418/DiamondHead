import nltk
import re
import time

exmapleArray = ['Run a DNS lookup on the following IPs - 172.4.1.15, 172.4.1.12', 'Whois google.com', 'Whois 182.41.41.33']

def processLanguage():
    try:
        for item in exmapleArray:
            tokenized = nltk.word_tokenize(item)
            tagged = nltk.pos_tag(tokenized)

            #print tagged
            chunkGram = r"""Chunk: {<RB\w?>*<VB\w?>*<NNP>}"""
            chunkParser = nltk.RegexpParser(chunkGram)
            chunked = chunkParser.parse(tagged)
            print chunked
            #chunked.draw()

    except Exception, e:
        print str(e)

processLanguage()