import json
import requests
import icalendar
#Нужно получать все токены с сайта

def GetRequest (tokenDepartment, tokenEducation, tokenGroup):
    return requests.get("https://scribabot.tk/api/v1.0/schedule/" 
            + tokenEducation + "/" + tokenDepartment + "/" + str(tokenGroup))

def GetJson(tokenDepartment, tokenEducation, tokenGroup):
    getString = GetRequest(tokenDepartment, tokenEducation, tokenGroup)
    return json.loads(getString.text)

def SaveFile(requestData, fileName , extention):
        if extention == ".ics":
            with open(file=fileName + extention, mode='wb') as file:
                file.write(requestData.to_ical())
        else:
            with open(file=fileName + extention, mode='w') as file:
                file.write(requestData.text) 
