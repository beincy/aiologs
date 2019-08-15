import asyncio
from aiologs import esHandler
from aiologs import Logger
from aiologs import LoggerConfig

async def t1(tag,i):
    await asyncio.sleep(i)
    print(tag)


async def main():
    # await esHandler.addlogs()
    # await asyncio.gather(
    #     t1("d",0.9),
    #     t1("e",0.4),
    #     t1("b",0.5),

    #     t1("a",0.1),
    #     t1("c",0.2),
       
    #     t1("f",0.6),
    # )
    # tasks=[]
    # tasks.append(asyncio.create_task(t1("d",0.9))) 
    # tasks.append(asyncio.create_task(t1("e",0.4)))
    # tasks.append(asyncio.create_task( t1("b",0.5)))
    # tasks.append(asyncio.create_task(t1("a",0.1)))
    # tasks.append(asyncio.create_task(t1("c",0.2)))
    # tasks.append(asyncio.create_task(t1("f",0.6)))
    # await asyncio.gather(*tasks)

    # ssss()
    LoggerConfig.addConfig({
        "ifFile":0,
        "ifConsole":1,
        "fileName":"",
        "path":'./',
        "projectName":"my-test",
        "asyncWrite":1,
        "dbtype":0,
        "targetDB":["192.168.88.103"],
        "env":"develop"
    })
    log=Logger(0)
    await log.info("m1","c1","c2",{"abc":1},{"bcd":1},"f1","f2")
    await log.warning("m1","c1","c2",{"abc":1},{"bcd":1},"f1","f2")
    await log.error("m1","c1","c2",{"abc":1},{"bcd":1},"f1","f2")
    await log.debug("m1","c1","c2",{"abc":1},{"bcd":1},"f1","f2")


if __name__ == "__main__":
    try:
        import uvloop
        asyncio.set_event_loop_policy(uvloop.EventLoopPolicy())
    except ImportError:
        pass
    asyncio.run(main())
    # loop=asyncio.get_event_loop()
    # loop.run_forever()