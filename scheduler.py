from apscheduler.schedulers.background import BlockingScheduler
from random import randrange
from time import sleep
from scrape_and_send import scrape_send


def randStart():
    randsecs = randrange(3600)
    print(randsecs)
    sleep(randsecs)
    # print('running.')
    scrape_send()
    

sched = BlockingScheduler()
# for testing
# sched.add_job(randHello, 'interval', seconds=60)
sched.add_job(randStart, 'interval', days=1)

sched.start()

