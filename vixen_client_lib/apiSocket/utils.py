import socket, asyncio
from typing import List

def check_port(hostname, port):
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(1)

        result = s.connect_ex((hostname, port))
        
        if result == 0: return True
        else: return False
        
    except Exception as e: return False
    finally: s.close()

task = asyncio.create_task

async def run_tasks(tasks: List):
    try:
        for task in tasks: await task
    except Exception as error:
        raise error