"""
Threading in python
"""

import threading
import time


def thread_function(name):
    print(f"Thread {name}: starting")
    time.sleep(2)
    print(f"Thread {name}: finishing")


print("Main    : before creating thread")
x = threading.Thread(target=thread_function, args=(1,))
print("Main    : before running thread")
x.start()
print("Main    : wait for the thread to finish")
x.join()
print("Main    : all done")
