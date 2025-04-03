import time
from prefect import flow


@flow
def sleep_flow():
    print("I'm tired, grandpa. Sleeping now.")
    time.sleep(300)
    print("Done sleeping. So well rested.")
