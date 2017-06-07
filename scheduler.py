from apscheduler.schedulers.background import BlockingScheduler
from random import randrange
from time import sleep
from scrape_and_send import scrape_send


def randStart():
	# for testing use this line:
    randsecs = randrange(10)	
	# for production use this line:	
    # randsecs = randrange(3600)
    print(randsecs)
    sleep(randsecs)
    # print('running.')
    scrape_send()
    
# http://apscheduler.readthedocs.io/en/latest/modules/triggers/cron.html#module-apscheduler.triggers.cron
sched = BlockingScheduler()
sched.add_job(my_job, trigger='cron', hour='16', minute='00') # platform uses UTC time (2 hours behind)
# second job for testing:
sched.add_job(my_job, trigger='cron', hour='16', minute='01', second='15') 
sched.start()

