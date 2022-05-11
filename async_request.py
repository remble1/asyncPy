# here is my test with async requests
import asyncio
import aiohttp
import requests
import os
import time

api_key = os.getenv('ALPHAVANTAGE_API_KEY')
url = 'https://www.alphavantage.co/query?function=OVERVIEW&symbol={}&apikey={}'
symbols = ['AAPL', 'GOOG', 'TSLA', 'MSFT', 'PEP', 'AAPL', 'AAPL', 'GOOG', 'TSLA', 'MSFT', 'PEP',
           'AAPL', 'AAPL', 'GOOG', 'TSLA', 'MSFT', 'PEP', 'AAPL', 'AAPL', 'GOOG', 'TSLA', 'MSFT', 'PEP', 'AAPL']
results = []

print("Timer started...")
start = time.time()


async def get_symbols():
    async with aiohttp.ClientSession() as session:
        for symbol in symbols:
            response = await session.get(url.format(symbol, api_key), ssl=False)
            results.append(await response.json())


# get_symbols()
asyncio.run(get_symbols())
# loop = asyncio.get_event_loop() #making object loop
# loop.run_until_complete(get_symbols())
# asyncio.close()

end = time.time()
total_time = end - start
print("It took {} seconds to make {} API calls".format(total_time, len(symbols)))
