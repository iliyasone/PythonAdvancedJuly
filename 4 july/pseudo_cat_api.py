from random import random
import asyncio

async def pseudo_download(n: int):
    print(f'Cat {n} start download')
    await asyncio.sleep(random())
    print(f'Cat {n} done!')
    
async def main():
    tasks = []
    for i in range(10):
        tasks.append(pseudo_download(i))
    await asyncio.gather(*tasks)

asyncio.run(main())
    
