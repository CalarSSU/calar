import scratch
import icalendar
import datetime

def convert(jsonData, educationType):
    iCal = icalendar.Calendar()
    iCal.add('prodid', '-//My calendar product//example.com//')
    iCal.add('version', '2.0')
    for event in jsonData['lessons']:
        iEvent = icalendar.Event()
        iEvent.add('name', event['name'])
        iTeacher = (event['teacher']['surname'] + " " 
        + event['teacher']['name'] + " " 
        + event['teacher']['patronymic'])
        iEvent.add('description', iTeacher)
        iEvent.add('location', event['place'])
        iCal.add_component(iEvent)
    return iCal


def main():
    Department = "knt"
    Group = 351
    Education = "full"
    data = scratch.GetJson(Department, Education, Group) 
    for event in data["lessons"]:
        print(event)
        print('\n')
    scratch.SaveFile(scratch.GetRequest(Department, Education, Group),
                    "timetable/"+ Department + '_' + str(Group), '.json')
    ical = convert(data, Education)
    for component in ical.walk():
        if component.name == "VEVENT":
            print(component.get("name"))
            print(component.get("description"))
            print(component.get("organizer"))
            print(component.get("location"))
            # print(component.decoded("dtstart"))
            # print(component.decoded("dtend"))
    scratch.SaveFile(ical, "timetable/"+ Department + '_' + str(Group), '.ics')

if __name__ == "__main__":
    main()