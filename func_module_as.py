import datetime as dt

def module_show():
    module_type = dir(dt)
    print(module_type)

def date_now():
    return dt.datetime.now()

def remain_date():
    # print(dt.date.today())
    today = dt.date.today()
    print('오늘은 {}년 {}월 {}일입니다'.format(today.year, today.month, today.day))
    # print(dt.datetime.now().replace(month=12 , day=25))
    return dt.datetime(2020,12,25)-dt.datetime.now()

def remain_date_input(nmonth = 12, nday = 11):
    # print(dt.date.today())
    today = dt.date.today()
    print('오늘은 {}년 {}월 {}일입니다'.format(today.year, today.month, today.day))
    # print(dt.datetime.now().replace(month=12 , day=25))
    nmonth = int(input('원하는 월을 입력하세요'))
    nday = int(input('원하는 일을 입력하세요'))
    return dt.datetime(2020,nmonth,nday)-dt.datetime.now()

#nmonth = int(input('원하는 월을 입력하세요'))
#nday = int(input('원하는 일을 입력하세요'))
print(remain_date_input(nmonth,nday))