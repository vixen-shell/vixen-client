import  asyncio, threading, websockets
from ..external_libraries import Gtk

class ApiSocket:
    def __init__(self):
        self._url = None
        self._thread = threading.Thread(
            target = self._start_thread
        )
        self._websocket = None
        self._listeners = []

    def run(self, client_id: str):
        self._url = f'ws://localhost:6481/feature/{client_id}?client=true'
        self._thread.start()

    def add_listener(self, listener):
        self._listeners.append(listener)

    def remove_listener(self, listener):
        self._listeners.remove(listener)

    async def _websocket_task(self):
        async with websockets.connect(self._url) as websocket:
            self._websocket = websocket
            while True:
                try:
                    data = await websocket.recv()

                    if data == 'close-event':
                        await websocket.send('close-event')
                        Gtk.main_quit()
                        break

                    for listener in self._listeners:
                        listener(data)

                except Exception as e:
                    Gtk.main_quit()
                    break
                    
    def _start_thread(self):
        loop = asyncio.new_event_loop()
        asyncio.set_event_loop(loop)
        loop.run_until_complete(self._websocket_task())

    def send(self, data):
        async def async_send():
            if self._websocket:
                await self._websocket.send(data)

        asyncio.run(async_send())

api_socket = ApiSocket()