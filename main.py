#!/usr/bin/env python3
#
# Title: job-ofert-fetcher
# Description: Download job offers from pracuj.pl, clean response of unnecessary things
#              and save it into output file
# Author: @k1k9
# License: MIT
#
import re
import log
import json	
import requests
from bs4 			import BeautifulSoup 	as bsoup




# Initialize variables
job_offers          = []
subpages_counter    = 0
subpages            = 0

url                 = 'https://www.pracuj.pl/praca?pn=%d'
blacklist           = ["@context", "@type", "validThrough"]




# Get number of subpages
try:
    request 	= requests.get(url%1)
    response	= bsoup(request.text, 'html.parser')

    # Find the highest number of subpages
    for subpage in response.findAll('a', {'class':'pagination_trigger'}):
        try: tmpSubpage = int(subpage.text)
        except: break
        subpages = tmpSubpage if subpages < tmpSubpage else subpages
except Exception as E:
        log.saveError(__file__, E)
        raise E




# Fetch job offers from all subpages
for subpage in range(1, subpages+1):
    print('Downloaded {0} job offers from {1}/{2} subpages'.format(len(job_offers), 
                                                    subpages_counter, subpages), end='\r')
        

    # Parse data from subpage
    try:
        request 		=  requests.get(url%subpage)
        response 		=  bsoup(request.text, 'html.parser')
        subpages_counter  += 1
    except Exception as E:
        log.saveError(__file__, E)
        raise E


    # Grab job offers
    for ofert in response.findAll('script', {'type':'application/ld+json'}):
        ofert = eval(re.sub(' +', ' ', ofert.text.replace('\n','').replace('\r', '')))

        # Clean data of keys from blacklist
        try: 
            for key in blacklist: del ofert[key]
        except: pass
        job_offers.append(ofert)




# Save data into file
with open('output.json', 'w') as file:
    json.dump(job_offers, file, ensure_ascii=False)
    log.saveLog('Saved {0} job offers from {1}'.format(len(job_offers), url))