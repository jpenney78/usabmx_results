#!/usr/bin/env python

from bs4 import BeautifulSoup
import urllib3
import re
import sys
import collections

def get_results(url):
    # url = 'https://www.usabmx.com/site/bmx_races/448450/results?past_only=1&section_id=228'
    http = urllib3.PoolManager()
    r = http.request('GET', url)
    page = r.data
    soup = BeautifulSoup(page, 'html.parser')
    groups = soup.findAll('h4', class_='race-result-group')

    days = soup.findAll('div', id=re.compile('^rday_'))
    res = str()

    for day in days:
        title = day.find('h3', class_='race-result-title')
        
        if title is None:
            exit(0)

        title = title.text

        res += '\n\n----------------------------------\n'
        res += 'RACE: {}\n'.format(title)
        res += '----------------------------------\n'

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
                        place_text = place.text
                        if place_text == 'O' or place_text == 'S':
                            place_text = 1
                        try:
                            places[int(place_text)] += 1
                        except:
                            places[int(place_text)] = 1
                    
                        ordinal = lambda n: "%d%s" % (n,"tsnrhtdd"[(n/10%10!=1)*(n%10<4)*n%10::4])
                        place_ordinal = ordinal(int(place_text))
                        #print '{}, {}, {}'.format(rider_name, place.text, class_name)
                        if rider_sponsor:
                            try:
                                rider_name = "{} ({})".format(rider_name, str(rider_sponsor))
                            except:
                                pass
                        res += '{} - {} in {}\n'.format(rider_name, place_ordinal, class_name)
                else:
                    pass


            count += 1
        res += '\nPlace Count:\n'
        for i in places:
            if places[i] > 0:
                res += f"{i} - {places[i]}\n"

    return res

