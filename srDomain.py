#!/usr/bin/env python3

import io
import sys
import datetime
import time
from optparse import OptionParser
from prettytable import PrettyTable

def countRemoteHost(filter_content):
    host = {}
    x = PrettyTable()
    x.field_names = ["Remote Host", "Request", "%"]
        
    for data in filter_content:
        if (filter_content[data]["remote_host"] in host):
            host[filter_content[data]["remote_host"]] = host.get(filter_content[data]["remote_host"]) + 1
        else:
            host[filter_content[data]["remote_host"]] = 1
    
    for a in host:
        x.add_row([a, host.get(a), "{0:.2f}%".format(host.get(a) * 100 / len(filter_content))])

    x.sortby = "Request"
    x.align["Remote Host"] = 'l'
    x.reversesort = True
    print ("\nHosts")
    print (x)


def countFileType(filter_content):
    filetype = {}
    x = PrettyTable()
    x.field_names = ["File Type", "Request", "%"]
        
    for data in filter_content:
        if (filter_content[data]["file_type"] in filetype):
            filetype[filter_content[data]["file_type"]] = filetype.get(filter_content[data]["file_type"]) + 1
        else:
            filetype[filter_content[data]["file_type"]] = 1
    
    for a in filetype:
        x.add_row([a, filetype.get(a), "{0:.2f}%".format(filetype.get(a) * 100 / len(filter_content))])

    x.sortby = "Request"
    x.align["File Type"] = 'l'
    x.reversesort = True
    print ("\nFile type")
    print (x)


def main():
    usage = "usage: %prog [options] arg"
    version = 'SquidReport::Domain' + ' version' + ' 0.1'
    parser = OptionParser(usage, version=version)
    parser.add_option("-f", "--file", dest="filename",
                  help="write report to FILE", metavar="FILE")
    parser.add_option("-s", "--search", dest="domainsearch")
    parser.add_option("-q", "--quiet",
                  action="store_false", dest="verbose", default=True,
                  help="don't print status messages to stdout")

    (options, args) = parser.parse_args()
    if options is None:
        parser.print_help()
        sys.exit()

    if options.filename is None:
        path_log_squid = "/var/log/squid3/access.log"
    else:
        path_log_squid = options.filename
    
    if options.domainsearch is None:
        domain = ""
    else:
        domain = options.domainsearch

    file_log = open(path_log_squid, "r", encoding="utf-8")
    content_log = file_log.readlines()
    file_log.close()
    
    filter_content = {}
    index = 0
    
    for data in content_log:
        column = data.split()
        
        if (column[6].find(domain) != -1):
            filter_row = {}
            
            # column 0 -> date
            # print (time.strftime("%d/%m/%Y %H:%M", time.localtime(float(column[0]))))
            filter_row['date_query'] = time.strftime("%d/%m/%Y %H:%M", time.localtime(float(column[0])))
        
            # column 2 -> Remote Host
            # print (column[2])
            filter_row['remote_host'] = column[2]
        
            # column 3 -> code/status
            # print (column[3])
            filter_row['status'] = column[3]
        
            # column 4 -> bytes
            # print (column[4])
            filter_row['bytes'] = column[4]
        
            # column 5 -> method
            # print (column[5])
            filter_row['method'] = column[5]
        
            # column 6 -> URL
            # print (column[6])
            filter_row['url'] = column[6]
        
            # column 9 -> type
            # print (column[9])
            filter_row['file_type'] = column[9]
            
            filter_content[index] = filter_row
            index += 1
            
    print ("# Summary ")
    print ("SquidReport")
    print ("Lines Content Log " + str(len(content_log)))
    print ("Domain Search " + domain)
    print ("Match line " + str(len(filter_content)))
    countRemoteHost(filter_content)
    countFileType(filter_content)
    
    print ("\n\nSquidReport v0.1")
    print ("Copyright (C) 2019")
    print ("Author: Daniel Maldonado.")
    print ("SquidReport comes with ABSOLUTELY NO WARRANTY. It is free software, and you are")
    print ("welcome to redistribute it under certain conditions. See source for details.")
    print ("http://danielmaldonado.com.ar/")


if __name__ == "__main__":
    main()