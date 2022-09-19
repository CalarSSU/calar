import scratch
import icalendar
from datetime import date, datetime, tzinfo
import pytz
shortenWeekDay = {
    7:'SU',
    6:'SA',
    5:'FR',
    4:'TH',
    1:'MO',
    3:'WE',
    2:'TU',
}

def convert(jsonData, educationType):
    Date = date.today()
    Day = datetime.weekday(Date)
    iCal = icalendar.Calendar()
    iCal.add('prodid', '-//My calendar product//example.com//')
    iCal.add('version', '2.0')
    for event in jsonData['lessons']:
        iEvent = icalendar.Event()
        iEvent.add('name', event['name'])
        iEvent.add('summary', event['name'])
        iTeacher = (event['teacher']['surname'] + " " 
        + event['teacher']['name'] + " " 
        + event['teacher']['patronymic'])
        iEvent.add('description', iTeacher)
        iEvent.add('location', event['place'])
        iEvent.add('dtstart'
                  , datetime( Date.year, Date.month,
                            Date.day + int(event['day']['dayNumber']) - Day - 1,
                            int(event['lessonTime']['hourStart']),
                            int(event['lessonTime']['minuteStart']), 0))
        iEvent.add('dtend'
                  , datetime( Date.year, Date.month,
                            Date.day + int(event['day']['dayNumber']) - Day - 1,
                            int(event['lessonTime']['hourEnd']),
                            int(event['lessonTime']['minuteEnd']), 0)
                  )
        iCal.add_component(iEvent)
    return iCal


def main():
    Department = "knt"
    Group = 351
    Education = "full"
    data = scratch.GetJson(Department, Education, Group) 
    ical = convert(data, Education)
    # for component in ical.walk():
    #     if component.name == "VEVENT":
            # print(component.get("name"))
            # print(component.get("description"))
            # print(component.get("organizer"))
            # print(component.get("location"))
            # print(component.decoded("dtstart"))
            # print(component.decoded("dtend"))
    scratch.SaveFile(ical, "timetable/"+ Department + '_' + str(Group), '.ics')

if __name__ == "__main__":
    main()