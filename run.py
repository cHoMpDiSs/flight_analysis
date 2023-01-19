from app import app, views

from apscheduler.schedulers.background import BackgroundScheduler
from apscheduler.triggers.combining import OrTrigger
from apscheduler.triggers.cron import CronTrigger

trigger = CronTrigger(minute='*/1')


from app.functions import plotting
from app.flight_data import update_flight_data, cut_off_delay

sched = BackgroundScheduler()
sched.add_job(update_flight_data, trigger)
sched.add_job(cut_off_delay, trigger)
sched.add_job(plotting, trigger)

sched.start()


if __name__ == "__main__":

    app.run()