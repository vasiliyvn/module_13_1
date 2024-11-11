
import asyncio


async def start_strongman(name, power):
    print(f'Силач {name} начал соревнования.')
    for i in range(1, 6):
        await asyncio.sleep(1 / power)
        print(f'Силач {name} поднял {i}')
    print(f'Силач {name} закончил соревнования.')


async def start_tournament():
    task = asyncio.create_task(start_strongman('Pasha', 3))
    task1 = asyncio.create_task(start_strongman('Denis', 4))
    task2 = asyncio.create_task(start_strongman('Apollon', 5))
    await task
    await task1
    await task2

asyncio.run(start_tournament())
