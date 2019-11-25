#!/usr/bin/env python

from bs4 import BeautifulSoup
import urllib2
import re
import sys
import collections
import cgi, cgitb

form = cgi.FieldStorage()
results_url = form.getvalue('results_url')
states = form.getvalue('states')
state_list = states.split(',')
results_url = sys.argv[-1]
page = urllib2.urlopen(results_url)
soup = BeautifulSoup(page, 'html.parser')

groups = soup.findAll('h4', class_='race-result-group')

days = soup.findAll('div', id=re.compile('^rday_'))

#print 'Race, Class, Place, Name, City, State, Sponsor'
for day in days:
    title = day.find('h3', class_='race-result-title')
    
    if title is None:
        exit(0)

    title = title.text

    print '\n\n----------------------------------'
    print 'RACE: {}'.format(title)
    print '----------------------------------'

    groups = day.findAll('h4', class_='race-result-group')
    uls = day.findAll('ul', class_='race-result-list')
    count = 0
    places = collections.OrderedDict()
    p = 1
    while p < 8:
        places[p] = 0
        p += 1

    for ul in uls:
        group = groups[count].text
        class_name = group.split('Total Riders')[0].rstrip()
        # print class_name
        for li in ul.findAll('li'):
            (place, rider) = li.findAll('span')
            rider_info = rider.text.rstrip().split(',')
            rider_info_len = len(rider_info)

            if rider_info_len >= 3:
                if rider_info_len == 4:
                  rider_sponsor = rider_info[1].lstrip()
                else:
                  rider_sponsor = None

                rider_name = rider_info[0]
                rider_city = rider_info[-2]
                rider_state = rider_info[-1]
                if rider_state == ' MO' or rider_state == ' KS':
                    #print '{},{},{},{},{},{},{}'.format(title, class_name, place.text, rider_name, rider_city, rider_state, rider_sponsor)
                    try:
                        places[int(place.text)] += 1
                    except:
                        places[int(place.text)] = 1
                   
                    ordinal = lambda n: "%d%s" % (n,"tsnrhtdd"[(n/10%10!=1)*(n%10<4)*n%10::4])
                    place_ordinal = ordinal(int(place.text))
                    #print '{}, {}, {}'.format(rider_name, place.text, class_name)
                    if rider_sponsor:
                        try:
                            rider_name = "{} ({})".format(rider_name, str(rider_sponsor))
                        except:
                            pass
                    print '{} - {} in {}'.format(rider_name, place_ordinal, class_name)
            else:
                pass


        count += 1
    print '\nPlace Count:'
    for k,v in places.iteritems():
        if v > 0:
            print '{} - {}'.format(k,v)

