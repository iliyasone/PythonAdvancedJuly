import asyncio

class Countdown:
    def __init__(self, sec: int, name: str) -> None:
        self._sec = sec
        self._name = name
    
    async def start(self):
        for i in range(self._sec, 0, -1):
            await asyncio.sleep(1)
            print(f'{self._name}:\t{i}')
        self._ready()
    def _ready(self):
        print(f'{self._name} done!')
        

async def main():
    cd = Countdown(5, "First")
    cd2 = Countdown(3, "Second")

    await asyncio.gather(cd.start(), cd2.start())

asyncio.run(main())