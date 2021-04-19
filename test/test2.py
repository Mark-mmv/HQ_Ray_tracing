import sys, os, time
import time

sys.path.append(os.getcwd())
from vector3d import *


start = time.perf_counter()

vec = Vector(3.0, 4.0, 10.0)
for i in range(0, 10**6, 1):
    vec / i

end = time.perf_counter()
print(end - start)