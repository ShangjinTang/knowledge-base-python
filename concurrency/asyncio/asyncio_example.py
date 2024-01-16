#!/usr/bin/env python3

import asyncio
import time


async def brewCoffee():
    print("Start brewCoffee()")
    await asyncio.sleep(3)
    print("End brewCoffee()")


async def toastBread():
    print("Start toastBread()")
    await asyncio.sleep(2)
    print("End toastBread()")


async def main():
    start_time = time.time()
    await asyncio.gather(brewCoffee(), toastBread())
    task_brew_coffee = asyncio.create_task(brewCoffee())
    task_toast_bread = asyncio.create_task(toastBread())
    await task_brew_coffee
    await task_toast_bread
    end_time = time.time()
    elapsed_time = end_time - start_time

    print(f"Total execution time: {elapsed_time:.2f} seconds")


if __name__ == "__main__":
    asyncio.run(main())
