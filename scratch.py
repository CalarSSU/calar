import json
import requests
import icalendar
import os


def GetRequest(tokenDepartment, tokenEducation, tokenGroup):
    return requests.get("https://scribabot.tk/api/v1.0/schedule/" +
                        tokenEducation + "/" + tokenDepartment + "/" +
                        tokenGroup)


def GetJson(tokenDepartment, tokenEducation, tokenGroup):
    getString = GetRequest(tokenDepartment, tokenEducation, tokenGroup)
    return json.loads(getString.text)


def SaveFile(requestData, filePath):
    folder = filePath.rsplit('/', maxsplit=1)[0]
    os.makedirs(folder, exist_ok=True)
    if filePath.split('.')[-1] == 'ics':
        with open(file=filePath, mode='wb') as file:
            file.write(requestData.to_ical())
    else:
        with open(file=filePath, mode='w') as file:
            file.write(requestData.text)
