import scratch

def main():
    tokenDepartment = "knt"
    tokenGroup = 351
    data = scratch.GetJson(tokenDepartment, tokenGroup) 
    # scratch.SaveJson(jsonData= data, fileName= "timetable/timetable_" + tokenDepartment + '_' + str(tokenGroup))
    for events in data["extramuralEvents"]: # найти токен очного, да и просто найти все токены
        print(events)
        print('\n')

if __name__ == "__main__":
	main()