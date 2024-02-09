import json, asyncio
from websockets import WebSocketClientProtocol, ConnectionClosedOK, ConnectionClosedError
from .ApiEvents import ApiEventObject
from .utils import run_tasks, task

async def runtime_listeners(event: ApiEventObject, websocket: WebSocketClientProtocol):
    if event['id'] == 'close_client':
        await websocket.send(json.dumps(event))
        await asyncio.sleep(0.2)
        raise ConnectionClosedOK('Receive close client event', 1000)

# API  SOCKET LOOP
async def api_socket_loop(websocket: WebSocketClientProtocol, listeners):
    while True:
        try:
            event: ApiEventObject = json.loads(await websocket.recv())

            await run_tasks([
                task(runtime_listeners(event, websocket))
            ])

            for listener in listeners:
                listener(event)

        except ConnectionClosedError as error:
            raise error

        except ConnectionClosedOK as connection_closed_ok:
            raise connection_closed_ok