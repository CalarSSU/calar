import icalendar

from scratch import *
from date import *


def convert(jsonData, educationType, subGroup):
    curDate = date.today()
    firstSeptember = date(curDate.year, 9, 1)
    nom = (int(date.strftime(curDate, '%U')) -
           int(date.strftime(firstSeptember, '%U'))) % 2 == 0
    day = datetime.weekday(curDate) + 1
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
            eventDate = incDateByNum((curDate.year, curDate.month, curDate.day),
                                     int(event['day']['dayNumber']) - day)
            iEvent.add(
                'dtstart',
                datetime(eventDate[0], eventDate[1], eventDate[2],
                         int(event['lessonTime']['hourStart']),
                         int(event['lessonTime']['minuteStart']), 0))
            iEvent.add(
                'dtend',
                datetime(eventDate[0], eventDate[1], eventDate[2],
                         int(event['lessonTime']['hourEnd']),
                         int(event['lessonTime']['minuteEnd']), 0))
            iCal.add_component(iEvent)
    return iCal


def main():
    Department = 'knt'
    Group = '351'
    Education = 'full'
    SubGroup = '1'
    data = GetJson(Department, Education, Group)
    ical = convert(data, Education, SubGroup)
    fileName = Department + '_' + Group

    SaveFile(ical, "calendar/" + fileName + '.ics')
    SaveFile(GetRequest(Department, Education, Group),
             "json/" + fileName + '.json')


if __name__ == "__main__":
    main()
