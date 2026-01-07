import asyncio
import time
from datetime import datetime, timezone

def tst():
    time.sleep()

async def func1():
    print(f"{func1.__name__} started at {datetime.now(timezone.utc)}")
    await asyncio.sleep(2)
    tst()
    print(f"{func1.__name__} finished at {datetime.now(timezone.utc)}")
    

async def func2():
    print(f"{func2.__name__} started at {datetime.now(timezone.utc)}")
    await asyncio.sleep(5)
    print(f"{func2.__name__} finished at {datetime.now(timezone.utc)}")
    

async def func3():
    print(f"{func3.__name__} started at {datetime.now(timezone.utc)}")
    await asyncio.sleep(4)
    print(f"{func3.__name__} finished at {datetime.now(timezone.utc)}")
    


# await func1()
# await func2()
# await func3()

async def main():
    tasks = (func1(), func2(), func3())
    await asyncio.gather(*tasks)
    

asyncio.run(main())


# asyncio, anyio, uvloop