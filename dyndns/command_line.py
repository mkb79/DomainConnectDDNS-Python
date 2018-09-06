from __future__ import print_function
import argparse
import json
import validators

from dyndns import domain_setup
from dyndns import domain_update
from dyndns import domain_status

def main():
    parser = argparse.ArgumentParser(description="Config domain for DynDNS")

    parser.add_argument('action', choices=['setup', 'update', 'status'], help="action to be performed on domain(s)")
    parser.add_argument('--config', type=str, default='settings.txt', help="config file path")

    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument('--domain', type=str, help="domain to keep up to date")
    group.add_argument('--all', action='store_true', help="update all domains in config")

    args = parser.parse_args()

    action = args.action
    domain = args.domain
    all = args.all
    settings = args.config

    # validate domain
    if domain and not validators.domain(domain) is True:
        print("Domain is not valid.")
        return

    if all and action == 'setup':
        print("Bulk setup not supported")
        return

    domains = []
    if all:
        try:
            with open(settings, "r") as settings_file:
                try:
                    config = json.load(settings_file)
                except ValueError:
                    config = {}
        except IOError:
            print("Couldn't read setttings.")
        domains = config.keys()
    elif domain:
        domains = [domain, ]

    for domain in domains:
        if action == 'setup':
            print(domain_setup.main(domain, settings))
        elif action == 'update':
            print(domain_update.main(domain, settings))
        elif action == 'status':
            print(domain_status.main(domain, settings))
