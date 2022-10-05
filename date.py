from datetime import date, datetime, tzinfo


def isLeapYear(year: int) -> bool:
    return year % 400 == 0 or year % 100 != 0 and year % 4 == 0


def isLongMonth(month: int) -> bool:
    return month < 8 and month % 2 == 1 or month > 7 and month % 2 == 0


def daysInMonth(date: (int, int, int)) -> int:
    if isLongMonth(date[1]):
        return 31
    elif date[1] != 2:
        return 30
    elif isLeapYear(date[0]):
        return 29
    else:
        return 28


def incDateByNum(date: (int, int, int), days: int) -> (int, int, int):
    if days <= 0:
        return date
    elif days <= daysInMonth(date) - date[2]:
        return (date[0], date[1], date[2] + days)
    elif date[1] == 12:
        return incDateByNum((date[0] + 1, 1, 1),
                            days - daysInMonth(date) + date[2] - 1)
    else:
        return incDateByNum((date[0], date[1] + 1, 1),
                            days - daysInMonth(date) + date[2] - 1)
