import multiprocessing
import threading
import time
from datetime import datetime, timezone


def proc1():
    res = 0
    start_time = datetime.now(timezone.utc)
    for i in range(1_000_000):
        res += i
    end_time = datetime.now(timezone.utc)
    print(f"Process1 spent {end_time - start_time} time, from {start_time} till {end_time}")

    return res


def proc2():
    res = 0
    start_time = datetime.now(timezone.utc)
    for i in range(1_000_000, 2_000_000):
        res += i
    end_time = datetime.now(timezone.utc)
        
    print(f"Process1 spent {end_time - start_time} time, from {start_time} till {end_time}")
    
    return res


# p1 = multiprocessing.Process(
#     target=proc1
# )
# p2 = multiprocessing.Process(
#     target=proc2
# )

# p1.start()
# p2.start()

# p1.join()
# p2.join()

# print(p1.exitcode)
# print(p2.exitcode)

t1 = threading.Thread(
    target=proc1
)
t2 = threading.Thread(
    target=proc2
)

t1.start()
t2.start()

t1.join()
t2.join()

# proc1()
# proc2()