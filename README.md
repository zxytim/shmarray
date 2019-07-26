# shmarray
shmarray is a shared numpy-array implementation utilizing
multiprocessing.sharedctypes.  It is a quite useful small library created of
David Baddeley. I found it at
https://github.com/lucastheis/parallel/blob/master/shmarray.py

Despite its usefulness, it not only does not come with a pip-installable
package, but also contains disrepaired bugs. 

This repo is created to amend these remedies. 

# Installation
```
pip install shmarray
```

# Usage


# PS
The code in `shmarray.py` is mostly the same as the original, I've only done two things:
1. fix a bug that did not pass `dtype` argument to downstream calls
2. reformat the code using [black](https://github.com/psf/black)
