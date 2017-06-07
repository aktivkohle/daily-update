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
    

sched = BlockingScheduler()
# for testing use this line:
sched.add_job(randStart, 'interval', seconds=60)
# for production use this line:
# sched.add_job(randStart, 'interval', days=1)

sched.start()

