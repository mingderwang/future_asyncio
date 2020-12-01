import asyncio

loop = asyncio.get_event_loop()


def p(val, stop: bool =False) -> None:
    print('----')
    print(stop)
    if stop:
        loop = asyncio.get_event_loop()
        loop.stop()

h = loop.call_soon(p, 'hello')
s = loop.call_soon(p, 'stop', True)
loop.call_later(1, p, 'world', True)
print(h, loop._ready, loop._scheduled, sep='\n')
print(s, loop._ready, loop._scheduled, sep='\n')
loop.run_forever()