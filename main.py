import icalendar
import json
from datetime import date, datetime, tzinfo, timedelta

from scratch import *
from config import *
from convert import *

def main():
    Department = 'knt'
    Group = '351'
    Education = 'full'
    SubGroup = '1'
    fileName = Department + '_' + Group
    jsonPath = "json/" + fileName + '.json'
    iСalPath = "calendar/" + fileName + '.ics'

    jsonData = getJson(Department, Education, Group)
    saveFile(jsonData, jsonPath)

    iCal = json_to_ical(jsonData, Education, SubGroup)
    saveFile(iCal, iСalPath)


if __name__ == "__main__":
    main()
