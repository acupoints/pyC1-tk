import time
import threading
from threading import Thread

def wait():
    time.sleep(0.1)

while 1:
    try:
        Thread(target=wait, name='test_thread').start()
        print(f'-->Failed at {len(threading.enumerate())} threads in.')
    except RuntimeError as f:
        print(f'Failed at {len(threading.enumerate())} threads in.')
        print(str(f))
        break