import icalendar
from datetime import date, datetime, timedelta

from config import *


def json_to_ical(jsonData, subGroup):
    iCal = icalendar.Calendar()
    iCal.add(
        'prodid', '-//Calar - a schedule that is always at hand : project '
        'within the course of programming technology at SSU University//'
        'example.com//')
    iCal.add('version', '2.0')

    startDay, startMonth = map(int,
                               SEMESTER_TIME[CUR_SEMESTER]['start'].split('.'))
    endDay, endMonth = map(int, SEMESTER_TIME[CUR_SEMESTER]['end'].split('.'))
    endDate = date(date.today().year, endMonth, endDay)
    for event in jsonData['lessons']:
        isCorrectSubGroup = (event['subGroup'] == ''
                             or event['subGroup'].split()[0] == subGroup
                             or event['subGroup'].split()[0] == 'с')
        if not isCorrectSubGroup:
            continue

        curDate = date(date.today().year, startMonth, startDay)
        while curDate < endDate:
            fill_event(iCal, curDate, event)
            curDate += timedelta(weeks=1)

    return iCal


def fill_event(iCal, curDate, event):
    firstSeptember = date(curDate.year, 9, 1)
    isNom = (int(date.strftime(curDate, '%U')) -
             int(date.strftime(firstSeptember, '%U'))) % 2 == 0
    weekday = datetime.weekday(curDate) + 1
    isCorrectNom = (event['weekType'] == 'FULL'
                    or event['weekType'] == 'DENOM' and not isNom
                    or event['weekType'] == 'NOM' and isNom)
    if isCorrectNom:
        iEvent = icalendar.Event()
        iEvent.add('name', event['name'])
        iEvent.add('summary',
                   event['name'] + ' ' + LESSON_TYPES[event["lessonType"]])
        iTeacher = (event['teacher']['surname'] + " " +
                    event['teacher']['name'] + " " +
                    event['teacher']['patronymic'])
        iEvent.add('description', iTeacher)
        iEvent.add('location', event['place'])
        diffDays = event['day']['dayNumber'] - weekday
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

