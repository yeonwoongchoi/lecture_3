import func_module
import func_module_as
import math_module as mm

#func_module.module_show()

nowdate = func_module.date_now()
now_year = nowdate.year
now_month = nowdate.month
now_day = nowdate.day
#print(nowdate)
print(now_year,'년',now_month,'월',now_day,'일')
xmas = nowdate.replace(month = 12, day = 25)
print(xmas)


#date_today = '{}년 {}월 {}일'.format(nowdate.year , nowdate.month ,nowdate.day) 이외의 방법은 무수히 많다.




ndate = func_module_as.date_now()
print(ndate)

func_module_as.remain_date()

re_date = func_module_as.remain_date_input()                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 
print(re_date)

mm.math_pow()