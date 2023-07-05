import asyncio
import aiohttp
import os

url: str = 'https://api.thecatapi.com/v1/images/search?limit=10'

def delete_cats():
    for file in os.listdir('cats'):
        os.remove('cats/' + file)

async def download_cat(
    session: aiohttp.ClientSession,
    url: str,
    n: int):
    
    format = url[-3:]
    
    response = await session.get(url)
    response_bytes = await response.read()
    
    with open(f'cats/cat{n}.{format}', 'wb') as file:
        file.write(response_bytes)
    
    print(f'cat{n}.{format}')
    
async def get_cats():
    async with aiohttp.ClientSession() as session:
        response = await session.get(url)
        json: list[dict[str, str]] = await response.json()
        
        url_cats = []
        for data in json:
            url_cats.append(data['url'])
            
        tasks = []
        for i in range(len(url_cats)):
            tasks.append(download_cat(session, url_cats[i], i))
        
        await asyncio.gather(*tasks)
        
def main():
    delete_cats()
    asyncio.run(get_cats())
    
    
if __name__ == "__main__":
    main()