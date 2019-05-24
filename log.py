#!/usr/bin/env python3
#
# Title: job-ofert-fetcher
# Description: This part of script is responsible for saving script behaviors into log file
# Author: @k1k9
# License: MIT
#
from time import localtime as ltime

def saveLog(content, tag="INFO"):
	''' Save information (log) into log file '''

	# Config
	logDate 	= '{0}/{1}/{2} {3}:{4}:{5}'.format(ltime().tm_mday, ltime().tm_mon, 
                    ltime().tm_year, ltime().tm_hour, ltime().tm_min, ltime().tm_sec)

	log 		= '[{0}]\t{1}\t\t{2}\n'.format(logDate, tag.upper(), content)
	file 		= open('logs.txt', 'a+')

	file.write(log)


def saveError(path, error):
    ''' Save error into log file like normal log '''
    saveLog('In {0} error: {1}'.format(path, error), 'error')