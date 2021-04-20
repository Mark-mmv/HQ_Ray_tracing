import sys, os, time
import time

sys.path.append(os.getcwd())
from vector3d import *
from ray import *


start = time.perf_counter()

origin = (1.0, 2.0, 3.0)
basis = (4.0, 5.0, 6.0)
r = Ray(origin, basis)

for i in range(0, 10**8, 1):
    r.basis / i
    r.origin / i

end = time.perf_counter()
print((end - start)*1000, 'ms')