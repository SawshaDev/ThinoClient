import asyncio
import thino

client = thino.Client()

async def function():
    print(await client.tomboy())
    print(await client.neko())
    print(await client.femboy())
    print(await client.thighs())
    print(await client.porn())
    print(await client.hentai())
    await client.close()

asyncio.run(function())
