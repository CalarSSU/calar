import scratch
import icalendar
from datetime import date, datetime, tzinfo


def isLeapYear(year):
    return year % 400 == 0 or year % 100 != 0 and year % 4 == 0

def isLongMonth(month): 
    return month < 8 and month % 2 == 1 or month > 7 and month % 2 == 0 

def daysInMonth(data):
    if isLongMonth(data[1]): 
        return 31
    elif data[1] != 2: 
        return 30
    elif isLeapYear(data[0]): 
        return 29
    else: return 28

def incDateByNum(date, days):
    if days <= 0: 
        return date
    elif days <= daysInMonth(date) - date[2]:
        return (date[0], date[1], date[2] + days)
    elif date[1] == 12: 
        return incDateByNum((date[0] + 1, 1, 1)
                           , days - daysInMonth(date) + date[2] - 1)
    else: 
        return incDateByNum((date[0], date[1] + 1, 1)
                           , days - daysInMonth(date) + date[2] - 1)

def convert(jsonData, educationType, subGroup):
    Date = date.today()
    firstSeptember = date(int(Date.year), 9, 1)
    nom = (int(date.strftime(Date, '%U')) -
           int(date.strftime(firstSeptember, '%U'))) % 2
    Day = datetime.weekday(Date) + 1
    iCal = icalendar.Calendar()
    iCal.add('prodid', '-//Calar - a calendar that is always at hand : project '
             + 'within the course of programming technology at SSU University//'
             + 'example.com//')
    iCal.add('version', '2.0')
    for event in jsonData['lessons']:
        if ((event['subGroup'] == '' 
             or event['subGroup'].replace(' ', '')[0] == subGroup
             or event['subGroup'].replace(' ', '')[0] == 'с')
            and (event['weekType'] == 'FULL'
                 or event['weekType'] == 'DENOM' and nom == 1
                 or event['weekType'] == 'NOM' and nom == 0)):
            iEvent = icalendar.Event()
            iEvent.add('name', event['name'])
            iEvent.add('summary', event['name']
                       + '({0})'.format(event['lessonType'][0]))
            iTeacher = (event['teacher']['surname'] + " "
                        + event['teacher']['name'] + " "
                        + event['teacher']['patronymic'])
            iEvent.add('description', iTeacher)
            iEvent.add('location', event['place'])
            eventDate = incDateByNum((Date.year, Date.month, Date.day)
                                    , int(event['day']['dayNumber']) - Day)
            iEvent.add('dtstart'
                    , datetime( eventDate[0], eventDate[1]
                              , eventDate[2]
                              , int(event['lessonTime']['hourStart'])
                              , int(event['lessonTime']['minuteStart']), 0))
            iEvent.add('dtend'
                    , datetime( eventDate[0], eventDate[1]
                              , eventDate[2]
                              , int(event['lessonTime']['hourEnd'])
                              , int(event['lessonTime']['minuteEnd']), 0)
                    )
            iCal.add_component(iEvent)
    return iCal


def main():
    Department = 'knt'
    Group = 351
    Education = 'full'
    SubGroup = '2'
    data = scratch.GetJson(Department, Education, Group)
    ical = convert(data, Education, SubGroup)
    # for component in ical.walk():
    #     if component.name == "VEVENT":
    # print(component.get("name"))
    # print(component.get("description"))
    # print(component.get("organizer"))
    # print(component.get("location"))
    # print(component.decoded("dtstart"))
    # print(component.decoded("dtend"))
    scratch.SaveFile(ical, "timetable/" + Department +
                     '_' + str(Group), '.ics')


if __name__ == "__main__":
    main()
