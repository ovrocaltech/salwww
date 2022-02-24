#!/usr/bin/env python
import time
import os.path
import requests


projects = ['ovrolwa', 'dsa110']
mdpath = './status/'

# map group to service and service to server:port
services = {'ovrolwa': {'webUI': None, 'grafana': 'grafanaservice.lwa.pvt:3000', 'dashboard': 'lxdlwacr.sas.pvt:500?',
                        'LWASNAP': 'greghell.github.io/LWASNAP'},
            'dsa110': {'webUI': 'webserverUIservice.sas.pvt:9090', 'grafana': 'grafanaservice.ovro.pvt:3000',
                       'dashboard': 'lxd110h23.sas.pvt:5008', 'hiplot': 'dsa-storage.ovro.pvt:5007',
                       'bokeh': 'bokehservice.sas.pvt:5006', 'archive': 'code.deepsynoptic.org/dsa110-archive'}}

for project in projects:
    with open(os.path.join(mdpath, f'{project}.md'), 'w') as fp:
        for service in services[project].keys():
            url = f'http://{services[project][service]}'
            print(url)
            if services[project][service] is not None:
                status = 'Down'
                try:
                    resp = requests.get(url)
                    if resp.ok:
                        status = 'Up'
                except requests.exceptions.ConnectionError:
                    status = 'Down'
            else:
                status = 'in development'
            fp.write(f'{project} | {service} | {status} | {time.ctime()}\n')

# Projects are groups of servicese (e.g., OVRO-LWA, DSA-110)
# Services are individual web apps (e.g., webUI, hiplot)
# For each service, check on status and write a status line to the group markdown file.
# TODO: define method to check status

# Example line:
## OVRO-LWA webUI | Up | 13:18 8Feb2022

# Then push to github.
# Github Actions will aggregate md files, render to include.html, which is used by Squarespace.

# TODO: define scheme to render include.html that has richer interaction (e.g. bokeh plot)
