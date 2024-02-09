import  asyncio, threading, websockets, json
from websockets import ConnectionClosedOK, ConnectionClosedError
from .ApiLoop import api_socket_loop
from .ApiEvents import ApiEventObject
from .utils import check_port
from ..constants import API_URI
from ..external_libraries import Gtk

class ApiSocket:
    def __init__(self):
        self._uri = None
        self._thread = threading.Thread(
            target = self._start_thread
        )
        self._websocket = None
        self._listeners = []

    def run(self, client_id: str):
        self._uri = f'{API_URI.ws}/feature/{client_id}?client=true'
        self._thread.start()

    def add_listener(self, listener):
        self._listeners.append(listener)

    def remove_listener(self, listener):
        self._listeners.remove(listener)

    async def _websocket_task(self):
        while True:
            try:
                async with websockets.connect(self._uri) as websocket:
                    self._websocket = websocket
                    await api_socket_loop(websocket, self._listeners)

            except ConnectionClosedError as e:
                if check_port(API_URI.host, API_URI.port):
                    print("WebSocket connection failed:", e)
                    await asyncio.sleep(2)
                else:
                    Gtk.main_quit()
                    break

            except ConnectionClosedOK:
                Gtk.main_quit()
                break
                    
    def _start_thread(self):
        loop = asyncio.new_event_loop()
        asyncio.set_event_loop(loop)
        loop.run_until_complete(self._websocket_task())

    def send(self, event: ApiEventObject):
        async def send_event():
            if self._websocket:
                await self._websocket.send(json.dumps(event))

        asyncio.run(send_event())