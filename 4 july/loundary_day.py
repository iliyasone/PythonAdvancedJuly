import asyncio
K = 0.1

async def loundary():
    print("Начали стирку")
    await asyncio.sleep(70*K)
    print("Закончили стирку")
    
async def soup():
    print("Начали готовку")
    await asyncio.sleep(60*K)
    print("Едим суп!")
    
async def tea(name: str):
    print(f"Чайник {name} на плите")
    await asyncio.sleep(15*K)
    print(f"Буль-буль, можно пить чай из чайника {name}!")
    
async def sync_main():
    await loundary()
    await soup()
    await tea()
    
async def async_main():
    await asyncio.gather(
        loundary(), 
        soup(), 
        tea("Черный"), 
        tea("Крутой")
    )

asyncio.run(async_main())