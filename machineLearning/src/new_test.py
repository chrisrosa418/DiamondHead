#!/usr/bin/env/ python

from pprint import pprint
import requests
import functools

def handle_errors(func):
    @functools.wraps(func)
    def wrapped(*args, **kwargs):
        pprint('wrapped')
        print func
        #try:
        #    func(*args, **kwargs)
        #except:
        #    pprint('didn\'t work')

    return wrapped

@handle_errors
def index():
    response = requests.get('http://api.macvendors.com/AA:AA:AA:AA:AA:AA')
    pprint(response.content)


index()
