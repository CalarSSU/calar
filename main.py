import argparse
from curses.ascii import isdigit

from scratch import *
from config import *
from convert import *


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('-d',
                        metavar='DEPARTMENT',
                        help='choose department',
                        type=str,
                        default='knt')
    parser.add_argument('-f',
                        metavar='FORM',
                        help='choose education form',
                        type=str,
                        default='full')
    parser.add_argument('-g',
                        metavar='GROUP',
                        help='choose group',
                        type=str,
                        default='')
    parser.add_argument('-s',
                        metavar='SUBGROUP',
                        help='choose subgroup',
                        type=str,
                        default='')
    parser.add_argument('-i',
                        help='save results into DATA_DIR from config',
                        action=argparse.BooleanOptionalAction)
    cfg = parser.parse_args()

    prefix = './'
    if cfg.i:
        prefix = DATA_DIR

    if cfg.g == '':
        cfg.g = GROUPS[cfg.d][MAP_FORM[cfg.f]]

    for group in cfg.g.split():
        jsonData = getJson(cfg.d, cfg.f, group)

        if cfg.s == '':
            cfg.s = get_subgroups(jsonData) + " 0"

        for sg in cfg.s.split():
            if sg == '0':
                sg = ''

            iCalPath = \
                f'{prefix}/calendars/{cfg.d}/{MAP_FORM[cfg.f]}/{group}x{sg}.ics'

            iCal = json_to_ical(jsonData, sg)
            saveFile(iCal, iCalPath)
        cfg.s = ''


def get_subgroups(jsonData):
    subgrops = set()
    for event in jsonData['lessons']:
        sg = str(event['subGroup']).strip()
        if sg != '':
            if isdigit(sg[0]):
                subgrops.add(sg[0])
    return " ".join(subgrops)


if __name__ == "__main__":
    main()
