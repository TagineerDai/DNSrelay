#!/usr/bin/env python
# coding: utf-8
import sys
from cache import DNSCache


if __name__ == "__main__":
    "python dnsrecs.py dnsrelay.txt all | add domainname ip | del domainname"
    DNSFile = sys.argv[1]
    cache = DNSCache(DNSFile, 2000, 600)
    print "Loaded DNSFile " + DNSFile

    cmd = sys.argv[2]
    if cmd =='add':
        cache.add_rec(sys.argv[3], sys.argv[4])
        print "added" , sys.argv[3] , sys.argv[4]
        cache.save(DNSFile)
        print "saved modified cache file in" + DNSFile

    elif cmd == 'del':
        cache.del_rec(sys.argv[3])
        print "delete" , sys.argv[3]
        cache.save(DNSFile)
        print "saved modified cache file in" + DNSFile

    elif cmd == 'all':
        for pair in cache.rec.iteritems():
            print pair[1] + ' ' + pair[0]