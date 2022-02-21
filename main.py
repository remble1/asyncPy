import asyncio

async def main1():
    print("elo")
    task = asyncio.create_task((foo('zadanie w połowie')))
    await asyncio.sleep(2) # poczeka aż wszystkie taski się skończą
    print("koniec")

async def foo(text):
    print(text)
    await asyncio.sleep(1)
    print("drugi zakonczony")

####################################################################################

async def fench_data(): # async iunformuje że to funkcja asynchornicnz i tylko w takiej działa await
    print('start fetching') # rozpocznij pierwszy wątek
    await asyncio.sleep(2 ) # sleep 2
    print('done fetching') # zakończ pierwszy wątek
    return {'data':1} # po zakończeniu zwróć to

async def print_numbers():
    for i in range(10): # rozpocznij drugi wątek
        print(i) # printuj 10 pkt co 0.25
        await asyncio.sleep(0.25) # przerwy co 0.25

async def main():
    task1 = asyncio.create_task(fench_data())  # stworz obiekt 1 taska na funkcji fench data
    task2 = asyncio.create_task(print_numbers()) # stworz obiekt 2 taska na funkcji print numbers

    value = await task1 # await do 1 taska, ktory poczeka az sie zrobi
    print(value) # printnie nam returna
    await task2 # await do 2 taska ktory poczeka az sie wszystkie wartosci wypiszą

asyncio.run(main())