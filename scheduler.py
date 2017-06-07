from apscheduler.schedulers.background import BlockingScheduler
from random import randrange
from time import sleep
from scrape_and_send import scrape_send


# delay the start a random time after the Scheduler to make scraping less obvious
def randStart():
    randsecs = randrange(1000)   # random number of seconds delay between 1 and 1000
    print(randsecs)
    sleep(randsecs)
    # print('running.')
    scrape_send()
    
sched = BlockingScheduler()
sched.add_job(randStart, trigger='cron', hour='17', minute='45') # host platform uses UTC time (2 hours behind)
# for adjusting the cron job see this link:
# http://apscheduler.readthedocs.io/en/latest/modules/triggers/cron.html#module-apscheduler.triggers.cron
sched.start()



