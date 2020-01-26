#!/usr/bin/env python3
import sys
import argparse
import os
import requests
import yaml
import operator
import logging
from functools import reduce  # forward compatibility for Python 3


def parse_args():
    parser = argparse.ArgumentParser(
        description="Configure NZBHydra based on environment variables")
    parser.add_argument("-v",
                        "--verbose",
                        help="Be verbose",
                        action="store_true",
                        dest="verbose")
    parser.add_argument("-d", "--data", default="/data", help="Data directory")

    return parser.parse_args()


def getFromDict(dataDict, mapList):
    return reduce(operator.getitem, mapList, dataDict)


def setInDict(dataDict, mapList, value):
    getFromDict(dataDict, mapList[:-1])[mapList[-1]] = value


def main():
    args = parse_args()

    upstream_yml_url = (
        "https://raw.githubusercontent.com/theotherp/nzbhydra2/master/"
        "core/src/main/resources/config/baseConfig.yml")

    env_mapping = {
        'NZBHYDRA_BACKUP_DAYS': {
            'map': 'main.backupEveryXDays',
            'force_type': int
        },
        'NZBHYDRA_APIKEY': {
            'map': 'main.apiKey',
            'force_type': str
        },
        'NZBHYDRA_BACKUP_KEEP_WEEKS': {
            'map': 'main.deleteBackupsAfterWeeks',
            'force_type': int
        }
    }

    force_mapping = {
        'main.updateCheckEnabled': False,
        'main.showUpdateBannerOnDocker': False
    }

    yml_config = os.path.join(args.data, "nzbdrone.yml")
    if not os.path.exists(yml_config):
        existing_config = yaml.load(requests.get(upstream_yml_url).text)

    # Set up forced mapping values
    for mapping, value in force_mapping.items():
        mapping_list = mapping.split(".")
        existing_value = str(getFromDict(existing_config, mapping_list))
        if existing_value != value:
            logging.warning(f"Setting {mapping} to {value}")
            setInDict(existing_config, mapping_list, value)

    # Set up some optional mapping values
    for env_name, mapping in env_mapping.items():
        new_value = os.environ.get(env_name)
        if new_value:
            map_list = mapping['map'].split(".")
            existing_value = str(getFromDict(existing_config, map_list))

            if new_value != existing_value:
                logging.warning(f"Setting {mapping['map']} to {new_value}")
                setInDict(existing_config, map_list,
                          mapping['force_type'](new_value))

    print(yaml.dump(existing_config))

    return 0


if __name__ == "__main__":
    sys.exit(main())
