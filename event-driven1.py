"""
Using 'asyncio' modlule in python to run asynchronous tasks concurrently using a single thread.

Ali Dadgar - 2020
"""

import asyncio

''' global params '''
var1 = 0 # varibale to be handled in function loop1()
var2 = 0 # variable to be handled in function loop2()
halt = 0.000001 # sleep time between functions (to let the other functions implement)

''' function responsible to change (handle) var1 '''
async def loop1():
    global var1, var2
    for _ in range(10000):
        var1 += 1.5
        await asyncio.sleep(halt)
        if (var1 + var2) % 193 == 0:
            print("Found a match: ", var1, var2)

''' function responsible to change (handle) var2 '''
async def loop2():
    global var2
    for _ in range(10000):
        var2 += 3
        await asyncio.sleep(halt)

''' main function - responsible to handle both'''
async def main():
    task1 = asyncio.create_task(loop1())
    task2 = asyncio.create_task(loop2())
    await task1
    await task2

asyncio.run(main())