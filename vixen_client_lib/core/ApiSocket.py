import  asyncio, threading, websockets

class ApiSocket:
    def __init__(self):
        self._url = None
        self._thread = threading.Thread(
            target = self._start_thread
        )
        self._websocket = None

    def set_client_id(self, client_id: str):
        self._url = f'ws://localhost:6481/feature/{client_id}?subject=true'

    async def _websocket_task(self):
        async with websockets.connect(self._url) as websocket:
            self._websocket = websocket
            while True:
                data = await websocket.recv()

                if data == 'user-close-event':
                    print('Received: ', data)
                    break

    def _start_thread(self):
        loop = asyncio.new_event_loop()
        asyncio.set_event_loop(loop)
        loop.run_until_complete(self._websocket_task())

    def send(self, data):
        async def _send():
            await self._websocket.send(data)

        if self._websocket: asyncio.run(_send())

    def start(self):
        if self._url:
            self._thread.start()

    def stop(self):
        self.send('user-close-event')
        self._thread.join()

api_socket = ApiSocket()