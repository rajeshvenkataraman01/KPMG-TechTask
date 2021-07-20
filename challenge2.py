#!/usr/bin/env python

import requests
import json

def load():
    metaurl = 'http://169.254.169.254/latest'
    dictonary = { 'meta-data': {} }

    for item in dictonary.keys():
        #print('{0}/{1}/'.format(metaurl, item))
        readPath('{0}/{1}/'.format(metaurl, item), dictonary[item])
        
    return dictonary


def readPath(url, d):
    r = requests.get(url)
    if r.status_code == 404:
        return
    for l in r.text.split('\n'):
        if not l: 
            continue
        newurl = '{0}{1}'.format(url, l) 
        if l.endswith('/'):
            path = l.split('/')[-2]
            d[path] = {}
            readPath(newurl, d[path])

        else:
            r = requests.get(newurl)
            if r.status_code != 404:
                    d[l] = json.loads(r.text)
 
            else:
                d[l] = None



if __name__ == '__main__':
    print(json.dumps(load()))
