import asyncio

async def main():
    print("main start")
    asyncio.sleep(1)
    print("main end")
    
if __name__ == "__main__":
    asyncio.run(main())