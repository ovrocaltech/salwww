import time
import os.path
import requests
import argparse

projects = ['ovrolwa', 'dsa110', 'ovro']
mdpath = './status/'

# map group to service and service to server:port
services = {'ovrolwa': {'webUI': 'webserveruiservice.lwa.pvt:9090', 'grafana': 'grafanaservice.lwa.pvt:3000',
                        'dashboard': 'lxdlwacr.sas.pvt:5006', 'LWASNAP': 'greghell.github.io/LWASNAP',
                        'lwamaas': 'lwamaas.lwa.pvt:5240'},
            'dsa110': {'webUI': 'webserverUIservice.sas.pvt:9090', 'grafana': 'grafanaservice.sas.pvt:3000',
                       'dashboard': 'lxd110h23.sas.pvt:5008', 'hiplot': None,
                       'archive': 'code.deepsynoptic.org/dsa110-archive',
                       'dsa110maas': 'dsa110maas.ovro.pvt:5240'},
            'ovro': {}}
#'bokeh': 'bokehservice.sas.pvt:5006'  # deprecated

# TODO:
# - need route to dsa-storage for hiplot: 'dsa-storage.ovro.pvt:5007'
# - automatic push
# - define scheme to render include.html that has richer interaction (e.g. bokeh plot)

def run(project):
    """ Check services in project to make md files.
    Projects are groups of servicese (e.g., OVRO-LWA, DSA-110). Can be list of str or a str.
    Services are individual web apps (e.g., webUI, hiplot)
    For each service, check on status and write a status line to the group markdown file.

    Example md line:
    OVRO-LWA | webUI | Up | Sat Mar 5 22:33:06 2022

    Github Actions will aggregate md files, render to include.html, which is used by Squarespace.
    """

    if isinstance(project, str):
        projectlist = [project]
    elif isinstance(project, list):
        projectlist = project

    for project in projectlist:
        with open(os.path.join(mdpath, f'{project}.md'), 'w') as fp:
            for service in services[project].keys():
                if services[project][service] is not None:
                    url = f'http://{services[project][service]}'
                    print(f'Checking {url}')

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


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Get project name')
    parser.add_argument('--project', help='project name(s) (list or string)', default=projects)
    parser.add_argument('--loop', help='repeat timescale in minutes (indefinite)', default=0, type=float)
    args = parser.parse_args()

    while True:
        try:
            run(args.project)
        except KeyboardInterrupt:
            print('Escaping loop...')

        if not args.loop:
            break
        else:
            print(f'Sleeping for {args.loop} minutes...')
            time.sleep(args.loop*60)

