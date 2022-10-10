import json
import requests
import os


def getRequest(tokenDepartment, tokenEducation, tokenGroup):
    return requests.get("https://scribabot.tk/api/v1.0/schedule/" +
                        tokenEducation + "/" + tokenDepartment + "/" +
                        tokenGroup)


def getJson(tokenDepartment, tokenEducation, tokenGroup):
    getString = getRequest(tokenDepartment, tokenEducation, tokenGroup)
    return json.loads(getString.text)


def saveFile(requestData, filePath):
    folder = filePath.rsplit('/', maxsplit=1)[0]
    os.makedirs(folder, exist_ok=True)
    if filePath.split('.')[-1] == 'ics':
        with open(file=filePath, mode='wb') as file:
            file.write(requestData.to_ical())
    else:
        with open(file=filePath, mode='w') as file:
            json.dump(requestData, file, ensure_ascii=False)

