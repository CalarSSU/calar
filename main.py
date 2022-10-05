import icalendar
import json
from datetime import date, datetime, tzinfo, timedelta

from scratch import *

UPDATE_FREQUENCY_IN_SECONDS = 86_400


def convert(jsonData, educationType, subGroup):
    curDate = date.today()
    firstSeptember = date(curDate.year, 9, 1)
    nom = (int(date.strftime(curDate, '%U')) -
           int(date.strftime(firstSeptember, '%U'))) % 2 == 0
    weekday = datetime.weekday(curDate) + 1
    iCal = icalendar.Calendar()
    iCal.add(
        'prodid', '-//Calar - a schedule that is always at hand : project '
        'within the course of programming technology at SSU University//'
        'example.com//')
    iCal.add('version', '2.0')
    for event in jsonData['lessons']:
        isCorrectSubGroup = (event['subGroup'] == ''
                             or event['subGroup'].split()[0] == subGroup
                             or event['subGroup'].split()[0] == 'с')
        isNom = (event['weekType'] == 'FULL'
                 or event['weekType'] == 'DENOM' and not nom
                 or event['weekType'] == 'NOM' and nom)
        if isCorrectSubGroup and isNom:
            iEvent = icalendar.Event()
            iEvent.add('name', event['name'])
            iEvent.add('summary',
                       event['name'] + '({0})'.format(event['lessonType'][0]))
            iTeacher = (event['teacher']['surname'] + " " +
                        event['teacher']['name'] + " " +
                        event['teacher']['patronymic'])
            iEvent.add('description', iTeacher)
            iEvent.add('location', event['place'])
            diffDays = int(event['day']['dayNumber']) - weekday
            eventDate = curDate + timedelta(days=diffDays)
            iEvent.add(
                'dtstart',
                datetime(eventDate.year, eventDate.month, eventDate.day,
                         event['lessonTime']['hourStart'],
                         event['lessonTime']['minuteStart'], 0))
            iEvent.add(
                'dtend',
                datetime(eventDate.year, eventDate.month, eventDate.day,
                         event['lessonTime']['hourEnd'],
                         event['lessonTime']['minuteEnd'], 0))
            iCal.add_component(iEvent)
    return iCal


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

    iCal = convert(jsonData, Education, SubGroup)
    saveFile(iCal, iСalPath)


if __name__ == "__main__":
    main()
