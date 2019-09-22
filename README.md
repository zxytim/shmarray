# shmarray

**NOTE**: If you are using Python 3.8, please turn to 
[multiprocessing.shared_memory](https://docs.python.org/3.8/library/multiprocessing.shared_memory.html#module-multiprocessing.shared_memory)
instead.

-----

shmarray is a shared numpy-array implementation utilizing
multiprocessing.sharedctypes.  It is a quite useful small library created of
David Baddeley. I found it at
https://github.com/lucastheis/parallel/blob/master/shmarray.py

Despite its usefulness, it not only does not come with a pip-installable
package, but also contains disrepaired bugs. 

This repo is created as a remedy.

# Installation
```
pip install shmarray
```

# Usage

`test.py`
```python
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
```

Result:
```bash
$ python3 test.py
[1. 1. 1. 1. 1. 1. 1. 1. 1. 1.]
[1. 1. 1. 1. 1. 1. 1. 1. 1. 1.]
[2. 2. 2. 2. 2. 2. 2. 2. 2. 2.]
[2. 2. 2. 2. 2. 2. 2. 2. 2. 2.]
[3. 3. 3. 3. 3. 3. 3. 3. 3. 3.]
[3. 3. 3. 3. 3. 3. 3. 3. 3. 3.]
[4. 4. 4. 4. 4. 4. 4. 4. 4. 4.]
[4. 4. 4. 4. 4. 4. 4. 4. 4. 4.]
[5. 5. 5. 5. 5. 5. 5. 5. 5. 5.]
[5. 5. 5. 5. 5. 5. 5. 5. 5. 5.]
[6. 6. 6. 6. 6. 6. 6. 6. 6. 6.]
[6. 6. 6. 6. 6. 6. 6. 6. 6. 6.]
...
```

# Under the hood
The code in `shmarray.py` is mostly the same as the original, I've only done a few things:
1. fix a bug that did not pass `dtype` argument to downstream calls
2. fix python version compatibility bugs
3. reformat the code using [black](https://github.com/psf/black)
