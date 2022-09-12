import json
import requests


def GetJson(tokenDepartment, tokenGroup): #Нужно получать эти токены с сайта
    getString = "https://scribabot.tk/api/v1.0/schedule/extramural/" + tokenDepartment + "/" + str(tokenGroup)
    return json.loads(requests.get(getString).text)

# def SaveJson(jsonData, fileName):
    # with open(file=fileName+ '.json', mode='w') as file:
        # file.write(jsonData) переписать через реквесты


# getDepartment = input("Department: ")
# getGroup = input("Group : ")
# todos = json.loads(response.text)
# print(todos == response.json()) # True
# print(response.json())
# with open("test.json","w") as file:
#   file.write(jsonData.text)
# with open("data.json", "w") as file:
#     file.write(requests.get(getString).text)