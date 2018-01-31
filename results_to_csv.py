#!/usr/bin/env python

from bs4 import BeautifulSoup
import re

with open('sample_output.html') as f:
    soup = BeautifulSoup(f, 'html.parser')

groups = soup.findAll('h4', class_='race-result-group')

days = soup.findAll('div', id=re.compile('^rday_'))

print 'Race, Class, Place, Name, City, State, Sponsor'
for day in days:
    title = day.find('h3', class_='race-result-title')
    title = title.text
    # print 'RACE', title

    uls = day.findAll('ul', class_='race-result-list')
    count = 0
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
                  rider_sponsor = rider_info[1]
                else:
                    rider_sponsor = 'Privateer'

                rider_name = rider_info[0]
                rider_city = rider_info[-2]
                rider_state = rider_info[-1]
            else:
                pass

            if rider_state == ' MO' or rider_state == ' KS':
                print '{},{},{},{},{},{},{}'.format(title, class_name, place.text, rider_name, rider_city, rider_state, rider_sponsor)

        count += 1

