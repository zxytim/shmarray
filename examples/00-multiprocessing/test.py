from multiprocessing import Process
import time

import shmarray

def worker(data):
    while True:
        data += 1
        time.sleep(1)


def monitor(data):
    while True:
        print(data)
        time.sleep(0.5)

data = shmarray.zeros(10)

procs = [
    Process(target=worker, args=(data, )),
    Process(target=monitor, args=(data, )),
]


for p in procs:
    p.start()

for p in procs:
    p.join()
