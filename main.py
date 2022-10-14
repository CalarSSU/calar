import argparse

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
                        default='351')
    parser.add_argument('-s',
                        metavar='SUBGROUP',
                        help='choose subgroup',
                        type=str,
                        default='1')
    cfg = parser.parse_args()

    for group in cfg.g.split():
        fileName = cfg.d + '_' + group
        jsonPath = "json/" + fileName + '.json'
        iСalPath = "calendar/" + fileName + '.ics'

        jsonData = getJson(cfg.d, cfg.f, group)
        saveFile(jsonData, jsonPath)

        iCal = json_to_ical(jsonData, cfg.s)
        saveFile(iCal, iСalPath)


if __name__ == "__main__":
    main()

