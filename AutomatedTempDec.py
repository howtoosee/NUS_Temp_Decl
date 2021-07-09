import schedule, time
from TempDec import declareAmTemp, declarePmTemp
from datetime import datetime as dt

schedule.every().day.at("01:00").do(declareAmTemp)
schedule.every().day.at("13:00").do(declarePmTemp)

while True:
    schedule.run_pending()
    time.sleep(100)
    # 10 - 1 minute
    # 600 - 1 hour
    