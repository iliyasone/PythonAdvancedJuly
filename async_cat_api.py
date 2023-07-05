import aiohttp
import asyncio
from decorators import time_measure_decorator
url = 'https://api.thecatapi.com/v1/images/search?limit=10'

async def download(session: aiohttp.ClientSession,
                   url: str, 
                   n: int):
    """Скачивает одного котёнка"""
    print(f'Cat {n} start download')
    response = await session.get(url)
    response_bytes = await response.read()
    
    file = open(f'cats/cat{n}.jpg', 'wb') # write bytes
    file.write(response_bytes)
    file.close()
    
    print(f'Cat {n} done!')
    
async def main():
    session = aiohttp.ClientSession()
    
    response = await session.get(url)
    response_json = await response.json()    

    url_cats = []
    for data in response_json:
        url_cats.append(data['url'])


    tasks = []
    for i in range(10):
        tasks.append(download(session, url_cats[i], i))
    await asyncio.gather(*tasks)
    
    response.release()

    await session.close()

@time_measure_decorator
def sync_main():
    asyncio.run(main())
    
sync_main()
