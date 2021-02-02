#!/usr/bin/sh
from crontab import CronTab

cron = CronTab(user='danielkearney-spaw')
job = cron.new(command='cd / && cd /Users/danielkearney-spaw/Desktop/wsbapi/auth && /usr/bin/python example1.py')
job.minute.every(1)

cron.write()