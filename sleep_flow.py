import time
from prefect import flow


@flow(log_prints=True)
def sleep_flow():
    print("I'm tired, grandpa. Sleeping now.")
    time.sleep(60)
    print("Done sleeping. So well rested.")
