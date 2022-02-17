#!/usr/bin/env python

projects = ['ovrolwa', 'dsa110']
mdpath = './status/'

# map group to service and service to server:port
services = {'ovrolwa': {'webUI': '?'}, {'grafana': 'grafanaservice.lwa.pvt:3000'}, {'dashboard': 'lxdlwacr.sas.pvt:500?'},
            'dsa110': {'webUI': 'webserverUIservice.sas.pvt:9090'}, {'grafana': 'grafanaservice.ovro.pvt:3000'},
            {'dashboard': 'lxd110h23.sas.pvt:5008'}, {'hiplot': 'dsa-storage.ovro.pvt:5007'}, {'bokeh': 'bokehservice.ovro.pvt:5006'}}

# Projects are groups of servicese (e.g., OVRO-LWA, DSA-110)
# Services are individual web apps (e.g., webUI, hiplot)
# For each service, check on status and write a status line to the group markdown file.
# TODO: define method to check status

# Example line:
## OVRO-LWA webUI | Up | 13:18 8Feb2022

# Then push to github.
# Github Actions will aggregate md files, render to include.html, which is used by Squarespace.

# TODO: define scheme to render include.html that has richer interaction (e.g. bokeh plot)
