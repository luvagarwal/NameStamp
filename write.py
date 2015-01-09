import os
import uuid
from datetime import datetime, timedelta

import bitmap

BASE_DATE = datetime(2014, 10, 26)

def get_start_date():
    today_date = datetime.today()
    diff_date = today_date - BASE_DATE
    end_date = today_date - timedelta(diff_date.days%7)
    start_date = end_date - timedelta(50*7)
    return start_date

def print_nick():
    start_date = get_start_date()
    nick = raw_input('Enter your nick: ')
    nick = nick.upper()
    os.chdir('/home/luv/gitrepos/mine/tmp')
    for i in nick:
        start_date = print_letter(i, start_date)
        start_date += timedelta(7)
    os.system('git push')

def print_letter(letter, date):
    letter_bitmap = bitmap.alphabet[letter]
    month = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul',
              'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
    for i in letter_bitmap:
        if i!=0:
            with open('/home/luv/gitrepos/mine/tmp/README.md', 'w') as fp:
                fp.write(uuid.uuid4().hex)
            date_str = '%s %s %s %s' % (month[date.month-1], date.day, '23:59:59', date.year)
            os.system('git add README.md')
            os.system('git commit -m "%s" --date="%s"' %
                ('commit by NameStamp (https://github.com/luviiit/NameStamp)', date_str))
        date += timedelta(1)
    return date

def get_time_list(current_time, num, unit):
    item = current_time

    datetime_list=[]
    datetime_list.append(item)
    for i in xrange(num-1):
        if unit=='hour':
            item = item - timedelta(0,3600)
        if unit=='day':
            item = item - timedelta(1)
        if unit=='month':
            if item.month!=1:
                item = datetime(item.year,item.month-1,item.day,item.hour,item.second)
            else:
                item = datetime(item.year-1,12,item.day,item.hour,item.second)
        if unit=='year':
            item=datetime(item.year-1,item.month,item.day,item.hour,item.second)    
        datetime_list.append(item)
    return datetime_list

if __name__=='__main__':
    print_nick()
