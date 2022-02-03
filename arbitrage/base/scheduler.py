from apscheduler.schedulers.background import BackgroundScheduler
from .views import collect_data


def start():
    scheduler = BackgroundScheduler()
    scheduler.add_job(func=collect_data, trigger="interval", seconds=5)
    scheduler.start()
